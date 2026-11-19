"""Training-only augmentation interface."""

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class DataAugmentor:
    """Own augmentation settings without applying transformations yet."""

    enabled: bool = False

    def augment(self, image: Any) -> Any:
        """Return unmodified input when disabled; defer enabled transforms."""
        if not self.enabled:
            return image
        raise NotImplementedError(
            "Training augmentation will be implemented after baseline setup."
        )
