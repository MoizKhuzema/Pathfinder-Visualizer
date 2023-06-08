import pygame
from queue import PriorityQueue


def heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstructt_path(came_from, draw):
    for current in came_from:
        current.make_path()
        draw()


def bfs(draw, start, end):
    visited, stack = [], [(start, [start])]
    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        vertex, path = stack.pop(0)

        if vertex not in visited:
            visited.append(vertex)
            for child in set(vertex.neighbors) - set(visited):
                if child == end:
                    reconstructt_path([child] + path, draw)
                    end.make_end()
                    return True
                else:
                    stack.append((child, [child] + path))
                    child.make_open()

            draw()
            if vertex != start:
                vertex.make_closed()

    return False


def dfs(draw, start, end):
    visited, stack = [], [(start, [start])]
    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        vertex, path = stack.pop()

        if vertex not in visited:
            visited.append(vertex)
            for child in set(vertex.neighbors) - set(visited):
                if child == end:
                    reconstruct_path([child] + path, draw)
                    end.make_end()
                    return True
                else:
                    stack.append((child, [child] + path))
                    child.make_open()

            draw()
            if vertex != start:
                vertex.make_closed()

    return False


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def a_star(draw, grid, start, end):
    count = 0
    queue = PriorityQueue()
    queue.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = heuristic(start.get_pos(), end.get_pos())

    visited = {start}

    while not queue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = queue.get()[2]
        visited.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor.get_pos(), end.get_pos())
                if neighbor not in visited:
                    count += 1
                    queue.put((f_score[neighbor], count, neighbor))
                    visited.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False
