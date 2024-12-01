def print_2d_list(to_print: list[list[str]]) -> None:
    for row in to_print:
        for col in row:
            print(col, end="")
        print()
    print()


def cosmic_expansion_v1(data):
    counter = 0
    lines = data.splitlines()
    grid = []

    for line in lines:
        grid.append([char for char in line])

    galaxy_positions = []

    to_dupe_row = []
    for index, line in (enumerate(grid)):
        if "#" not in line:
            to_dupe_row.append(index)

    for index, line in reversed(list(enumerate(to_dupe_row))):
        grid.insert(line, ["X" for _ in range(len(grid[0]))])

    grid = list(zip(*grid[::-1]))

    to_dupe_col = []
    for index, line in (enumerate(grid)):
        if "#" not in line:
            to_dupe_col.append(index)

    for index, line in reversed(list(enumerate(to_dupe_col))):
        grid.insert(line, ["X" for _ in range(len(grid[0]))])

    grid = list(zip(*grid))[::-1]

    # print_2d_list(grid)

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "#":
                galaxy_positions.append((x, y))

    # print(galaxy_positions)

    for i, position1 in enumerate(galaxy_positions):
        for position2 in galaxy_positions[i + 1:]:
            x_diff = abs(position1[0] - position2[0])
            y_diff = abs(position1[1] - position2[1])
            print(position1, position2, x_diff + y_diff)

            # print(x_diff+y_diff)
            counter += x_diff + y_diff

    return int(counter)


def cosmic_expansion_v2(data: str, expansion: int):
    counter = 0
    lines = data.splitlines()
    grid = []

    for line in lines:
        grid.append([char for char in line])

    galaxy_positions = []

    empty_rows = []
    for index, line in (enumerate(grid)):
        if "#" not in line:
            empty_rows.append(index)

    grid = list(zip(*grid[::-1]))

    empty_cols = []
    for index, line in (enumerate(grid)):
        if "#" not in line:
            empty_cols.append(index)

    grid = list(zip(*grid))[::-1]

    # print_2d_list(grid)

    number_of_y_expansions = 0
    number_of_x_expansions = 0
    for y, line in enumerate(grid):
        new_y = y
        for row in empty_rows:
            if y > row:
                number_of_y_expansions += 1
                new_y += expansion * number_of_y_expansions

        for x, char in enumerate(line):
            new_x = x
            for col in empty_cols:
                if x > col:
                    number_of_x_expansions += 1
                    new_x += expansion * number_of_x_expansions
            if char == "#":
                galaxy_positions.append((new_x, new_y))

    # print(galaxy_positions)

    for i, position1 in enumerate(galaxy_positions):
        position1 = list(position1)
        for position2 in galaxy_positions[i + 1:]:
            position2 = list(position2)

            # print(position1, position2)
            x_diff = abs(position1[0] - position2[0])
            y_diff = abs(position1[1] - position2[1])
            # print(x_diff + y_diff)
            counter += x_diff + y_diff

    return int(counter)


def cosmic_expansion(data: str, expansion: int):
    counter = 0
    lines = data.splitlines()
    grid = []

    for line in lines:
        grid.append([char for char in line])

    galaxy_positions = []

    to_dupe_row = []
    for index, line in (enumerate(grid)):
        if "#" not in line:
            to_dupe_row.append(index)

    for index in reversed(to_dupe_row):
        grid.insert(index, ["X" for _ in range(len(grid[0]))])

    grid = list(zip(*grid[::-1]))

    to_dupe_col = []
    for index, line in (enumerate(grid)):
        if "#" not in line:
            to_dupe_col.append(index)

    for index in reversed(to_dupe_col):
        grid.insert(index + 1, ["X" for _ in range(len(grid[0]))])

    grid = list(zip(*grid))[::-1]

    print_2d_list(grid)

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "#":
                galaxy_positions.append((x, y))

    for index, galaxy in enumerate(galaxy_positions):
        galaxy_x = galaxy[0]
        galaxy_y = galaxy[1]
        new_y, new_x = 0, 0
        for y in range(galaxy_y):
            if grid[y][galaxy_x] == "X":
                new_y += expansion
            else:
                new_y += 1

        for x in range(galaxy_x):
            if grid[galaxy_y][x] == "X":
                new_x += expansion
            else:
                new_x += 1

        galaxy_positions[index] = [new_x, new_y]

    # print(galaxy_positions)

    for i, position1 in enumerate(galaxy_positions):
        for position2 in galaxy_positions[i + 1:]:
            x_diff = abs(position1[0] - position2[0])
            y_diff = abs(position1[1] - position2[1])
            print(position1, position2, x_diff + y_diff)

            # print(x_diff+y_diff)
            counter += x_diff + y_diff

    return counter


if __name__ == "__main__":
    with open("data1") as f:
        data1 = f.read().strip()

    with open("my_data1") as f:
        my_data1 = f.read().strip()

    with open("data") as f:
        data = f.read().strip()

    print("Part 1:", cosmic_expansion_v1(data1))
    print("Part 2:", cosmic_expansion(data, 999_999))
