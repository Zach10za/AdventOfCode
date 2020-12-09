
"""
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.) # 211
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""

trees_r1_d1 = 0
trees_r3_d1 = 0
trees_r5_d1 = 0
trees_r7_d1 = 0
trees_r1_d2 = 0

with open('data/day2.txt') as f:
    lines = f.readlines()
    h_index_r1_d1 = 0
    h_index_r3_d1 = 0
    h_index_r5_d1 = 0
    h_index_r7_d1 = 0
    h_index_r1_d2 = 0

    for v_index, line in enumerate(lines):
        line = line.strip()
        if line[h_index_r1_d1] == '#':
            trees_r1_d1 += 1
        h_index_r1_d1 += 1
        if h_index_r1_d1 >= len(line):
            h_index_r1_d1 = h_index_r1_d1 - len(line)

        if line[h_index_r3_d1] == '#':
            trees_r3_d1 += 1
        h_index_r3_d1 += 3
        if h_index_r3_d1 >= len(line):
            h_index_r3_d1 = h_index_r3_d1 - len(line)

        if line[h_index_r5_d1] == '#':
            trees_r5_d1 += 1
        h_index_r5_d1 += 5
        if h_index_r5_d1 >= len(line):
            h_index_r5_d1 = h_index_r5_d1 - len(line)

        if line[h_index_r7_d1] == '#':
            trees_r7_d1 += 1
        h_index_r7_d1 += 7
        if h_index_r7_d1 >= len(line):
            h_index_r7_d1 = h_index_r7_d1 - len(line)

        if v_index % 2 == 0:
            if line[h_index_r1_d2] == '#':
                trees_r1_d2 += 1
            h_index_r1_d2 += 1
            if h_index_r1_d2 >= len(line):
                h_index_r1_d2 = h_index_r1_d2 - len(line)

print(trees_r1_d1)
print(trees_r3_d1)
print(trees_r5_d1)
print(trees_r7_d1)
print(trees_r1_d2)

print(trees_r1_d1 * trees_r3_d1 * trees_r5_d1 * trees_r7_d1 * trees_r1_d2)
