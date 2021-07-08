# -*- coding: utf-8 -*-


class Node:
    def __init__(self, parent, position) -> None:
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def new_position(self, movment):
        return (self.position[0] + movment[0], self.position[1] + movment[1])

    def __eq__(self, other):
        return self.position == other.position


class Maze:
    def __init__(self, maze_map):
        self.maze_map = maze_map

    def __contains__(self, position):
        return (position[0] >= 0 and position[0] <= len(self.maze_map) - 1
                and position[1] >= 0 and position[1] <=
                (len(self.maze_map[len(self.maze_map) - 1]) - 1))

    def is_reachable(self, position):
        return self.maze_map[position[0]][position[1]] == 0


def path(node):
    res = []
    cur = node
    while cur:
        res.append(cur.position)
        cur = cur.parent
    return res[::-1]


def astar(maze, start, end):
    movements = [(0, -1), (0, 1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, -1),
                 (-1, 1)]
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    close_list = []

    open_list.append(start_node)

    while open_list:
        cur_node = open_list[0]
        cur_idx = 0
        for idx, node in enumerate(open_list):
            if node.f < cur_node.f:
                cur_node = node
                cur_idx = idx

        open_list.pop(cur_idx)
        close_list.append(cur_node)

        if cur_node == end_node:
            return path(cur_node)

        children = []
        for movement in movements:
            new_position = cur_node.new_position(movement)
            if new_position not in maze:
                continue

            if not maze.is_reachable(new_position):
                continue

            new_node = Node(cur_node, new_position)
            children.append(new_node)

        for child in children:
            if [
                    close_child for close_child in close_list
                    if close_child == child
            ]:
                continue

            child.g = cur_node.g + 1
            child.h = pow(child.position[0] - end_node.position[0], 2) + \
                pow(child.position[1] - end_node.position[1], 2)
            child.f = child.g + child.h

            if [
                    open_node for open_node in open_list
                    if child == open_node and child.g > open_node.g
            ]:
                continue

            open_list.append(child)


def main():
    maze_map = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    maze = Maze(maze_map)

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)


if __name__ == "__main__":
    main()
