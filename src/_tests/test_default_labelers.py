from pathlib import Path
from typing import cast

import numpy as np
import pytest
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QPushButton
from tifffile import imread

from quantpunc.quantification.default_puncta_labelers import (
    RFCPunctaLabeler,
)
from quantpunc.quantification.puncta_analyzer import PunctaAnalyzer
from quantpunc.table.table_widget import TableWidget

labelers_to_test = [
    "Laplacian of Gaussian",
    "Difference of Gaussians",
    "Determinant of Hessian",
    "Random Forest Classifier",
]


@pytest.mark.parametrize("labeler", labelers_to_test)
def test_blob_labelers(make_napari_viewer_proxy, qtbot, labeler) -> None:
    viewer = make_napari_viewer_proxy()
    table_widget = TableWidget(viewer=viewer)
    puncta_analyzer = PunctaAnalyzer(viewer=viewer, table_widget=table_widget)

    test_dir = Path(__file__).parent
    example_img_path = test_dir / "data" / "hello_world.tif"
    example_mask_path = test_dir / "data" / "hello_world_mask.tif"

    example_img = imread(example_img_path)
    example_mask = imread(example_mask_path)

    viewer.add_image(data=example_img, name="hello_world")
    viewer.add_image(data=example_mask, name="hello_world_mask")

    example_img_idx = puncta_analyzer.img_combobox.findText("hello_world")
    puncta_analyzer.img_combobox.setCurrentIndex(example_img_idx)

    blob_labeler_idx = puncta_analyzer.method_combobox.findText(labeler)
    puncta_analyzer.method_combobox.setCurrentIndex(blob_labeler_idx)

    if labeler == "Random Forest Classifier":
        example_annotations_path = (
            test_dir / "data" / "hello_world_annotations.tif"
        )
        example_annotations = imread(example_annotations_path)
        viewer.add_labels(
            data=example_annotations, name="hello_world_annotations"
        )

        puncta_analyzer.blob_labeler = cast(
            RFCPunctaLabeler, puncta_analyzer.blob_labeler
        )

        annotation_idx = (
            puncta_analyzer.blob_labeler.annotation_combobox.findText(
                "hello_world_annotations"
            )
        )
        puncta_analyzer.blob_labeler.annotation_combobox.setCurrentIndex(
            annotation_idx
        )

        puncta_analyzer.blob_labeler.puncta_line_edit.setText("2")
        puncta_analyzer.blob_labeler.background_line_edit.setText("3")

        train_button = puncta_analyzer.findChild(
            QPushButton, name="train_button"
        )
        qtbot.mouseClick(train_button, Qt.MouseButton.LeftButton)

    masks_to_test = ["None", "hello_world_mask"]

    for mask_name in masks_to_test:
        mask_idx = puncta_analyzer.mask_combobox.findText(mask_name)
        puncta_analyzer.mask_combobox.setCurrentIndex(mask_idx)

        label_button = puncta_analyzer.findChild(
            QPushButton, name="label_button"
        )
        count_button = puncta_analyzer.findChild(
            QPushButton, name="count_button"
        )

        qtbot.mouseClick(label_button, Qt.MouseButton.LeftButton)

        assert "hello_world_puncta" in viewer.layers

        qtbot.mouseClick(count_button, Qt.MouseButton.LeftButton)

        assert table_widget.save_initialized

        del viewer.layers["hello_world_puncta"]


@pytest.mark.parametrize("labeler", labelers_to_test)
def test_labeling_with_no_selection(make_napari_viewer_proxy, labeler) -> None:
    viewer = make_napari_viewer_proxy()
    table_widget = TableWidget(viewer=viewer)
    puncta_analyzer = PunctaAnalyzer(viewer=viewer, table_widget=table_widget)

    blob_labeler_idx = puncta_analyzer.method_combobox.findText(labeler)
    puncta_analyzer.method_combobox.setCurrentIndex(blob_labeler_idx)

    example_img_idx = puncta_analyzer.img_combobox.findText("None")
    puncta_analyzer.img_combobox.setCurrentIndex(example_img_idx)

    puncta_analyzer.get_puncta_labels()

    assert len(viewer.layers) == 0

    assert not table_widget.save_initialized


@pytest.mark.parametrize("labeler", labelers_to_test)
def test_rejects_multilayer_img(make_napari_viewer_proxy, labeler) -> None:
    viewer = make_napari_viewer_proxy()
    table_widget = TableWidget(viewer=viewer)
    puncta_analyzer = PunctaAnalyzer(viewer=viewer, table_widget=table_widget)

    blob_labeler_idx = puncta_analyzer.method_combobox.findText(labeler)
    puncta_analyzer.method_combobox.setCurrentIndex(blob_labeler_idx)

    example_img = np.random.randint(
        0, 256, size=(1024, 1024, 5), dtype=np.uint16
    )
    viewer.add_image(data=example_img, name="example_img")

    example_img_idx = puncta_analyzer.img_combobox.findText("example_img")
    puncta_analyzer.img_combobox.setCurrentIndex(example_img_idx)

    puncta_analyzer.get_puncta_labels()

    assert "example_img_puncta" not in viewer.layers

    assert not table_widget.save_initialized
