import resource
import sys

from sympy import Point2D

resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x10000000)


def get_furthest_point_from_animal(data: str) -> tuple[int, list[str]]:
    lines = data.splitlines()
    path = build_path(lines)
    # print(path)
    furthest_point = int(len(path) / 2)
    return furthest_point, path


def build_path(pipe_map: list[str], path: list[str] = None, position: tuple[int, int] = None, direction: int = None,
               pipe: str = None) -> list[str]:
    if not position:
        grid = []
        path = []
        for index, line in enumerate(pipe_map):
            if "S" in line:
                position = (index, line.index("S"))
                break
        direction, pipe = find_first_pipe(pipe_map, position)
    else:
        direction, pipe = find_next_pipe(pipe_map, position, direction, pipe)

    if len(path) > 0 and pipe_map[position[0]][position[1]] == "S":
        return path

    path.append(pipe)
    if direction == 0:
        position = (position[0] - 1, position[1])
    elif direction == 1:
        position = (position[0], position[1] + 1)
    elif direction == 2:
        position = (position[0] + 1, position[1])
    elif direction == 3:
        position = (position[0], position[1] - 1)

    return build_path(pipe_map, path, position, direction)


def find_first_pipe(pipe_map: list[str], position: tuple[int, int]):
    for i in range(4):
        if i == 0 and pipe_map[position[0] - 1][position[1]] in ("F", "|", "7"):
            return 0, pipe_map[position[0] - 1][position[1]]
        elif i == 1 and pipe_map[position[0]][position[1] + 1] in ("7", "-", "J"):
            return 1, pipe_map[position[0]][position[1] + 1]
        elif i == 2 and pipe_map[position[0] + 1][position[1]] in ("J", "|", "L"):
            return 2, pipe_map[position[0] + 1][position[1]]
        elif i == 3 and pipe_map[position[0]][position[1] - 1] in ("L", "-", "F"):
            return 3, pipe_map[position[0]][position[1] - 1]


def find_next_pipe(pipe_map: list[str], position: tuple[int, int], old_direction: int) -> (int, str):
    up = {
        "F": 1,
        "|": 0,
        "7": 3
    }
    right = {
        "7": 2,
        "-": 1,
        "J": 0
    }
    down = {
        "J": 3,
        "|": 2,
        "L": 1
    }
    left = {
        "L": 0,
        "-": 3,
        "F": 2
    }

    if old_direction == 0:
        char = pipe_map[position[0]][position[1]]
        return up.get(char), char
    elif old_direction == 1:
        char = pipe_map[position[0]][position[1]]
        return right.get(char), char
    elif old_direction == 2:
        char = pipe_map[position[0]][position[1]]
        return down.get(char), char
    elif old_direction == 3:
        char = pipe_map[position[0]][position[1]]
        return left.get(char), char


def find_first_pipe_iterative(pipe_map: list[str], position: Point2D):
    for i in range(4):
        if i == 0 and pipe_map[position.y - 1][position.x] in "F|7":
            return Point2D(position.x, position.y - 1)
        elif i == 1 and pipe_map[position.y][position.x + 1] in "7-J":
            return Point2D(position.x + 1, position.y)
        elif i == 2 and pipe_map[position.y + 1][position.x] in "J|L":
            return Point2D(position.x, position.y + 1)
        elif i == 3 and pipe_map[position.y][position.x - 1] in "LF":
            return Point2D(position.x - 1, position.y)


def find_next_pipe_iterative(pipe_map: list[str], position: Point2D, last_position: Point2D) -> Point2D:
    pass


def build_path_iterative(pipe_map: list[str]) -> list[(int, int)]:
    path = []
    for index, line in enumerate(pipe_map):
        if "S" in line:
            path.append(Point2D(line.index("S"), index))
            break

    position = find_first_pipe_iterative(pipe_map, path[0])

    while pipe_map[position.y][position.x] != "S":
        path.append(position)
        position = find_next_pipe_iterative(pipe_map, position, path[len(path) - 1])

    print(path)
    return path


def count_tiles_in_pipe(data: str) -> int:
    count = 0
    lines = data.splitlines()
    path = build_path_iterative(lines)
    var = (path[1][0] - path[-1][0], path[1][1] - path[-1][1])
    if var == (1, 0):
        data.replace("S", "F")
    elif var == (-1, 0):
        data.replace("S", "J")
    elif var == (0, 1):
        data.replace("S", "L")
    elif var == (0, -1):
        data.replace("S", "7")

    print(var)

    for y, line in enumerate(lines):
        in_pipe = False
        for x, char in enumerate(line):
            if (x, y) in path:
                print(char, end="")
                if char in "|F7":
                    in_pipe = not in_pipe
            else:
                if in_pipe and char != "S":
                    count += 1
                    print("X", end="")
                else:
                    print(char, end="")
        print()

    return count


if __name__ == "__main__":
    with open("test_input1") as f:
        test_input1 = f.read().strip()

    with open("test_input2") as f:
        test_input2 = f.read().strip()

    with open("test_input3") as f:
        test_input3 = f.read().strip()

    with open("input") as f:
        input = f.read().strip()

    print(get_furthest_point_from_animal(test_input1))
    # print(build_path_iterative(test_input1.splitlines()))
    # print(count_tiles_in_pipe(test_input1))
    # print(get_furthest_point_from_animal(test_input2))
    # print(count_tiles_in_pipe(test_input3))
    # print(count_tiles_in_pipe(input))
