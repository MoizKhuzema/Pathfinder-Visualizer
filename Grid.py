"""
class implementation of grid
"""
import pygame
import numpy as np
from Node import Node, ColorPalette as Clr


class Grid:
    def __init__(self, total_rows, window_width):
        self.rows = total_rows
        self.gap = window_width // total_rows
        self.grid = np.empty(shape=[total_rows, total_rows], dtype=Node)
        for i in range(total_rows):
            for j in range(total_rows):
                self.grid[i, j] = Node(i, j, self.gap, total_rows)

    def reset_grid(self):
        for row in self.grid:
            for node in row:
                node.reset()

    def render_gridlines(self, window, window_width):
        """
        renders grey lines separating and highlighting each node
        :param window:
        :param window_width:
        :return: void
        """
        for i in range(self.rows):
            pygame.draw.line(window, Clr['GREY'], (0, i * self.gap), (window_width, i * self.gap))
            for j in range(self.rows):
                pygame.draw.line(window, Clr['GREY'], (j * self.gap, 0), (j * self.gap, window_width))

    def render_grid(self, window, window_width):
        """
        renders the grid, gridlines and each node
        :param window:
        :param window_width:
        :return:
        """
        for row in self.grid:
            for node in row:
                node.draw(window)

        self.render_gridlines(window, window_width)
