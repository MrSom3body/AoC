import re


def get_distance(hold_down: int, time: int):
    distance = (time - hold_down) * hold_down
    return distance


def get_possible_solutions(data: str) -> int:
    sum = 1
    lines = data.splitlines()
    pattern = re.compile(r"(Time|Distance): +((?:\d+ *)+)")
    times = [int(number) for number in re.split(r" +", pattern.match(lines[0]).group(2))]
    distances = [int(number) for number in re.split(r" +", pattern.match(lines[1]).group(2))]
    times = [int(re.sub(r" +", "", pattern.match(lines[0]).group(2)))]
    distances = [int(re.sub(r" +", "", pattern.match(lines[1]).group(2)))]
    print(times, distances)

    for index, time in enumerate(times):
        solutions = []
        for i in range(time):
            distance = get_distance(i, time)
            if distance > distances[index]:
                solutions.append(distance)
        sum *= len(solutions)
    return sum


if __name__ == "__main__":
    with open("test_input") as f:
        test_input = f.read().strip()

    with open("input") as f:
        input = f.read().strip()

    print(get_possible_solutions(test_input))
    print(get_possible_solutions(input))
