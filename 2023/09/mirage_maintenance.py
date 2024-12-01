from pprint import pprint


def get_difference(history: list[int]) -> list[int]:
    differences = []
    for i in range(1, len(history)):
        differences.append(history[i] - history[i - 1])
    return differences


def sum_of_extrapolated_values(data: str) -> int:
    sum_of_extrapolated_values = 0
    lines = data.splitlines()
    histories = []
    for line in lines:
        histories.append([int(number) for number in line.split(" ")])

    for history in histories:
        differences = [history, get_difference(history)]
        while differences[-1].count(0) != len(differences[-1]):
            differences.append(get_difference(differences[-1]))
        pprint(differences)

        current_value = 0
        for i in range(len(differences) - 1, 0, -1):
            current_value = current_value + differences[i - 1][-1]
        sum_of_extrapolated_values += current_value

    return sum_of_extrapolated_values


def sum_of_extrapolated_values_back(data: str) -> int:
    sum_of_extrapolated_values = 0
    lines = data.splitlines()
    histories = []
    for line in lines:
        histories.append([int(number) for number in line.split(" ")])

    for history in histories:
        differences = [history, get_difference(history)]
        while differences[-1].count(0) != len(differences[-1]):
            differences.append(get_difference(differences[-1]))
        pprint(differences)

        current_value = 0
        for i in range(len(differences) - 1, 0, -1):
            current_value = differences[i - 1][0] - current_value
        sum_of_extrapolated_values += current_value

    return sum_of_extrapolated_values


if __name__ == "__main__":
    with open("test_input") as f:
        test_input = f.read().strip()

    with open("my_test_input") as f:
        my_test_input = f.read().strip()

    with open("input") as f:
        input = f.read().strip()

    # print("Result:", sum_of_extrapolated_values(test_input))
    # print("Result:", sum_of_extrapolated_values(input))
    print("Result:", sum_of_extrapolated_values_back(input))
