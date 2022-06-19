""" MAke generation synthetic data for study pipeline """
import os
from typing import NoReturn
import click
import numpy as np

from sklearn.datasets import load_breast_cancer


@click.command("generate")
@click.option("--output_path")
def generate_data_cancer(output_path: str) -> NoReturn:
    """ func for data generation """
    n_entries = np.random.randint(10, 568)
    X, y = load_breast_cancer(return_X_y=True, as_frame=True)

    os.makedirs(output_path, exist_ok=True)

    X[:n_entries].to_csv(os.path.join(output_path, 'data.csv'))
    y[:n_entries].to_csv(os.path.join(output_path, 'target.csv'))


if __name__ == '__main__':
    generate_data_cancer()
