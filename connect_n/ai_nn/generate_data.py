"""generate_data.py file, generates dataset for Deep Learning model, AI agent."""

# Python module(s)
import os
import random
import numpy as np

# Environment Variable(s)
from ..env import N, ROWS, COLUMNS

# Project Module(s)
from ..ai import AI
from ..player import Player
from ..connect_n import ConnectNGame


class GenerateData:
    """Generate Data class used to generate train data(in .npy format) for AI agent

    Args:
        out_dir (str): Output directory for training datast.
        file_name (str):
            File name for training dataset,
            (do not include extention in file name),
            extention .npy is automatically added
        game_runs (int): Number of game runs for training dataset.

    Raises:
        TypeError: When non-string type are passed for out_dir and file_name
        TypeError: When non-int type is passed for game_runs"""

    def __init__(
        self,
        out_dir="/dataset",
        file_name="dl_train_dataset",
        game_runs=10,
        n=N,
        num_rows=ROWS,
        num_cols=COLUMNS,
    ):
        if not isinstance(out_dir, str) or not isinstance(file_name, str):
            raise TypeError(
                "Type 'string' accepted for out_dir and file_name arguments, type {} and {} encountered".format(
                    type(out_dir), type(file_name)
                )
            )
        if not isinstance(game_runs, int):
            raise TypeError(
                "Type 'int' accepted for out_dir argument, type {} encountered".format(
                    type(game_runs)
                )
            )
        self.n = n
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.game_runs = abs(game_runs)
        if not os.path.isdir(os.getcwd() + out_dir):
            os.mkdir(os.getcwd() + out_dir)
        self.out_file = os.getcwd() + "/" + out_dir + "/" + file_name + ".npy"

    def generate_save(self, want_return=False):
        """Generates dataset for Deep Learning Model trainning

        Args:
            want_return (bool): Returns generated dataset as numpy.ndarray if true

        Returns:
            numpy.ndarray : Generated dataset"""
        if self.game_runs == 0:
            raise MemoryError(
                "Dataset already generated, use another object for new dataset"
            )
        count = -1
        game_runs = self.game_runs
        dataset = list()
        game = ConnectNGame(ai=True, graphic=False)
        game.players.append(AI(game, 2))
        while game_runs:
            count += 1
            if count > (2 * self.game_runs):
                break
            winner = None
            board_states = [game.board]
            turn = random.getrandbits(1)
            game.reset()
            while not winner:
                if len(game.get_valid_moves()) == 0:
                    break
                turn = (turn + 1) % len(game.players)
                if random.getrandbits(1):
                    col = random.choice(game.get_valid_moves())
                elif random.getrandbits(1):
                    col = game.players[turn].get_move()
                else:
                    col = game.players[turn].greedy()
                row = game.make_move(col, turn + 1)
                board_states.append(game.board)
                if game.is_winning_move(row, col):
                    winner = "AI" if game.players[turn].p_id == 1 else "Not AI"
                    break
            if winner != "AI":
                continue
            game_runs -= 1
            dataset.append(np.array(board_states))
        np.save(self.out_file, np.array(dataset), allow_pickle=True)
        if want_return:
            return np.array(dataset)

    def load(self):
        """Loads generated dataset"""
        return np.load(self.out_file, allow_pickle=True)

    def __str__(self):
        """String representation of class object"""
        return "<class Generate Data>"
