from pathlib import Path

import numpy as np
import pytest
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QPushButton
from tifffile import imread

from quantpunc.table.table_widget import TableWidget
from quantpunc.watershed import WatershedWidget


@pytest.mark.parametrize(
    "seed_point_layer", ["None", "hello_world_seed_points"]
)
@pytest.mark.parametrize(
    "elevation_map_transform", ["Distance Transform", "Sobel"]
)
def test_watershed(
    make_napari_viewer_proxy, qtbot, seed_point_layer, elevation_map_transform
) -> None:
    viewer = make_napari_viewer_proxy()
    table_widget = TableWidget(viewer=viewer)
    watershed_widget = WatershedWidget(
        viewer=viewer, table_widget=table_widget
    )

    test_dir = Path(__file__).parent

    example_labels = imread(test_dir / "data" / "hello_world_labels.tif")
    example_seed_points = imread(
        test_dir / "data" / "hello_world_seed_points.tif"
    )

    viewer.add_labels(data=example_labels, name="hello_world_labels")
    viewer.add_labels(data=example_seed_points, name="hello_world_seed_points")

    labels_idx = watershed_widget.img_combobox.findText("hello_world_labels")
    watershed_widget.img_combobox.setCurrentIndex(labels_idx)

    transform_idx = watershed_widget.elevation_map_combobox.findText(
        elevation_map_transform
    )
    watershed_widget.elevation_map_combobox.setCurrentIndex(transform_idx)

    seed_points_idx = watershed_widget.seed_point_combobox.findText(
        seed_point_layer
    )
    print(seed_points_idx)
    watershed_widget.seed_point_combobox.setCurrentIndex(seed_points_idx)

    watershed_button = watershed_widget.findChild(
        QPushButton, name="watershed_button"
    )
    qtbot.mouseClick(watershed_button, Qt.MouseButton.LeftButton)

    assert "hello_world_labels_watershed" in viewer.layers

    del viewer.layers["hello_world_labels_watershed"]


def test_watershed_with_no_selection(make_napari_viewer_proxy) -> None:
    viewer = make_napari_viewer_proxy()
    table_widget = TableWidget(viewer=viewer)
    watershed_widget = WatershedWidget(
        viewer=viewer, table_widget=table_widget
    )

    labels_idx = watershed_widget.img_combobox.findText("None")
    watershed_widget.img_combobox.setCurrentIndex(labels_idx)

    watershed_widget.watershed_layer()

    assert len(viewer.layers) == 0


def test_rejects_multidimensional_img(make_napari_viewer_proxy) -> None:
    viewer = make_napari_viewer_proxy()
    table_widget = TableWidget(viewer=viewer)
    watershed_widget = WatershedWidget(
        viewer=viewer, table_widget=table_widget
    )

    example_labels = np.random.randint(
        0, 256, size=(1024, 1024, 5), dtype=np.uint16
    )
    viewer.add_labels(data=example_labels, name="example_labels")

    labels_idx = watershed_widget.img_combobox.findText("example_labels")
    watershed_widget.img_combobox.setCurrentIndex(labels_idx)

    watershed_widget.watershed_layer()

    assert "example_labels_watershed" not in viewer.layers
