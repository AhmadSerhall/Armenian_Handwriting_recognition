"""Reproducibility helpers for future experiments."""

import random


def set_global_seed(seed: int) -> None:
    """Seed standard-library, NumPy, and PyTorch RNGs when available."""
    if not isinstance(seed, int):
        raise TypeError("seed must be an integer.")

    random.seed(seed)
    try:
        import numpy as np

        np.random.seed(seed)
    except ImportError:
        pass

    try:
        import torch

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass
