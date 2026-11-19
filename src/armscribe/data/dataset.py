"""Dataset interface for Armenian handwriting samples."""

from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    from torch.utils.data import Dataset
except ImportError:  # Allows structural imports before optional dependencies.
    class Dataset:  # type: ignore[no-redef]
        """Minimal fallback when PyTorch is not installed."""


@dataclass(frozen=True, slots=True)
class DatasetSample:
    """Metadata needed to load one labelled handwriting image later."""

    image_path: Path
    label: int
    writer_id: str | None = None


class ArmenianDataset(Dataset):
    """PyTorch-compatible dataset contract for labelled Armenian characters.

    Loading formats and preprocessing decisions are intentionally deferred until
    the dataset audit in the next phase.
    """

    def __init__(
        self,
        samples: Sequence[DatasetSample],
        transform: Callable[[Any], Any] | None = None,
    ) -> None:
        self.samples = list(samples)
        self.transform = transform

    def __len__(self) -> int:
        """Return the number of indexed sample records."""
        return len(self.samples)

    def __getitem__(self, index: int) -> tuple[Any, int]:
        """Load an image and label once the dataset format is finalized."""
        del index
        raise NotImplementedError(
            "Dataset image loading will be implemented after data inspection."
        )
