import re
from pprint import pprint


def get_points_from_scratchcards(data: str) -> int:
    total_sum = 0
    for line in data.splitlines():
        pattern = re.compile(r"Card +(\d+): +((?:\d+ *)+) \| +((?:\d+ *)+)")
        match = pattern.match(line)

        winning_numbers = [int(number) for number in re.split(" +", match.group(2))]
        numbers_you_have = [int(number) for number in re.split(" +", match.group(3))]
        points = 2 ** (sum(number in winning_numbers for number in numbers_you_have) - 1)
        total_sum += points if points >= 1 else 0

    return total_sum


def get_points_from_scratchcards_v2(cards: list[str], index: int = 1, cache=None) -> int:
    if cache is None:
        cache = {0: 0}

    sum_of_scratchcards = 0

    pattern = re.compile(r"Card +(\d+): +((?:\d+ *)+) \| +((?:\d+ *)+)")
    match = pattern.match(cards[index - 1])

    if index in cache:
        next_cards = cache.get(index)
        sum_of_scratchcards += cache.get(index)
    else:
        winning_numbers = [int(number) for number in re.split(" +", match.group(2))]
        numbers_you_have = [int(number) for number in re.split(" +", match.group(3))]
        next_cards = sum(number in winning_numbers for number in numbers_you_have)
        cache[index] = next_cards

        sum_of_scratchcards += next_cards + 1
        sum_of_scratchcards += get_points_from_scratchcards_v2(cards, index + 1, cache) if index < len(cards) else 0

    for i in range(1, next_cards + 1):
        sum_of_scratchcards += get_points_from_scratchcards_v2(cards, index + i, cache) if index + i < len(cards) else 0

    return sum_of_scratchcards


if __name__ == "__main__":
    with open("test_input") as f:
        test_input = f.read().strip()

    with open("input") as f:
        input = f.read().strip()

    print(get_points_from_scratchcards(test_input))
    print(get_points_from_scratchcards(input))

    print("Result:", get_points_from_scratchcards_v2(test_input.splitlines()))
    print("Result:", get_points_from_scratchcards_v2(input.splitlines()))
