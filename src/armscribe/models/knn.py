"""Placeholder for the future scikit-learn k-NN baseline."""

from .base_model import BaseModel


class KNNClassifier(BaseModel):
    """Hold validated k-NN settings without fitting a baseline yet."""

    def __init__(self, n_neighbors: int = 5) -> None:
        if n_neighbors <= 0:
            raise ValueError("n_neighbors must be a positive integer.")
        self.n_neighbors = n_neighbors
