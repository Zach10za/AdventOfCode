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

    # GOAL = 127
    GOAL = 542529149

    # Old solution
    # end = 1
    # for start in range(len(lines)):
    #     while sum(lines[start:end]) < GOAL:
    #         end += 1
    #     if sum(lines[start:end]) == GOAL:
    #         found = lines[start:end]
    #         return min(found) + max(found)

    # Better solution
    start, end = 0, 0
    while (total := sum(lines[start:end])) != GOAL:
        if total < GOAL:
            end += 1
        else:
            start += 1

    return min(lines[start:end]) + max(lines[start:end])


def run():
    print(part1())  # 542529149
    print(part2())  # 75678618
