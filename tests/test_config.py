"""Tests for configuration loading and Phase 1 defaults."""

from armscribe.utils.config import ConfigManager


def test_default_configuration_loads_with_expected_values() -> None:
    """The shared configuration exposes agreed infrastructure defaults."""
    config = ConfigManager().load_default()

    assert config["project"]["num_classes"] == 39
    assert config["data"]["image_size"] == [64, 64]
    assert config["training"]["seeds"] == [42, 123, 2026]
    assert config["data"]["split"]["writer_independent"] is True


def test_cnn_override_merges_with_defaults() -> None:
    """Model-specific files preserve required shared configuration values."""
    config = ConfigManager().load_experiment("cnn")

    assert config["model"]["name"] == "cnn"
    assert config["training"]["augmentation_enabled"] is True
    assert config["paths"]["checkpoints"] == "checkpoints"
