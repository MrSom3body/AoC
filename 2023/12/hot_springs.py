import itertools
import re


def get_arrangements(line: str) -> int:
    count = 0
    print(line)
    springs = line.split(" ")[0]
    damaged_springs = [int(n) for n in line.split(" ")[1].split(",")]
    number_of_damaged_springs = sum(damaged_springs)

    pattern_str = ""
    spring_list = []

    pattern_str = pattern_str.replace("+", "*", 1)

    pattern = re.compile(pattern_str)

    return count


if __name__ == "__main__":
    with open("data") as f:
        data = f.read().strip()

    with open("data1") as f:
        data1 = f.read().strip()

    get_arrangements(data1.splitlines()[0])
