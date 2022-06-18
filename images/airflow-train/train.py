import os
from typing import NoReturn
import click
import pickle

import pandas as pd
from sklearn.linear_model import LogisticRegression


@click.command("train")
@click.option("--load_data_path")
@click.option("--save_model_path")
def train_model(train_path: str, model_path: str) -> NoReturn:
    """ Train model """

    model = LogisticRegression(
        random_state=42,
        max_iter=1000,
    )

    dataframe = pd.read_csv(os.path.join(train_path, 'train.csv'), index_col=0)
    y_train = dataframe.target.values
    X_train = dataframe.drop(['target'], axis=1).values
    model.fit(X_train, y_train)

    save_object_pkl(model, model_path)

def save_object_pkl(obj, path: str) -> NoReturn:
    """ Save pickle object """

    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, 'model.pkl'), 'wb', encoding='utf-8') as handler:
        pickle.dump(obj, handler)


if __name__ == "__main__":
    train_model()
