"""Common minimal interface for project models."""

from collections.abc import Sequence
from typing import Any


class BaseModel:
    """Minimal contract shared by future CNN and k-NN implementations."""

    def fit(self, features: Any, labels: Sequence[int]) -> None:
        """Fit the model when the selected implementation is available."""
        del features, labels
        raise NotImplementedError("Model training is not implemented in Phase 1.")

    def predict(self, features: Any) -> Sequence[int]:
        """Predict labels when the selected implementation is available."""
        del features
        raise NotImplementedError("Model prediction is not implemented in Phase 1.")
