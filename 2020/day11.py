import re
import time
from copy import deepcopy
from os import system
from typing import List

from helpers import get_file_lines

DAY = 11

# input_path = f'data/day{DAY}_test.txt'
input_path = f'data/day{DAY}.txt'


def count_occupied_seats(grid):
    occupied_seats = 0
    for col in grid:
        for cell in col:
            if cell == '#':
                occupied_seats += 1
    return occupied_seats


def print_grid(grid):
    time.sleep(.08)
    system('clear')
    # print('*' * len(grid[0]) * 2)
    print('\n'.join([' '.join(row) for row in grid]))
    # print('*' * len(grid[0]) * 2)


def get_occupied_adj_count1(x: int, y: int, grid: List[List[str]]):
    directions = [
        [-1, -1], [0, -1], [1, -1],
        [-1,  0],          [1,  0],
        [-1,  1], [0,  1], [1,  1],
    ]

    num_occupied = 0
    for d in directions:
        cy = y + d[0]
        cx = x + d[1]
        if (
                0 <= cy <= len(grid) - 1
                and 0 <= cx <= len(grid[0]) - 1
                and grid[cy][cx] == '#'
        ):
            num_occupied += 1
    return num_occupied


def part1():
    lines = get_file_lines(input_path)
    grid = [list(l) for l in lines]
    prev_grid = []
    while str(grid) != str(prev_grid): 
        prev_grid = deepcopy(grid)
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                seat = prev_grid[y][x]
                if seat == '.':
                    continue
                elif seat == 'L' and get_occupied_adj_count1(x, y, prev_grid) == 0:
                    grid[y][x] = '#'
                elif seat == '#' and get_occupied_adj_count1(x, y, prev_grid) >= 4:
                    grid[y][x] = 'L'
        print_grid(grid)
    return count_occupied_seats(grid)


def get_occupied_adj_count2(x: int, y: int, grid: List[List[str]]):
    directions = [
        [-1, -1], [0, -1], [1, -1],
        [-1,  0],          [1,  0],
        [-1,  1], [0,  1], [1,  1],
    ]

    num_occupied = 0
    for d in directions:
        cy = y + d[0]
        cx = x + d[1]
        while 0 <= cy <= len(grid) - 1 and 0 <= cx <= len(grid[0]) - 1:
            if grid[cy][cx] == '#':
                num_occupied += 1
                break
            elif grid[cy][cx] == 'L':
                break
            cy += d[0]
            cx += d[1]
    return num_occupied


def part2():
    lines = get_file_lines(input_path)
    grid = [list(l) for l in lines]
    prev_grid = []
    while str(grid) != str(prev_grid): 
        prev_grid = deepcopy(grid)
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                seat = prev_grid[y][x]
                if seat == '.':
                    continue
                elif seat == 'L' and get_occupied_adj_count2(x, y, prev_grid) == 0:
                    grid[y][x] = '#'
                elif seat == '#' and get_occupied_adj_count2(x, y, prev_grid) >= 5:
                    grid[y][x] = 'L'
        print_grid(grid)
    return count_occupied_seats(grid)


def run():
    print(part1())
    # print(part2())
