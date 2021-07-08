import heapq


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

    def __repr__(self):
        return f"<Node {self.position} g:{self.g} h:{self.h} f:{self.f}>"


class PriorityQueue:
    def __init__(self):
        self._container = []
        self._index = 0

    def put(self, prority, item):
        heapq.heappush(self._container, (prority, self._index, item))
        self._index += 1

    def get(self):
        return heapq.heappop(self._container)[-1]

    def is_empty(self):
        if self._container:
            return False
        else:
            return True

    def __iter__(self):
        self.gen = iter(self._container)
        return self

    def __next__(self):
        return next(self.gen)[-1]


class Maze:
    def __init__(self, maze_map):
        self.maze_map = maze_map

    def __contains__(self, position):
        return (0 <= position[0] <= (len(self.maze_map) - 1)
                and 0 <= position[1] <=
                (len(self.maze_map[len(self.maze_map) - 1]) - 1))

    def is_reachable(self, position):
        return self.maze_map[position[0]][position[1]] == 0


def heuristic_cost_estimate(from_position, to_position):
    return (pow(from_position[0] - to_position[0], 2) +
            pow(from_position[1] - to_position[1], 2))


def path(node):
    res = []
    cur = node
    while cur:
        res.append(cur.position)
        cur = cur.parent
    return res[::-1]


def astar(maze, start, end):
    movements = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = PriorityQueue()
    close_list = []

    open_list.put(start_node.f, start_node)

    while not open_list.is_empty():
        cur_node = open_list.get()
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
            child.h = heuristic_cost_estimate(child.position,
                                              end_node.position)
            child.f = child.g + child.h

            if [
                    open_node for open_node in open_list
                    if child == open_node and child.g > open_node.g
            ]:
                continue

            open_list.put(child.f, child)


def main():
    # s = input()
    # rows, cols = [int(x) for x in s.split()]
    maze_map = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1],
                [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
    # for _ in range(rows):
    #     line = input()
    #     maze_map.append([int(x) for x in line.split()])

    maze = Maze(maze_map)
    start = (0, 0)
    end = (4, 4)
    path = astar(maze, start, end)

    for node in path:
        print(node)


if __name__ == "__main__":
    main()
