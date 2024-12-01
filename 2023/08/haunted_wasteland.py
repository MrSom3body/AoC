from math import lcm
import re
from pprint import pprint


def get_shortest_path(data: str) -> int:
    steps = []
    path = data.splitlines()[0].replace("L", "0").replace("R", "1")
    network = {}
    current = "AAA"
    pattern = re.compile(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)")
    for match in pattern.finditer(data):
        network[match.group(1)] = (match.group(2), match.group(3))

    index = 0
    path_length = len(path)
    while current != "ZZZ":
        direction = int(path[index % path_length])
        current = network.get(current)[direction]
        index += 1
        steps.append(direction)

    print(current)
    pprint(network)
    print(path)

    return len(steps)


def get_shortest_path_2(data: str) -> int:
    path = data.splitlines()[0].replace("L", "0").replace("R", "1")
    steps = []
    network = {}
    pattern = re.compile(r"(.{3}) = \((.{3}), (.{3})\)")
    for match in pattern.finditer(data):
        network[match.group(1)] = (match.group(2), match.group(3))

    path_length = len(path)
    nodes_with_a = list(filter(lambda node: node[-1] == "A", list(network.keys())))
    for node in nodes_with_a:
        index = 0
        while node[-1] != "Z":
            direction = int(path[index % path_length])
            node = network.get(node)[direction]
            index += 1
        steps.append(index)

    return lcm(*steps)


if __name__ == "__main__":
    with open("test_input_1") as f:
        test_input1 = f.read().strip()
    with open("test_input_2") as f:
        test_input2 = f.read().strip()

    with open("input") as f:
        input = f.read().strip()

    # print(get_shortest_path(test_input_1))
    # print(get_shortest_path(input))
    print(get_shortest_path_2(test_input2))
    print(get_shortest_path_2(input))
