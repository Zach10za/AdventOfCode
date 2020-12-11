import re
from math import factorial
from helpers import get_file_lines

DAY = 10

input_path = f'data/day{DAY}_test.txt'
input_path = f'data/day{DAY}.txt'


def part1():
    diffs = []
    lines = get_file_lines(input_path)
    adapters = sorted(map(int, lines))
    joltage = 0
    for adapter in adapters:
        diffs.append(adapter - joltage)
        joltage = adapter

    diffs.append(3)
    ones = len([a for a in diffs if a == 1])
    threes = len([a for a in diffs if a == 3])
    print(ones, threes)
    return ones * threes

    raise Exception('No answer found')


def part2():
    lines = get_file_lines(input_path)
    adapters = sorted(map(int, lines))
    diffs = []
    joltage = 0
    for adapter in adapters:
        diffs.append(adapter - joltage)
        joltage = adapter
    diffs.append(3)

    total = 1
    cur_ones_group_length = 0
    for diff in diffs:
        if cur_ones_group_length > 0 and diff == 3:
            total *= get_permutations(cur_ones_group_length)
            cur_ones_group_length = 0
        elif diff == 1:
            cur_ones_group_length += 1

    return total

    raise Exception('No answer found')


def get_permutations(count):
    if count < 2:
        return 1
    elif count < 3:
        return 2
    else:
        return (
            get_permutations(count - 1)
            + get_permutations(count - 2)
            + get_permutations(count - 3)
        )

def run():
    # print(part1())
    print(part2())
