"""Tests for dataset generation class"""

# Python module(s)
import os
import unittest
import numpy as np

# User module(s)
from env import ROWS, COLUMNS

# Project module(s)
from connect_n.ai_rnn.generate_data import GenerateData


class GenerateDataTests(unittest.TestCase):
    """Tests for dataset generation class"""

    def setUp(self):
        """setUp"""
        self.gd = GenerateData(
            out_dir="/test_directory", file_name="test_file", game_runs=1
        )

    def tearDown(self):
        """tearDown"""
        try:
            os.remove(self.gd.out_file)
            os.rmdir(os.getcwd() + "/test_directory")
            del self.gd
            del self.dataset
        except:
            pass

    def test_generate_save(self):
        """Testing generation method"""
        dataset = self.gd.generate_save(want_return=True)
        self.assertEqual(dataset.shape[0], 1)
        self.assertEqual(dataset.shape[2], ROWS)
        self.assertEqual(dataset.shape[3], COLUMNS)

    def test_load(self):
        """Testing load method"""
        dataset = self.gd.generate_save(want_return=True)
        loaded_dataset = self.gd.load()
        np.testing.assert_array_equal(
            dataset, loaded_dataset, err_msg="load method failed"
        )
