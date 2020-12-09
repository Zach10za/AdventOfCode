import re
from helpers import get_file_lines

DAY = 9

# input_path = f'data/day{DAY}_test.txt'
input_path = f'data/day{DAY}.txt'


def is_sum_of_two(number, preamble):
    for i, x in enumerate(preamble):
        for y in preamble[i+1:]:
            if x + y == number:
                return True
    return False


def part1():
    lines = get_file_lines(input_path)
    lines = map(int, lines)

    # PREAMBLE_SIZE = 5
    PREAMBLE_SIZE = 25
    preamble = []
    for index, line in enumerate(lines):
        if index < PREAMBLE_SIZE:
            preamble.append(line)
        elif is_sum_of_two(line, preamble):
            preamble.append(line)
            preamble.pop(0)
        else:
            return line

    raise Exception('No answer found')


def part2():
    lines = get_file_lines(input_path)
    lines = list(map(int, lines))

    # TOTAL = 127
    TOTAL = 542529149
    end = 1
    for start in range(len(lines)):
        while sum(lines[start:end]) < TOTAL:
            end += 1
        if sum(lines[start:end]) == TOTAL:
            found = lines[start:end]
            return min(found) + max(found)

    raise Exception('No answer found')


def run():
    print(part1())  # 542529149
    print(part2())  # 75678618
