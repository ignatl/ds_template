"""Trainable abstract base class."""

import abc

import polars as pl


class Trainable(metaclass=abc.ABCMeta):
    """Trainable abstract base class."""

    @abc.abstractmethod
    def fit(self, X: pl.DataFrame, y: pl.DataFrame | None = None) -> "Trainable":
        """Fit the model."""
        ...

    @abc.abstractmethod
    def predict(self, X: pl.DataFrame) -> pl.DataFrame:
        """Predict the model."""
        ...

    @abc.abstractmethod
    def fit_predict(self, X: pl.DataFrame, y: pl.DataFrame | None = None) -> pl.DataFrame:
        """Fit and predict the model."""
        ...
