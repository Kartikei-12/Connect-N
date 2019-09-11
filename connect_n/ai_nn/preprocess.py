"""Data preprocessing for neural network trainning"""

# Python module(s)
import numpy as np

from ..env import ROWS, COLUMNS


class Preprocess:
    """Pre-processing class for dataset

    Args:
        dataset (str): PATH to datset(in .npy format)

    Raises:
        TypeError: when incorrect path to dataset file is provided."""

    def __init__(self, dataset=""):
        """Instantiate method"""
        if not isinstance(dataset, str) or not dataset.endswith(".npy"):
            raise TypeError(
                "Name of dataset(with path) in .npy format need to be provided"
            )
        self.X, self.y = None, None
        self.dataset_name = dataset
        self.dataset = np.load(dataset, allow_pickle=True)

    def fit(self):
        """Fit method for data preprocessing"""
        X, y = list(), list()
        new_dataset = list()
        encode = {
            0: np.array([0, 0, 0], dtype=int),
            1: np.array([0, 1, 0], dtype=int),
            2: np.array([0, 0, 2], dtype=int),
        }
        min_game_len = min(i.shape[0] for i in self.dataset)
        for game in self.dataset:
            new_game = list()
            for frame in game:
                new_frame = list()
                for row in frame:
                    new_row = list()
                    for ele in row:
                        new_row.append(encode[int(ele)])
                    new_frame.append(np.array(new_row))
                new_game.append(np.array(new_frame))
            new_dataset.append(np.array(new_game))
        self.dataset = np.array(new_dataset)
        for game in self.dataset:
            for i in range(min_game_len, game.shape[0]):
                X.append(game[i - min_game_len : i]), y.append(game[i])
        self.X, self.y = np.array(X), np.array(y)

    def transform(self):
        """Provides seprated and properly encoded X, y from dataset

        Returns:
            numpy.ndarray : X
            numpy.ndarray : y"""
        return self.X, self.y

    def __str__(self):
        """str method"""
        return "<class Preprocess: {}>".format(self.dataset_name)
