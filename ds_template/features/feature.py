"""Feature abstract base class."""

import abc

import polars as pl


class Feature(metaclass=abc.ABCMeta):
    """Feature abstract base class."""

    @abc.abstractmethod
    def fit(self, X: pl.DataFrame, y: pl.DataFrame | None = None) -> "Feature":
        """Fit the feature."""
        ...

    @abc.abstractmethod
    def transform(self, X: pl.DataFrame) -> pl.DataFrame:
        """Transform the feature."""
        ...

    @abc.abstractmethod
    def fit_transform(self, X: pl.DataFrame, y: pl.DataFrame | None = None) -> pl.DataFrame:
        """Fit and transform the feature."""
        ...
