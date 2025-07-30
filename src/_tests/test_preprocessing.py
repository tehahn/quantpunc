import numpy as np
import pytest
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QPushButton
from skimage import data, util

from quantpunc.preprocessing import Preprocessor

params_to_test = [
    (data.camera(), True),
    (np.random.randint(0, 256, size=(1024, 1024, 5), dtype=np.uint16), False),
]


@pytest.mark.parametrize("example_img, should_process", params_to_test)
def test_preprocess_pipeline(
    make_napari_viewer_proxy, qtbot, example_img, should_process
):
    viewer = make_napari_viewer_proxy()
    preprocessing_widget = Preprocessor(viewer=viewer)

    example_img_layer = viewer.add_image(data=example_img, name="example_img")

    example_img_idx = preprocessing_widget.img_combobox.findText(
        example_img_layer.name
    )
    preprocessing_widget.img_combobox.setCurrentIndex(example_img_idx)

    process_button = preprocessing_widget.findChild(
        QPushButton, name="process_button"
    )

    qtbot.mouseClick(process_button, Qt.LeftButton)

    if should_process:
        assert "example_img_processed" in viewer.layers
    else:
        assert "example_img_processed" not in viewer.layers


def test_process_with_no_selection(make_napari_viewer_proxy):
    viewer = make_napari_viewer_proxy()
    preprocessing_widget = Preprocessor(viewer=viewer)

    example_img_idx = preprocessing_widget.img_combobox.findText("None")
    preprocessing_widget.img_combobox.setCurrentIndex(example_img_idx)

    preprocessing_widget.process_images()

    assert len(viewer.layers) == 0


def run_denoising_test(viewer, preprocessing_widget, method, mode):
    method_idx = preprocessing_widget.method_combobox.findText(method)
    preprocessing_widget.method_combobox.setCurrentIndex(method_idx)

    mode_idx = preprocessing_widget.mode_combobox.findText(mode)
    preprocessing_widget.mode_combobox.setCurrentIndex(mode_idx)

    preprocessing_widget.process_images()

    assert "example_img_processed" in viewer.layers

    return viewer.layers["example_img_processed"].data.copy()


@pytest.mark.parametrize("method", ["BayesShrink", "VisuShrink"])
def test_different_denoising_methods(make_napari_viewer_proxy, method):
    viewer = make_napari_viewer_proxy()
    preprocessing_widget = Preprocessor(viewer=viewer)

    example_img = data.camera()
    example_img = util.random_noise(example_img, mode="gaussian", var=0.01)
    example_img = (example_img * 255).astype(np.uint16)

    example_img_layer = viewer.add_image(data=example_img, name="example_img")

    example_img_idx = preprocessing_widget.img_combobox.findText(
        example_img_layer.name
    )
    preprocessing_widget.img_combobox.setCurrentIndex(example_img_idx)

    soft_img = run_denoising_test(viewer, preprocessing_widget, method, "soft")
    hard_img = run_denoising_test(viewer, preprocessing_widget, method, "hard")

    assert not np.array_equal(soft_img, hard_img)
