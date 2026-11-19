"""Shared image-preprocessing configuration and interface."""

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ImagePreprocessor:
    """Validate and retain preprocessing settings shared by all model paths."""

    image_size: tuple[int, int] = (64, 64)
    normalize: bool = True
    invert_colors: bool = False

    def __post_init__(self) -> None:
        if len(self.image_size) != 2:
            raise ValueError("image_size must contain exactly width and height.")
        if any(not isinstance(size, int) or size <= 0 for size in self.image_size):
            raise ValueError("image_size values must be positive integers.")

    def preprocess(self, image: Any) -> Any:
        """Apply the future common image pipeline.

        This method is intentionally deferred until raw dataset characteristics
        and normalization choices are documented in the datasheet.
        """
        del image
        raise NotImplementedError(
            "Image preprocessing will be implemented after dataset inspection."
        )
