from kedro.pipeline import Pipeline, node, pipeline

from .nodes import prep


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=prep,
                inputs=["raw_green_data", "raw_yellow_data"],
                outputs=["output_green", "output_yellow", "merged_data"],
                name="PrepTaxiData",
            )
        ]
    )
