import re

EXPECTED_FIELDS = {
    'byr': lambda v: v.isdigit() and 1920 <= int(v) <= 2002,
    'iyr': lambda v: v.isdigit() and 2010 <= int(v) <= 2020,
    'eyr': lambda v: v.isdigit() and 2020 <= int(v) <= 2030,
    'hgt': lambda v: v[:-2].isdigit() and ((v[-2:] == 'cm' and 150 <= int(v[:-2]) <= 193) or (v[-2:] == 'in' and 59 <= int(v[:-2]) <= 76)),
    'hcl': lambda v: re.match(r'^#[a-f0-9]{6}$', v),
    'ecl': lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda v: v.isdigit() and len(v) == 9,
    # 'cid',
}

passports = []

with open('data/day4.txt') as f:
    lines = f.readlines()
    passport = {}
    for line in lines:
        if line == '\n':
            passports.append(passport)
            passport = {}
            continue
            
        pieces = line.split(' ')
        for piece in pieces:
            if piece:
                kvs = piece.split(':')
                if kvs[0] != 'cid':
                    passport[kvs[0]] = kvs[1].replace('\n', '')
                    
    if passport:
        passports.append(passport)

def check_expected_fields(p):
    for e, fn in EXPECTED_FIELDS.items():
        if e not in p:
            return False
        elif not fn(p[e]):
            return False
    return True

valids = 0
for p in passports:
    if check_expected_fields(p):
        valids += 1

print(valids)
    
