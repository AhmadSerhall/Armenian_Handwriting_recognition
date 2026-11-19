"""Training orchestration placeholder."""

from collections.abc import Mapping
from typing import Any

from armscribe.models.base_model import BaseModel


class ModelTrainer:
    """Coordinate a future model-training run without owning model logic."""

    def __init__(self, model: BaseModel, training_config: Mapping[str, Any]) -> None:
        self.model = model
        self.training_config = dict(training_config)

    def train(self, train_data: Any, validation_data: Any) -> None:
        """Run future training and validation loops."""
        del train_data, validation_data
        raise NotImplementedError("Training orchestration is not implemented.")
