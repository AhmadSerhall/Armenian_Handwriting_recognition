"""Placeholder for the future PyTorch convolutional neural network."""

from typing import Any

from .base_model import BaseModel


class ArmenianCNN(BaseModel):
    """CNN configuration holder; network layers are deferred to Phase 3."""

    def __init__(self, num_classes: int = 39, input_channels: int = 1) -> None:
        if num_classes != 39:
            raise ValueError("ArmScribe Phase 1 is configured for 39 classes.")
        if input_channels <= 0:
            raise ValueError("input_channels must be a positive integer.")
        self.num_classes = num_classes
        self.input_channels = input_channels

    def forward(self, inputs: Any) -> Any:
        """Define the future PyTorch forward pass."""
        del inputs
        raise NotImplementedError("CNN layers are not implemented in Phase 1.")
