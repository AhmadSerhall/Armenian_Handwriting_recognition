"""Model interfaces for ArmScribe AI."""

from .base_model import BaseModel
from .cnn import ArmenianCNN
from .knn import KNNClassifier

__all__ = ["ArmenianCNN", "BaseModel", "KNNClassifier"]
