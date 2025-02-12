#!/usr/bin/env python3

"""Load and clean data."""

import argparse

import polars as pl

from ds_template.config import MAIN_DIR, logger


def load_clean(df: pl.DataFrame) -> pl.DataFrame:
    """Load and clean data."""
    return df


def main(input_path: str, output_path: str) -> None:
    """Load and clean data."""
    input_df = pl.scan_csv(MAIN_DIR / input_path)
    logger.info(f"Loaded data from {input_path} and cleaned it (no)")

    output_df = load_clean(input_df)

    full_output_path = MAIN_DIR / output_path
    full_output_path.parent.mkdir(parents=True, exist_ok=True)
    output_df.collect().write_parquet(full_output_path)
    logger.info(f"Saved data to {output_path}")


def cli() -> None:
    """CLI for loading and cleaning data."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)
    args = parser.parse_args()

    main(args.input_path, args.output_path)


if __name__ == "__main__":
    cli()
