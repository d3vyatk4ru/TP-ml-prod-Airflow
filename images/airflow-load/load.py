import os
import click

import pandas as pd


@click.command("load")
@click.option("--input-path")
@click.option("--temp-path")
def load(input_path: str, temp_path: str) -> None:
    """
    The data is loaded and stored in the local temp directory
    :param filepath:
    :return:
    """
    features = pd.read_csv(os.path.join(input_path, "data.csv"), index_col=0)
    target = pd.read_csv(os.path.join(input_path, "target.csv"), index_col=0)

    dataframe = features.merge(target, right_index=True, left_index=True)
    os.makedirs(temp_path, exist_ok=True)
    print(temp_path)
    dataframe.to_csv(os.path.join(temp_path, "dataframe.csv"))


if __name__ == "__main__":
    load()