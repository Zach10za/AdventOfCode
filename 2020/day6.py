
with open('data/day6.txt') as f:
    lines = f.readlines()
    
groups = []
group = None
for line in lines:
    print(line)
    if line == '\n':
        groups.append(group)
        print(group)
        print('*'*80)
        group = None
        continue
    line_set = set(line.strip())
    if group is None:
        group = line_set
        continue
    print(group, line_set, group.intersection(line_set))
    group = group.intersection(line_set)
    
total = 0
for group in groups:
    total += len(group)
    # print(group, len(group), total)
    
print(total)
