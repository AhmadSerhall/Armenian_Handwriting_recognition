"""Inference contract for the future demo application."""

from typing import Any

from armscribe.models.base_model import BaseModel


class CharacterPredictor:
    """Load a future trained model and expose one prediction entry point."""

    def __init__(self, model: BaseModel) -> None:
        self.model = model

    def predict(self, image: Any) -> dict[str, Any]:
        """Return a real class, confidence, and top classes in a later phase."""
        del image
        raise NotImplementedError("Inference is not implemented in Phase 1.")
