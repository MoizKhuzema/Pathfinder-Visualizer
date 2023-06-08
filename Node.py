"""
class implementation of individual nodes in grid
"""
import pygame

# colors used for visualization
ColorPalette = {
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'YELLOW': (255, 255, 0),
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'PURPLE': (128, 0, 128),
    'ORANGE': (255, 165, 0),
    'GREY': (128, 128, 128),
    'TURQUOISE': (64, 224, 208)
}


class Node:
    def __init__(self, row, col, node_width, total_rows):
        self.row = row
        self.col = col
        self.x = row * node_width
        self.y = col * node_width
        self.color = ColorPalette['BLACK']
        self.neighbors = []
        self.node_width = node_width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == ColorPalette['RED']

    def is_open(self):
        return self.color == ColorPalette['GREEN']

    def is_barrier(self):
        return self.color == ColorPalette['WHITE']

    def is_start(self):
        return self.color == ColorPalette['ORANGE']

    def is_end(self):
        return self.color == ColorPalette['TURQUOISE']

    def reset(self):
        self.color = ColorPalette['BLACK']

    def make_start(self):
        self.color = ColorPalette['ORANGE']

    def make_closed(self):
        self.color = ColorPalette['RED']

    def make_open(self):
        self.color = ColorPalette['GREEN']

    def make_barrier(self):
        self.color = ColorPalette['WHITE']

    def make_end(self):
        self.color = ColorPalette['TURQUOISE']

    def make_path(self):
        self.color = ColorPalette['PURPLE']

    def draw(self, window):
        """
        draws the node on the window at coordinates x,y
        :param window:
        :return: void
        """
        pygame.draw.rect(window, self.color, (self.x, self.y, self.node_width, self.node_width))

    def update_neighbors(self, grid):
        """
        updates the list of legal possible adjacent nodes to *this
        :param grid:
        :return: void
        """
        self.neighbors = []
        # if *this is not in the last row and the node below is not a barrier, add it in neighbours
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        # if *this is not in the first row and the node above is not a barrier, add it in neighbours
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        # if *this is not in the last column and the node to the right is not a barrier, add it in neighbours
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        # if *this is not in the first column and the node to the left is not a barrier, add it in neighbours
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
