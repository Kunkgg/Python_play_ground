import copy


class Node:
    movements = [(1, 0), (0, 1)]

    def __init__(self, parent, position) -> None:
        self.parent = parent
        self.position = position

    def new_position(self, movement):
        return (self.position[0] + movement[0], self.position[1] + movement[1])

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return f"<Node {self.position}>"


class Maze:
    def __init__(self, maze_map):
        self.maze_map = copy.deepcopy(maze_map)

    def __contains__(self, position):
        return (0 <= position[0] <= (len(self.maze_map) - 1)
                and 0 <= position[1] <=
                (len(self.maze_map[len(self.maze_map) - 1]) - 1))

    def is_reachable(self, position):
        return self.__contains__(position) and self.maze_map[position[0]][
            position[1]] == 0

    def set(self, position, value):
        self.maze_map[position[0]][position[1]] = value

    def get(self, position):
        return self.maze_map[position[0]][position[1]]

    def get_neighs(self, position):
        neighs = []
        for movement in Node.movements:
            new_position = (position[0] + movement[0],
                            position[1] + movement[1])
            if self.__contains__(new_position):
                neighs.append(new_position)
        return neighs

    def path(self, node):
        res = []
        cur = node
        while cur:
            res.append(cur.position)
            cur = cur.parent
        return res[::-1]

    def copy(self):
        return copy.deepcopy(self.maze_map)

    def get_size(self):
        return (len(self.maze_map), len(self.maze_map[len(self.maze_map) - 1]))

    def get_rows(self):
        return len(self.maze_map)

    def get_cols(self):
        return len(self.maze_map[len(self.maze_map) - 1])

    def __repr__(self):
        return ("=" * 20 + "\n" + "\n".join(map(str, self.maze_map)))


def travel_dfs(maze, start_node, end_node, tryall=False):
    if start_node.position not in maze or end_node.position not in maze:
        raise ValueError("start or node position in over the range of maze.")

    maze.set(start_node.position, 2)

    if not tryall:
        print(maze)

    if start_node == end_node:
        maze.set(start_node.position, 2)
        return start_node

    for movement in Node.movements:
        new_position = start_node.new_position(movement)
        new_node = Node(start_node, new_position)
        if maze.is_reachable(new_position):
            if tryall:
                travel_dfs(maze, new_node, end_node, tryall=True)
            else:
                return travel_dfs(maze, new_node, end_node)


def is_trap(position, maze_tryall, path):
    if maze_tryall.get(position) != 2:
        return False
    neighs = maze_tryall.get_neighs(position)
    if position in path or any([neigh in path for neigh in neighs]):
        return False
    # if all([maze_tryall.get(neigh) != 1 for neigh in neighs]):
    #     return False
    return True


def trap_count(maze_tryall, path):
    counter = 0
    for row in range(maze_tryall.get_rows()):
        for col in range(maze_tryall.get_cols()):
            if is_trap((row, col), maze_tryall, path):
                counter += 1

    return counter


def unreach_count(maze_tryall):
    tmp = []
    for row in maze_tryall.maze_map:
        tmp.extend(row)
    return tmp.count(0)


def main():
    # s = input()
    # rows, cols = [int(x) for x in s.split()]
    # maze_map = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1],
    #             [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
    # maze_map = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
    maze_map = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    maze_map = [
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0],
    ]
    # for _ in range(rows):
    #     line = input()
    #     maze_map.append([int(x) for x in line.split()])

    maze = Maze(maze_map)
    maze_tryall = Maze(maze_map)

    start = (0, 0)
    end = (3, 5)
    start_node = Node(None, start)
    end_node = Node(None, end)
    node = travel_dfs(maze, start_node, end_node)
    path = maze.path(node)
    travel_dfs(maze_tryall, start_node, end_node, tryall=True)

    print("=" * 20)
    print("path:")
    print(path)
    print("=" * 20)
    print("maze tryall:")
    print(maze_tryall)

    print("=" * 20)
    print("maze tryall:")
    print("=" * 20)
    print("trap unreach:")
    print(f"{trap_count(maze_tryall, path)} {unreach_count(maze_tryall)}")


if __name__ == "__main__":
    main()
