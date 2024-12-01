import re


def calibration(data):
    lines = data.split("\n")
    numbers = [re.findall("\\d", line) for line in lines]
    return sum(int(number[0] + number[-1]) for number in numbers)


if __name__ == "__main__":
    with open("input") as f:
        data = f.read().strip()

    # Part 1
    print(calibration(data))

    # Part 2
    data = (
        data.replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "f4r")
        .replace("five", "f5e")
        .replace("six", "s6x")
        .replace("seven", "s7n")
        .replace("eight", "e8t")
        .replace("nine", "n9e")
    )
    print(calibration(data))
