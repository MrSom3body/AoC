import re


def engine_schematic(data: str) -> int:
    sum = 0
    lines = data.splitlines()
    for line_number, line in enumerate(lines):
        for number in re.finditer(r"\d+", line):
            adjacent_to_symbol = False
            for character_index in range(number.span()[0], number.span()[1]):
                for adjacent_character in range(9):
                    character = ""

                    try:
                        if adjacent_character == 0:
                            character = lines[line_number - 1][character_index - 1]
                        elif adjacent_character == 1:
                            character = lines[line_number - 1][character_index]
                        elif adjacent_character == 2:
                            character = lines[line_number - 1][character_index + 1]
                        elif adjacent_character == 3:
                            character = lines[line_number][character_index - 1]
                        elif adjacent_character == 4:
                            character = lines[line_number][character_index]
                        elif adjacent_character == 5:
                            character = lines[line_number][character_index + 1]
                        elif adjacent_character == 6:
                            character = lines[line_number + 1][character_index - 1]
                        elif adjacent_character == 7:
                            character = lines[line_number + 1][character_index]
                        elif adjacent_character == 8:
                            character = lines[line_number + 1][character_index + 1]
                    except IndexError:
                        pass

                    if re.match(r"[^.\d]", character) and not adjacent_to_symbol:
                        adjacent_to_symbol = True
                        sum += int(number.group())
                        break

    return sum


def engine_schematic_with_cogs(data: str) -> int:
    sum = 0
    lines = data.splitlines()

    for line_number, line in enumerate(lines):
        for cog in re.finditer(r"\*", line):
            cog_index = cog.span()[0]
            numbers = []

            for adjacent_character in range(9):
                character = ""
                number_character = []

                try:
                    if adjacent_character == 0:
                        character = lines[line_number - 1][cog_index - 1]
                        number_character = [line_number - 1, cog_index - 1]
                    elif adjacent_character == 1:
                        character = lines[line_number - 1][cog_index]
                        number_character = [line_number - 1, cog_index]
                    elif adjacent_character == 2:
                        character = lines[line_number - 1][cog_index + 1]
                        number_character = [line_number - 1, cog_index + 1]
                    elif adjacent_character == 3:
                        character = lines[line_number][cog_index - 1]
                        number_character = [line_number, cog_index - 1]
                    elif adjacent_character == 4:
                        character = lines[line_number][cog_index]
                        number_character = [line_number, cog_index]
                    elif adjacent_character == 5:
                        character = lines[line_number][cog_index + 1]
                        number_character = [line_number, cog_index + 1]
                    elif adjacent_character == 6:
                        character = lines[line_number + 1][cog_index - 1]
                        number_character = [line_number + 1, cog_index - 1]
                    elif adjacent_character == 7:
                        character = lines[line_number + 1][cog_index]
                        number_character = [line_number + 1, cog_index]
                    elif adjacent_character == 8:
                        character = lines[line_number + 1][cog_index + 1]
                        number_character = [line_number + 1, cog_index + 1]
                except IndexError:
                    pass

                if character.isdigit() and len(numbers) < 2:
                    line_with_number = lines[number_character[0]]
                    for number in re.finditer(r"\d+", line_with_number):
                        if number.span()[0] <= number_character[1] < number.span()[1] and int(
                                number.group()) not in numbers:
                            numbers.append(int(number.group()))

            if len(numbers) == 2:
                sum += numbers[0] * numbers[1]

    return sum


if __name__ == '__main__':
    with open("test_input") as f:
        test_input = f.read().strip()

    with open("input") as f:
        input = f.read().strip()

    print(engine_schematic(test_input))
    # print(engine_schematic(input))
    print(engine_schematic_with_cogs(test_input))
    print(engine_schematic_with_cogs(input))
