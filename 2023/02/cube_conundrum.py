import re


def possible_games_for_cube_configuration(data: str, max_cube_configuration: {str: int}) -> int:
    sum = 0
    lines = data.split('\n')
    for line in lines:
        line = line.strip()
        game_id = int(re.match(r"Game (\d+)", line).group(1))
        cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        line = line.split(":")[1].strip()

        pattern = re.compile(r"(\d+) (red|green|blue)")
        for cube in pattern.findall(line):
            cube_count = int(cube[0])
            cube_color = cube[1]
            if cubes[cube_color] < cube_count:
                cubes[cube_color] = cube_count

        if (cubes["red"] <= max_cube_configuration["red"]) and (cubes["green"] <= max_cube_configuration["green"]) and (
                cubes["blue"] <= max_cube_configuration["blue"]):
            sum += game_id

    return sum


def the_other_task(data: str) -> int:
    sum = 0
    lines = data.split('\n')
    for line in lines:
        line = line.strip()
        cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        line = line.split(":")[1].strip()

        pattern = re.compile(r"(\d+) (red|green|blue)")
        for cube in pattern.findall(line):
            cube_count = int(cube[0])
            cube_color = cube[1]
            if cubes[cube_color] < cube_count:
                cubes[cube_color] = cube_count

        sum += cubes["red"] * cubes["green"] * cubes["blue"]
    return sum


if __name__ == "__main__":
    with open("test_input") as f:
        test_input = f.read().strip()

    with open("input") as f:
        input = f.read().strip()

    print(possible_games_for_cube_configuration(test_input, {"red": 12, "green": 13, "blue": 14}))
    print(possible_games_for_cube_configuration(input, {"red": 12, "green": 13, "blue": 14}))

    print(the_other_task(test_input))
    print(the_other_task(input))
