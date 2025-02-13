"""Inference step."""

import argparse
import pickle
from pathlib import Path

import polars as pl
from polars.testing import assert_frame_equal

from ds_template.config import MAIN_DIR
from ds_template.inference.inference import Inference


def main(
    train_data_path: Path,
    y_data_path: Path,
    inference_data_path: Path,
    feature_path: Path,
    model_path: Path,
    output_path: Path,
    inference_path: Path,
) -> None:
    """Main function."""
    train_data = pl.scan_parquet(train_data_path)
    y_data = pl.scan_csv(y_data_path)
    inference_data = pl.scan_csv(inference_data_path)

    with feature_path.open("rb") as f:
        feature = pickle.load(f)

    with model_path.open("rb") as f:
        model = pickle.load(f)

    inference = Inference(feature, model)
    train_lf = inference.inference(train_data)
    assert_frame_equal(train_lf, y_data)

    inference_lf = inference.inference(inference_data)
    full_output_path = MAIN_DIR / output_path
    full_output_path.parent.mkdir(parents=True, exist_ok=True)
    inference_lf.collect().write_parquet(full_output_path)

    full_inference_path = MAIN_DIR / inference_path
    full_inference_path.parent.mkdir(parents=True, exist_ok=True)
    with full_inference_path.open("wb") as f:
        pickle.dump(inference, f)


def cli() -> None:
    """CLI."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_data_path", type=Path, required=True)
    parser.add_argument("--y_data_path", type=Path, required=True)
    parser.add_argument("--inference_data_path", type=Path, required=True)
    parser.add_argument("--feature_path", type=Path, required=True)
    parser.add_argument("--model_path", type=Path, required=True)
    parser.add_argument("--output_path", type=Path, required=True)
    parser.add_argument("--inference_path", type=Path, required=True)
    args = parser.parse_args()
    main(**vars(args))


if __name__ == "__main__":
    cli()
