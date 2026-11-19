"""Evaluation interface for future experiment metrics."""

from collections.abc import Sequence
from typing import Any


class ModelEvaluator:
    """Define the location for future classification metrics and matrices."""

    def evaluate(
        self,
        expected_labels: Sequence[int],
        predicted_labels: Sequence[int],
    ) -> dict[str, Any]:
        """Calculate metrics after a model produces real predictions."""
        del expected_labels, predicted_labels
        raise NotImplementedError("Evaluation metrics are not implemented.")
