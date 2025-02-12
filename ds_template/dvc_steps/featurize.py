"""Feature engineering."""

import argparse
import pickle
from pathlib import Path

import polars as pl

from ds_template.config import MAIN_DIR, logger
from ds_template.features.mock_feature import MockFeature


def feature(df: pl.DataFrame, column_name: int) -> tuple[pl.DataFrame, MockFeature]:
    """Feature engineering."""
    logger.info(f"Column name: {column_name}")
    mock_feature = MockFeature(column_name)
    df = mock_feature.fit_transform(df)
    return df, mock_feature


def main(input_path: Path, output_path: Path, obj_path: Path, column_name: str) -> None:
    """Feature engineering."""
    full_input_path = MAIN_DIR / input_path
    input_df = pl.scan_parquet(full_input_path)
    logger.info(f"Loaded data from {full_input_path}")

    logger.info("Feature engineering...")
    output_df, mock_feature = feature(input_df, column_name)
    logger.info("Feature engineering complete.")

    full_output_path = MAIN_DIR / output_path
    full_output_path.parent.mkdir(parents=True, exist_ok=True)
    output_df.collect().write_parquet(full_output_path)
    logger.info(f"Saved data to {output_path}")

    full_obj_path = MAIN_DIR / obj_path
    full_obj_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_obj_path, "wb") as f:
        pickle.dump(mock_feature, f)
    logger.info(f"Saved object to {obj_path}")


def cli() -> None:
    """Feature engineering."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)
    parser.add_argument("--obj_path", type=str, required=True)
    parser.add_argument("--column_name", type=str, required=True)
    args = parser.parse_args()

    main(args.input_path, args.output_path, args.obj_path, args.column_name)


if __name__ == "__main__":
    cli()
