from helpers import get_file_lines

path = 'data/day8.txt'
lines = get_file_lines(path)

accumulator, index = 0, 0
index_hit = []
while index < len(lines):
    if index in index_hit:
        raise Exception(f'Infinite loop detected: line: {index}, acc: {accumulator}')  # Part 1
        # index = index_hit[-1] + 1  # Part 2
    index_hit.append(index)
    action, value = lines[index].split(' ')
    index += int(value) if action == 'jmp' else 1
    accumulator += int(value) if action == 'acc' else 0

print(accumulator)
