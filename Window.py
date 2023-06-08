"""
class implementation of renderer for application window
"""
import pygame
from Grid import Grid
from Node import ColorPalette as Clr


class Window:
    def __init__(self, window_width, total_rows):
        self.window = pygame.display.set_mode((window_width, window_width))
        self.width = window_width
        pygame.display.set_caption("Visualization of Search Algorithms")
        self.grid = Grid(total_rows, window_width)

    def render_window(self):
        """
        renders the window, and calls render functions for grid and nodes
        :return: void
        """
        self.window.fill(Clr['WHITE'])
        self.grid.render_grid(self.window, self.width)
        pygame.display.update()

    def get_clicked_pos(self, pos):
        """
        returns position of mouse click translated to rows and columns
        :param pos:
        :return:
        """
        y, x = pos
        row = y // self.grid.gap
        col = x // self.grid.gap

        return row, col
