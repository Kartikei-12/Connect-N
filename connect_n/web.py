"""Utility class for web interface."""

# Python module(s)
import math
from env import ROWS, COLUMNS

# Colours
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
COLOR = {"RED": (255, 0, 0), "YELLOW": (255, 255, 0), "GREEN": (0, 255, 0)}
C_LIST = [BLACK, COLOR["RED"], COLOR["YELLOW"], COLOR["GREEN"]]

# Some constants
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)


class WebUtility:
    """Utility class for web interface

    Args:
        r (int): Rows of game
        c (int): Columns of game
    """

    def __init__(self, r=ROWS, c=COLUMNS):
        """Instantiate Method"""
        self.num_col = c
        self.num_rows = r
        self.width = c * SQUARESIZE
        self.height = (r + 1) * SQUARESIZE
        print(math.__name__)
        """"
        try:
            self.screen = pygame.display.set_mode((self.width, self.height))
        except pygame.error as e:  # Expected inside docker.
            print(e, "\nSwitching to command line.")
            raise EnvironmentError("Vedio device not found.")
        pygame.display.update()
        """

    def update(self):
        """Update Screen"""
        # pygame.display.update()
        pass

    def draw_black_rec(self):
        """Draw empty rectangles."""
        # pygame.draw.rect(self.screen, BLACK, (0, 0, self.width, SQUARESIZE))
        pass

    def draw_player_coin(self, p_id, event):
        """Draw player coin

        Args:
            p_id (int): Player ID
            event (pygame.event): Event of motion of coin.
        """
        # pygame.draw.circle(
        #     self.screen, C_LIST[p_id], (event.pos[0], int(SQUARESIZE / 2)), RADIUS
        # )
        pass

    def get_col(self, event):
        """Column in which coin was droped.

        Args:
            event (pygame.event): Event of dropiung of coin.

        Returns:
            int : Column in ehich coin is droped"""
        # return int(math.floor(event.pos[0] / SQUARESIZE))
        pass

    def blit(self, msg, p_id):
        """Finising game.

        Args:
            msg (str): Message to display
            p_id (int): Winnig player p_id"""
        # size = int((self.num_rows * SQUARESIZE * 1.5) / len(msg))
        # label = pygame.font.SysFont("monospace", size).render(msg, 1, C_LIST[p_id])
        # self.screen.blit(label, (40, 10))
        pass

    def wait(self):
        """Wait mthod for pygame."""
        # pygame.time.wait(3000)
        pass

    def get_event(self):
        """Get list of events."""
        # return pygame.event.get()
        pass

    def is_quit_event(self, event):
        """Checks QUIT event

        Args:
            event (pygame.event): Event."""
        # return event.type == pygame.QUIT
        pass

    def is_mouse_motion(self, event):
        """Checks MOUSE MOTION event

        Args:
            event (pygame.event): Event."""
        # return event.type == pygame.MOUSEMOTION
        pass

    def is_mouse_down(self, event):
        """Checks MOUSE CLICK event

        Args:
            event (pygame.event): Event."""
        # return event.type == pygame.MOUSEBUTTONDOWN
        pass

    def draw(self, board):
        """Draw basic board for the game.

        Args:
            board (numpy.ndarray): 2-D numpy array representing the board"""
        # self.screen.fill(BLUE, (0, SQUARESIZE, self.width, self.height))
        # for c in range(self.num_col):
        #     for r in range(self.num_rows):
        #         pygame.draw.circle(
        #             self.screen,
        #             C_LIST[board[r][c]],
        #             (
        #                 int(c * SQUARESIZE + SQUARESIZE / 2),
        #                 self.height - int(r * SQUARESIZE + SQUARESIZE / 2),
        #             ),
        #             RADIUS,
        #         )
        # pygame.display.update()
        pass
