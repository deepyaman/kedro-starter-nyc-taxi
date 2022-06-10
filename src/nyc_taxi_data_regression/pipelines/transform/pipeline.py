from kedro.pipeline import Pipeline, node, pipeline

from .nodes import transform


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=transform,
                inputs="clean_data",
                outputs="transformed_data",
                name="TaxiFeatureEngineering",
            )
        ]
    )
