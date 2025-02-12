"""Feature engineering."""

import argparse

import polars as pl

from ds_template.config import MAIN_DIR, logger


def feature(df: pl.DataFrame, column_name: int) -> pl.DataFrame:
    """Feature engineering."""
    logger.info(f"Column name: {column_name}")
    return df.select(pl.col(column_name)).count()


def main(input_path: str, output_path: str, column_name: str) -> None:
    """Feature engineering."""
    input_df = pl.scan_parquet(MAIN_DIR / input_path)
    logger.info(f"Loaded data from {input_path}")

    logger.info("Feature engineering...")
    output_df = feature(input_df, column_name)
    logger.info("Feature engineering complete.")

    full_output_path = MAIN_DIR / output_path
    full_output_path.parent.mkdir(parents=True, exist_ok=True)
    output_df.collect().write_parquet(full_output_path)
    logger.info(f"Saved data to {output_path}")


def cli() -> None:
    """Feature engineering."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)
    parser.add_argument("--column_name", type=str, required=True)
    args = parser.parse_args()

    main(args.input_path, args.output_path, args.column_name)


if __name__ == "__main__":
    cli()
