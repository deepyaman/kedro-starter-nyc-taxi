"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from nyc_taxi_data_regression.pipelines import prep


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    prepare_data = prep.create_pipeline()

    return {
        "__default__": prepare_data,
        "prepare_sample_data": prepare_data,
    }
