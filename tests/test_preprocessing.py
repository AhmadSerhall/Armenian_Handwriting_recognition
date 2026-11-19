"""Tests for preprocessing infrastructure validation."""

import pytest

from armscribe.data.preprocessing import ImagePreprocessor


def test_preprocessor_accepts_valid_shared_image_size() -> None:
    """A valid two-dimensional image size is retained."""
    preprocessor = ImagePreprocessor(image_size=(64, 64))

    assert preprocessor.image_size == (64, 64)
    assert preprocessor.normalize is True


@pytest.mark.parametrize("image_size", [(0, 64), (64, -1), (64,), (64, 32, 16)])
def test_preprocessor_rejects_invalid_image_sizes(
    image_size: tuple[int, ...],
) -> None:
    """Invalid preprocessing configuration fails before any data is processed."""
    with pytest.raises(ValueError, match="image_size"):
        ImagePreprocessor(image_size=image_size)  # type: ignore[arg-type]
