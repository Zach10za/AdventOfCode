
with open('data/day5.txt') as f:
    lines = f.readlines()
    
seat_ids = []

def process_line(line):
    print(line)
    row_end = 128
    row_start = 0
    row = -1
    for index, char in enumerate(line[:7]):
        print(char, row_start, row_end)
        if char == 'B':
            row_start += (row_end - row_start) / 2
            if index == 6:
                row = row_end - 1
        elif char == 'F':
            row_end -= (row_end - row_start) / 2
            if index == 6:
                row = row_start
                
    col_end = 8
    col_start = 0
    col = -1
    for index, char in enumerate(line[7:]):
        print(char, col_start, col_end)
        if char == 'R':
            col_start += (col_end - col_start) / 2
            if index == 2:
                col = col_end - 1
        elif char == 'L':
            col_end -= (col_end - col_start) / 2
            if index == 2:
                col = col_start

    seat_ids.append(row * 8 + col)    
        

for line in lines:
    process_line(line.strip())

for id in range(127 * 8):
    if id > 1:
        if id not in seat_ids and id - 1 in seat_ids and id + 1 in seat_ids:
            print(f'SEAT: {id}')            
