"""
Utility class for pygame.
"""
import math
import pygame
from default_variables import *

BLUE = (0,0,255)
BLACK = (0,0,0)
COLOR = {
    "RED": (255,0,0),
    "YELLOW": (255,255,0),
    "GREEN": (0,255,0)
}

C_LIST = [BLACK, COLOR['RED'], COLOR['YELLOW'], COLOR['GREEN']]
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)

class PygameUtility:
    """Utility class for pygame module

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
        self.height = (r+1) * SQUARESIZE
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.update()

    def update(self):
        """Update Screen"""
        pygame.display.update()

    def draw_blue_rec_board(self):
        """Draw empty board."""
        self.screen.fill(
            BLUE, (
                0, SQUARESIZE,
                self.width, self.height
            )
        )

    def draw_moves(self, board):
        """Draw moves made by players
        Args:
            board (numpy.ndarray): Playing board
        """
        for c in range(self.num_col):
            for r in range(self.num_rows):
                pygame.draw.circle(
                    self.screen,
                    C_LIST[int(board[r][c])],
                    (
                        int(c*SQUARESIZE+SQUARESIZE/2),
                        self.height-int(r*SQUARESIZE+SQUARESIZE/2)
                    ), RADIUS
                )

    def draw_black_rec(self):
        """Draw empty rectangles."""
        pygame.draw.rect(self.screen, BLACK, (0,0, self.width, SQUARESIZE))

    def draw_player_coin(self, id, event):
        """Draw player coin
        Args:
            id (int): Player ID
            event (pygame.event): Event of motion of coin.
        """
        pygame.draw.circle(
            self.screen,
            C_LIST[id],
            (
                event.pos[0],
                int(SQUARESIZE/2)
            ), RADIUS
        )

    def get_col(self, event):
        """Column in which coin was droped.
        Args:
            event (pygame.event): Event of dropiung of coin.
        Returns:
            int : Column in ehich coin is droped"""
        return int(math.floor(event.pos[0]/SQUARESIZE))

    def blit(self, msg, id):
        """Finising game.
        Args:
            msg (str): Message to display
            id (int): Winnig player id
        """
        size = int((self.num_rows*SQUARESIZE*1.5)/len(msg))
        label = pygame.font.SysFont("monospace", size).render(
            msg,
            1, C_LIST[id]
        )
        self.screen.blit(label, (40,10))
    
    def wait(self):
        """Wait mthod for pygame."""
        pygame.time.wait(3000)

    def get_event(self):
        """Get list of events."""
        return pygame.event.get()

    def is_quit_event(self, event):
        """Checks QUIT event
        Args:
            event (pygame.event): Event.
        """
        return event.type == pygame.QUIT

    def is_mouse_motion(self, event):
        """Checks MOUSE MOTION event
        Args:
            event (pygame.event): Event.
        """
        return event.type == pygame.MOUSEMOTION

    def is_mouse_down(self, event):
        """Checks MOUSE CLICK event
        Args:
            event (pygame.event): Event.
        """
        return event.type == pygame.MOUSEBUTTONDOWN

    def quit(self):
        pygame.quit()
