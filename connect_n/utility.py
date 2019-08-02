"""Utility methods for project."""

import sys
from loguru import logger

def getVersion(file):
    """Method

    Args:
        file (str): File path(usually to the file version.txt)

    Returns:
        Version after reading from given file"""
    try:
        with open(file, "r") as f:
            return f.read()
            f.close()
    except FileNotFoundError:
        return ""


def recordGame(game):
    """Simple method to record games using loguru module by https://pypi.org/project/loguru/

    Args:
        game (ConnectNGame): Game object"""
    format_ = "<green>{time:DD-MM-YYYY at HH:mm:ss}</green>: <level>{message}</level>"
    record = """\nWinner: {winner}
        Players: {players}
        Game Sequence: {sequence}\n\n"""

    logger.add(
        "reports/GameRecords.log", colorize=False, rotation="50 MB", format=format_
    )
    logger.add(sys.stdout, colorize=True, format=format_)
    logger.info(
        record, winner=game.winner, players=game.players, sequence=game.sequence
    )


def dummy_method(*args, **kwargs):
    """Dummy method which does nothing
    Note: Accepts anything and everything"""
    pass
