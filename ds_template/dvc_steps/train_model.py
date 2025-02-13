"""Train model."""

import argparse
import pickle
from pathlib import Path

import polars as pl

from ds_template.config import MAIN_DIR
from ds_template.models.constant_model import ConstantModel


def read_lf(*args: Path) -> pl.LazyFrame:
    """Read lazy frames from paths."""
    return pl.concat(
        (pl.scan_parquet(MAIN_DIR / path) for path in args),
        how="horizontal",
        rechunk=True,
        parallel=True,
    )


def main(
    feature_path: Path,
    data_path: Path,
    output_path: Path,
    model_path: Path,
    constant: float,
) -> None:
    """Train model."""
    lf = read_lf(feature_path, data_path)

    model = ConstantModel(constant)

    full_output_path = MAIN_DIR / output_path
    full_output_path.parent.mkdir(parents=True, exist_ok=True)
    model.fit_predict(lf).collect().write_parquet(full_output_path)

    full_model_path = MAIN_DIR / model_path
    full_model_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_model_path, "wb") as f:
        pickle.dump(model, f)


def cli() -> None:
    """Train model."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--feature-path", type=Path, required=True)
    parser.add_argument("--data-path", type=Path, required=True)
    parser.add_argument("--output-path", type=Path, required=True)
    parser.add_argument("--model-path", type=Path, required=True)
    parser.add_argument("--constant", type=float, required=True)
    args = parser.parse_args()

    main(
        args.feature_path,
        args.data_path,
        args.output_path,
        args.model_path,
        args.constant,
    )


if __name__ == "__main__":
    cli()
