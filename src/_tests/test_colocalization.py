from pathlib import Path

import numpy as np
import pytest
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QPushButton
from tifffile import imread

from quantpunc.quantification.colocalization import ColocalizationWidget
from quantpunc.table.table_widget import TableWidget


@pytest.mark.parametrize("mask_selection", ["None", "hello_world_mask"])
def test_colocalization(
    make_napari_viewer_proxy, qtbot, mask_selection
) -> None:
    viewer = make_napari_viewer_proxy()
    table_widget = TableWidget(viewer=viewer)
    colocalization_widget = ColocalizationWidget(
        viewer=viewer, table_widget=table_widget
    )

    test_dir = Path(__file__).parent

    coloc_0 = imread(test_dir / "data" / "coloc_0.tif")
    coloc_1 = imread(test_dir / "data" / "coloc_1.tif")
    example_masks = imread(test_dir / "data" / "hello_world_mask.tif")

    viewer.add_labels(data=coloc_0, name="coloc_0")
    viewer.add_labels(data=coloc_1, name="coloc_1")
    viewer.add_image(data=example_masks, name="hello_world_mask")

    coloc_0_idx = colocalization_widget.first_combobox.findText("coloc_0")
    colocalization_widget.first_combobox.setCurrentIndex(coloc_0_idx)

    coloc_1_idx = colocalization_widget.second_combobox.findText("coloc_1")
    colocalization_widget.second_combobox.setCurrentIndex(coloc_1_idx)

    mask_idx = colocalization_widget.mask_combobox.findText(mask_selection)
    colocalization_widget.mask_combobox.setCurrentIndex(mask_idx)

    iou_button = colocalization_widget.findChild(
        QPushButton, name="iou_button"
    )
    qtbot.mouseClick(iou_button, Qt.MouseButton.LeftButton)

    if mask_selection == "None":
        value_idx = table_widget.iou_table_view.dict_model.index(0, 0)
        value = table_widget.iou_table_view.dict_model.data(value_idx)

        assert int(value) == -1
    else:
        value_idx = table_widget.iou_table_view.dict_model.index(0, 0)
        value = table_widget.iou_table_view.dict_model.data(value_idx)

        assert int(value) != -1


def test_coloc_with_no_selection(make_napari_viewer_proxy) -> None:
    viewer = make_napari_viewer_proxy()
    table_widget = TableWidget(viewer=viewer)
    colocalization_widget = ColocalizationWidget(
        viewer=viewer, table_widget=table_widget
    )

    test_dir = Path(__file__).parent
    coloc_0 = imread(test_dir / "data" / "coloc_0.tif")
    viewer.add_labels(data=coloc_0, name="coloc_0")

    coloc_0_idx = colocalization_widget.first_combobox.findText("coloc_0")
    colocalization_widget.first_combobox.setCurrentIndex(coloc_0_idx)

    none_idx = colocalization_widget.second_combobox.findText("None")
    colocalization_widget.second_combobox.setCurrentIndex(none_idx)

    colocalization_widget.get_iou()

    value_idx = table_widget.iou_table_view.dict_model.index(0, 0)
    value = table_widget.iou_table_view.dict_model.data(value_idx)

    assert value is None


def test_rejects_multidimensional_img(make_napari_viewer_proxy) -> None:
    viewer = make_napari_viewer_proxy()
    table_widget = TableWidget(viewer=viewer)
    colocalization_widget = ColocalizationWidget(
        viewer=viewer, table_widget=table_widget
    )

    test_dir = Path(__file__).parent
    coloc_0 = imread(test_dir / "data" / "coloc_0.tif")
    viewer.add_labels(data=coloc_0, name="coloc_0")

    example_labels = np.random.randint(
        0, 256, size=(1024, 1024, 5), dtype=np.uint16
    )
    viewer.add_labels(data=example_labels, name="example_labels")

    coloc_0_idx = colocalization_widget.first_combobox.findText("coloc_0")
    colocalization_widget.first_combobox.setCurrentIndex(coloc_0_idx)

    labels_idx = colocalization_widget.second_combobox.findText(
        "example_labels"
    )
    colocalization_widget.second_combobox.setCurrentIndex(labels_idx)

    colocalization_widget.get_iou()

    value_idx = table_widget.iou_table_view.dict_model.index(0, 0)
    value = table_widget.iou_table_view.dict_model.data(value_idx)

    assert value is None
