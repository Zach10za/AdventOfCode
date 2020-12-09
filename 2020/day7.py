import re

with open('data/day7.txt') as f:
    lines = f.readlines()
    
bags = {}
    
for line in lines:
    matches = re.match(
        r'^([a-z\s]+) bags contain (\d+) ([a-z\s]+) bags?(, (\d+) ([a-z]+\s[a-z]+) bags?)?(, (\d+) ([a-z]+\s[a-z]+) bags?)?(, (\d+) ([a-z]+\s[a-z]+) bags?)?.$',
        line.strip(),
    )
    
    if matches is not None:
        color = matches.group(1)
        contains1 = {
            'count': int(matches.group(2)),
            'color': matches.group(3),
        }
        
        bags[color] = [contains1]

        if matches.group(5):
            bags[color].append({
                'count': int(matches.group(5)),
                'color': matches.group(6),
            })

        if matches.group(8):
            bags[color].append({
                'count': int(matches.group(8)),
                'color': matches.group(9),
            })

        if matches.group(11):
            bags[color].append({
                'count': int(matches.group(11)),
                'color': matches.group(12),
            })
            
    else:
        matches = re.match(r'([a-z\s]+) bags contain no other bags.', line.strip())
        color = matches.group(1)
        bags[color] = []


def get_bags_inside(current_bags: list, layer = 0):
    running_total = 0

    for bag in current_bags:
        if bag['color'] not in bags:
            print(f"{'----'* layer} Found {bag['count']} {bag['color']} bags with {bag['count']} bags inside 0")
            running_total += bag['count']
        elif len(bags[bag['color']]) == 0:
            print(f"{'----'* layer} Found {bag['count']} {bag['color']} bags with 0 bags inside 1")
            running_total += bag['count']
        else:
            num_bags_inside = get_bags_inside(bags[bag['color']], layer + 1)
            print(f"{'----'* layer} Found {bag['count']} {bag['color']} bags with {num_bags_inside} bags inside 2")
            running_total += bag['count'] + (bag['count'] * num_bags_inside)
        print(f"{'----'* layer} Running total: {running_total}")
    return running_total


color = 'shiny gold'
total_bags = get_bags_inside(bags[color])
print(total_bags)

    
