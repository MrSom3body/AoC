from collections import Counter

cards1 = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")
cards2 = ("J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A")


def task1(data: str) -> int:
    sum = 0
    hands = data.splitlines()
    hands.sort(key=card_sort)
    hands.sort(key=get_type)

    for index, hand in enumerate(hands):
        bid = int(hand.split(" ")[1])
        multiplier = index + 1

        sum += bid * multiplier

    return sum


def card_sort(hand: str) -> list[int]:
    return [cards1.index(card) for card in hand.split(" ")[0]]


def get_type(hand: str) -> int:
    hand = list(hand.split(" ")[0])
    counter = Counter(hand)
    values = list(counter.values())
    if len(counter) == 1:
        return 5
    elif len(counter) == 2 and 4 in values:
        return 4
    elif len(counter) == 2 and 3 in values:
        return 3
    elif len(counter) == 3 and 3 in values:
        return 2
    elif len(counter) == 3 and values.count(2) == 2:
        return 1
    elif len(counter) == 4:
        return 0
    return -1


def task2(data: str) -> int:
    sum = 0
    hands = data.splitlines()
    hands.sort(key=card_sort2)
    hands.sort(key=get_type2)

    for index, hand in enumerate(hands):
        bid = int(hand.split(" ")[1])
        multiplier = index + 1

        sum += bid * multiplier

    return sum


def card_sort2(hand: str) -> list[int]:
    return [cards2.index(card) for card in hand.split(" ")[0]]


def get_type2(hand: str) -> int:
    hand = list(hand.split(" ")[0])
    counter = Counter(hand)

    if "J" in counter and len(counter) > 1:
        j = counter.pop("J")
        most_common_char = counter.most_common(1)[0][0]
        counter[most_common_char] += j

    values = list(counter.values())
    if len(counter) == 1:
        return 5
    elif len(counter) == 2 and 4 in values:
        return 4
    elif len(counter) == 2 and 3 in values:
        return 3
    elif len(counter) == 3 and 3 in values:
        return 2
    elif len(counter) == 3 and values.count(2) == 2:
        return 1
    elif len(counter) == 4:
        return 0
    return -1


if __name__ == "__main__":
    with open("test_input") as f:
        test_input = f.read().strip()

    with open("input") as f:
        input = f.read().strip()

    print(task2(test_input))
    print(task2(input))  # print(task1(input))
