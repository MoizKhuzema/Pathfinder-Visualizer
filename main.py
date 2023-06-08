import pygame
from Window import Window
from algorithm import bfs
from algorithm import dfs
from algorithm import a_star


WIDTH = 650
ROWS = 50


def main():
    """
    implements an engine loop that runs the processes every event
    :return: void
    """
    window = Window(WIDTH, ROWS)

    start = None
    end = None
    run = True

    while run:
        window.render_window()
        for event in pygame.event.get():
            # if user clicks exit button
            if event.type == pygame.QUIT:
                run = False

            # if user clicks left mouse button
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = window.get_clicked_pos(pos)
                node = window.grid.grid[row, col]
                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()

            # if user clicks right mouse button
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = window.get_clicked_pos(pos)
                node = window.grid.grid[row, col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                # if user presses key space, start visualization
                if event.key == pygame.K_SPACE and start and end:
                    for row in window.grid.grid:
                        for node in row:
                            node.update_neighbors(window.grid.grid)

                    # bfs(lambda: window.render_window(), start, end)
                    #dfs(lambda: window.render_window(), start, end)
                    a_star(lambda: window.render_window(), window.grid.grid, start, end)

                # if user presses key c, reset visualization
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    window.grid.reset_grid()

    pygame.quit()


main()
