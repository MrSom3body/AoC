import re
import time


def get_lowest_location(data: str) -> int:
    numbers = [int(number) for number in re.match(r"seeds: ((?:\d+ ?)+)", data).group(1).split(" ")]
    pattern = re.compile(r"^(\d+ ?)+", re.RegexFlag.MULTILINE)

    for line in data.split("\n\n"):
        map_lines = []
        for match in pattern.finditer(line):
            map_lines.append([int(number) for number in match.group().split(" ")])
        numbers = nums_to_next_map(numbers, map_lines)
    return min(numbers)


def nums_to_next_map(numbers: list[int], new_map: list[list[int]]) -> list[int]:
    new_numbers = numbers.copy()

    for line in new_map:
        destination_range_start = line[0]
        source_range_start = line[1]
        range_length = line[2]
        for index, number in enumerate(numbers):
            if source_range_start <= number < source_range_start + range_length:
                new_numbers[index] = number + destination_range_start - source_range_start

    return new_numbers


def get_lowest_location_with_ranges_v2(data: str) -> int:
    pass


def get_lowest_location_with_ranges(data: str) -> int:
    numbers = [int(number) for number in re.match(r"seeds: ((?:\d+ ?)+)", data).group(1).split(" ")]
    additional_numbers = []
    for index, number in enumerate(numbers):
        if index % 2 == 1:
            for i in range(number):
                additional_numbers.append(numbers[index - 1] + i)

    numbers = additional_numbers
    end = time.time()
    print(end - start)

    pattern = re.compile(r"^(\d+ ?)+", re.RegexFlag.MULTILINE)

    for line in data.split("\n\n"):
        map_lines = []
        for match in pattern.finditer(line):
            map_lines.append([int(number) for number in match.group().split(" ")])
        numbers = nums_to_next_map(numbers, map_lines)
    return min(numbers)


if __name__ == "__main__":
    with open("test_input") as f:
        test_input = f.read().strip()

    with open("luka_input") as f:
        luka_input = f.read().strip()

    with open("input") as f:
        input = f.read().strip()

    # print(get_lowest_location(test_input_1))
    # print(get_lowest_location(input))

    start = time.time()
    print(get_lowest_location_with_ranges(input))
    # print(get_lowest_location_with_ranges_v2(input))
    end = time.time()

    print(f"It took {end - start} seconds")
