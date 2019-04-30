"""Utility class for pygame

Note:
    In this files pylint configured to ignore 'no member' because of C implementation of several pygame members like constants MOUSEBUTTONDOWN and methods like init()"""

# Python module(s)
import math
import pygame
import random

# Environment Variables
from env import ROWS, COLUMNS

# Disabling pylint because of implementation of pygame in C
# pylint: disable=no-member

# Colours
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
COLOR = {"RED": (255, 0, 0), "YELLOW": (255, 255, 0), "GREEN": (0, 255, 0)}

C_LIST = list(value for key, value in COLOR.items())
C_LIST.insert(0, BLACK)

# Some constants
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)


class PygameUtility:
    """Utility class for pygame module

    Note:
        Docker does nor support pygame will automatically switch to command line.

    Args:
        r (int): Rows of game
        c (int): Columns of game
    """

    def __init__(self, r=ROWS, c=COLUMNS):
        """Instantiate Method"""
        pygame.init()
        self.num_col = c
        self.num_rows = r
        self.width = c * SQUARESIZE
        self.height = (r + 1) * SQUARESIZE
        try:
            self.screen = pygame.display.set_mode((self.width, self.height))
        except pygame.error as e:  # Expected inside docker.
            print(e, "\nSwitching to command line.")
            raise EnvironmentError("Vedio device not found.")
        pygame.display.update()

    def draw_black_rec(self):
        """Draw empty rectangles."""
        pygame.draw.rect(self.screen, BLACK, (0, 0, self.width, SQUARESIZE))

    def draw_player_coin(self, p_id, event):
        """Draw player coin

        Args:
            p_id (int): Player ID
            event (pygame.event): Event of motion of coin.
        """
        pygame.draw.circle(
            self.screen, C_LIST[p_id], (event.pos[0], int(SQUARESIZE / 2)), RADIUS
        )

    def blit(self, msg, p_id):
        """Finising game.

        Args:
            msg (str): Message to display
            p_id (int): Winnig player p_id"""
        size = int((self.num_rows * SQUARESIZE * 1.5) / len(msg))
        label = pygame.font.SysFont("monospace", size).render(msg, 1, C_LIST[p_id])
        self.screen.blit(label, (40, 10))

    def draw(self, board):
        """Draw basic board for the game.

        Args:
            board (numpy.ndarray): 2-D numpy array representing the board"""
        self.screen.fill(BLUE, (0, SQUARESIZE, self.width, self.height))
        for c in range(self.num_col):
            for r in range(self.num_rows):
                pygame.draw.circle(
                    self.screen,
                    C_LIST[board[r][c]],
                    (
                        int(c * SQUARESIZE + SQUARESIZE / 2),
                        self.height - int(r * SQUARESIZE + SQUARESIZE / 2),
                    ),
                    RADIUS,
                )
        pygame.display.update()

    def play(self, board, players, is_valid_move, make_move, is_winning_move):
        """Method to play the game in GUI using pygame

        Args:
            board (numpy.ndarray): Game board
            players (list): List of players
            is_valid_move (function): Move validator
            make_move (function): Makes move
            is_winning_move (function): Ckeck for winning move"""
        turn = random.randint(0, len(players) - 1)
        while True:
            col = -1
            self.draw(board)
            if players[turn].name == "AI":
                col = players[turn].get_move()
                pygame.time.wait(500)
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return None
                    if event.type == pygame.MOUSEMOTION:
                        self.draw_black_rec()
                        self.draw_player_coin(players[turn].p_id, event)
                    pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.draw_black_rec()
                        col = int(math.floor(event.pos[0] / SQUARESIZE))
            if is_valid_move(col):
                row = make_move(col, players[turn].p_id)
                if is_winning_move(row, col):
                    self.blit(
                        " {} Wins!!".format(players[turn].name), players[turn].p_id
                    )
                    self.draw(board)
                    pygame.time.wait(3000)
                    return players[turn]
                turn = (turn + 1) % len(players)
            elif players[turn].name == "AI":  # AI makes an invalid move
                return None
