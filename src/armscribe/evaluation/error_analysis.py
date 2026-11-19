"""Error-analysis interface for future evaluation reports."""

from collections.abc import Sequence
from typing import Any


class ErrorAnalyzer:
    """Define the location for per-character error analysis."""

    def analyze(
        self,
        expected_labels: Sequence[int],
        predicted_labels: Sequence[int],
    ) -> dict[str, Any]:
        """Analyze real errors after evaluation is implemented."""
        del expected_labels, predicted_labels
        raise NotImplementedError("Error analysis is not implemented.")
