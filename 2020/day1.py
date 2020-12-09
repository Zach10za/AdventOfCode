"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation
at a nice resort on a tropical island. Surely, Christmas will go on without
you.

The tropical island has its own currency and is entirely cash-only. The gold
coins used there have a little picture of a starfish; the locals just call
them stars. None of the currency exchanges seem to have heard of them, but
somehow, you'll need to find fifty of these coins by the time you arrive so
you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each
day in the Advent calendar; the second puzzle is unlocked when you complete
the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense
report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then
multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying
them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum
to 2020; what do you get if you multiply them together?
"""

ENTRIES = [
    1078, 1109, 1702, 1293, 1541, 1422, 1679, 1891, 1898, 1455, 1540, 1205,
    1971, 1582, 1139, 1438, 1457, 1725, 1907, 1872, 1101, 1403, 1557, 1597,
    1619, 1974, 1287, 292, 1647, 1444, 1241, 879, 1761, 1067, 1178, 1510,
    1110, 1233, 1121, 1299, 1796, 1124, 1768, 1466, 1871, 1279, 1344, 1485,
    1258, 1179, 1147, 492, 1234, 1843, 1421, 1819, 1964, 1671, 1793, 1302,
    1731, 1886, 1686, 1150, 1806, 1960, 1841, 1936, 1845, 1520, 1779, 1102,
    1323, 1892, 1742, 1941, 1395, 1525, 1165, 715, 1829, 1448, 1906, 1191,
    1981, 1115, 1716, 1644, 1310, 1836, 1105, 1517, 1790, 1950, 1741, 1256,
    1467, 1677, 1372, 1838, 1637, 1143, 1763, 1222, 1291, 1835, 1602, 1927,
    1933, 1952, 1692, 1662, 1967, 1791, 1984, 1176, 1324, 1460, 1416, 562,
    1862, 1273, 1518, 1535, 1093, 1977, 1923, 1246, 1570, 1674, 1861, 1811,
    1431, 47, 1158, 1912, 1322, 1062, 1407, 1528, 1068, 1868, 1997, 1930,
    959, 1676, 1759, 2000, 1993, 1722, 1738, 1264, 1361, 1542, 1187, 1735,
    1405, 1745, 1753, 1833, 1493, 1311, 1547, 1180, 1553, 1513, 1812, 1951,
    1948, 1834, 1925, 1726, 1326, 1931, 1962, 1947, 1173, 1633, 1901, 1781,
    1483, 1789, 1417, 1929, 1859, 1760, 1347, 1996, 1328, 1798, 1230, 1298,
    1877, 1840, 1607, 1253, 1057, 1650, 1171, 1593,
]

result = None

for e1 in ENTRIES:
    for e2 in ENTRIES[::-1]:
        if e1 == e2:
            break
        if e1 + e2 == 2020:
            result = e1 * e2
            break

print(f'Part one: {result}')  # 751776

"""
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers
you a starfish coin they had left over from a past vacation. They offer you
a second one if you can find three numbers in your expense report that meet
the same criteria.

Using the above example again, the three entries that sum to 2020 are 979,
366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to
2020?
"""
result = None

for e1 in ENTRIES:
    for e2 in ENTRIES[::-1]:
        if e1 == e2:
            break
        for e3 in ENTRIES[::-1]:
            if e2 == e3:
                break
            if e1 + e2 + e3 == 2020:
                result = e1 * e2 * e3
                break

print(f'Part two: {result}')  # 42275090
