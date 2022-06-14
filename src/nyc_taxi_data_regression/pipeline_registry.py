"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from nyc_taxi_data_regression.pipelines import prep, train, transform


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    prepare_data = prep.create_pipeline()
    transform_data = transform.create_pipeline()
    train_model = train.create_pipeline()

    return {
        "__default__": prepare_data
        + pipeline(transform_data, inputs={"clean_data": "merged_data"})
        + pipeline(train_model, inputs={"training_data": "transformed_data"}),
        "prepare_sample_data": prepare_data,
        "transform_sample_data": pipeline(
            transform_data, inputs={"clean_data": "merged_data"}
        ),
        "train_with_sample_data": pipeline(
            train_model, inputs={"training_data": "transformed_data"}
        ),
    }
