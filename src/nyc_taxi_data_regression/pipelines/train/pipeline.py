from kedro.pipeline import Pipeline, node, pipeline

from .nodes import train


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=train,
                inputs="training_data",
                outputs=["test_data", "model_output"],
                name="TrainLinearRegressionModel",
            )
        ]
    )
