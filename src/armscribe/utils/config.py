"""YAML configuration loading and validation."""

from collections.abc import Mapping
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml


class ConfigManager:
    """Load project-relative YAML configuration files with basic validation."""

    def __init__(self, project_root: Path | str | None = None) -> None:
        default_root = Path(__file__).resolve().parents[3]
        self.project_root = Path(project_root or default_root).resolve()

    def load(self, path: Path | str) -> dict[str, Any]:
        """Load and validate one YAML mapping from a project-relative path."""
        config_path = Path(path)
        if not config_path.is_absolute():
            config_path = self.project_root / config_path
        if not config_path.is_file():
            raise FileNotFoundError(f"Configuration file not found: {config_path}")

        with config_path.open(encoding="utf-8") as config_file:
            config = yaml.safe_load(config_file) or {}
        if not isinstance(config, dict):
            raise ValueError("The configuration root must be a YAML mapping.")
        self.validate(config)
        return config

    def load_default(self) -> dict[str, Any]:
        """Load the shared Phase 1 default configuration."""
        return self.load("configs/default.yaml")

    def load_experiment(self, model_name: str) -> dict[str, Any]:
        """Merge a model override into the validated shared defaults."""
        if model_name not in {"cnn", "knn"}:
            raise ValueError("model_name must be either 'cnn' or 'knn'.")
        default_config = self.load_default()
        override_path = self.project_root / "configs" / f"{model_name}.yaml"
        with override_path.open(encoding="utf-8") as config_file:
            override = yaml.safe_load(config_file) or {}
        if not isinstance(override, dict):
            raise ValueError("The model override root must be a YAML mapping.")

        merged = self._merge(default_config, override)
        self.validate(merged)
        return merged

    def validate(self, config: Mapping[str, Any]) -> None:
        """Validate the infrastructure settings required by Phase 1."""
        try:
            num_classes = config["project"]["num_classes"]
            image_size = config["data"]["image_size"]
            split = config["data"]["split"]
            seeds = config["training"]["seeds"]
        except (KeyError, TypeError) as error:
            raise ValueError(
                "Configuration is missing required project, data, or training values."
            ) from error

        if num_classes != 39:
            raise ValueError("project.num_classes must be 39.")
        if (
            not isinstance(image_size, (list, tuple))
            or len(image_size) != 2
            or any(not isinstance(value, int) or value <= 0 for value in image_size)
        ):
            raise ValueError("data.image_size must contain two positive integers.")
        if not isinstance(seeds, list) or len(seeds) != 3:
            raise ValueError("training.seeds must contain exactly three seeds.")
        if not all(isinstance(seed, int) for seed in seeds):
            raise ValueError("training.seeds values must be integers.")

        split_keys = {"train", "validation", "test"}
        if set(split) != split_keys | {"writer_independent"}:
            raise ValueError(
                "data.split must define train, validation, test, and "
                "writer_independent."
            )
        proportions = [split[name] for name in sorted(split_keys)]
        if (
            not all(isinstance(value, (int, float)) and value > 0 for value in proportions)
            or abs(sum(proportions) - 1.0) > 1e-9
        ):
            raise ValueError("data.split proportions must be positive and sum to 1.0.")
        if split["writer_independent"] is not True:
            raise ValueError("data.split.writer_independent must be true.")

    @staticmethod
    def _merge(
        base: Mapping[str, Any],
        override: Mapping[str, Any],
    ) -> dict[str, Any]:
        """Recursively merge an override into a copy of a base mapping."""
        merged = deepcopy(dict(base))
        for key, value in override.items():
            if isinstance(value, Mapping) and isinstance(merged.get(key), Mapping):
                merged[key] = ConfigManager._merge(merged[key], value)
            else:
                merged[key] = deepcopy(value)
        return merged
