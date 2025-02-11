#!/usr/bin/env python3

"""Load and clean data."""

import argparse

import polars as pl

from ds_template.config import MAIN_DIR, logger


def load_and_clean(input_path: str, output_path: str) -> None:
    """Load and clean data."""
    df = pl.read_csv(MAIN_DIR / input_path)
    logger.info(f"Loaded data from {input_path} and cleaned it (no)")

    full_output_path = MAIN_DIR / output_path
    full_output_path.parent.mkdir(parents=True, exist_ok=True)
    df.write_parquet(full_output_path)
    logger.info(f"Saved data to {output_path}")


def cli() -> None:
    """CLI for loading and cleaning data."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)
    args = parser.parse_args()

    load_and_clean(args.input_path, args.output_path)


if __name__ == "__main__":
    cli()
