from aocd import data

rows = data.splitlines()
cols = ["".join(c) for c in zip(*rows)]
h2 = len(rows) // 2
n = "".join("10"[c.count("1") >= h2] for c in cols)
𝛾 = int(n, 2)
ε = int(n.translate(str.maketrans("10", "01")), 2)
print("part a:", 𝛾 * ε)

life_support = 1
s = "01"
for _ in s:
    i = 0
    ns = rows.copy()
    while len(ns) > 1:
        col = [n[i] for n in ns]
        b = col.count("1") >= col.count("0")
        ns = [n for n in ns if n[i] == s[b]]
        i += 1
    [n] = ns
    life_support *= int(n, 2)
    s = s[::-1]
print("part b:", life_support)

# def part1(self) -> int:
#     length = len(self.data_p1[0])
#     measurements = list(map(lambda x: int(x, 2), self.data_p1))
#     mask = 2**length -1
#     gamma = 0
#     for pos in reversed(range(length)):
#         masked = [(m & (1 << pos)) >> pos for m in measurements]
#         gamma += Counter(masked).most_common()[0][0] << pos
#     epsilon = ~gamma & mask
#     return gamma * epsilon

# def part2(self) -> int:
#     length = len(self.data_p2[0])
#     measurements = list(map(lambda x: int(x, 2), self.data_p2))
#     oxygen = co2 = measurements
#     for pos in reversed(range(length)):
#         oxy_masked = [(m & (1 << pos)) >> pos for m in oxygen]
#         co2_masked = [(m & (1 << pos)) >> pos for m in co2]
#         oxy_counts = Counter(oxy_masked).most_common()
#         co2_counts = Counter(co2_masked).most_common()
#         if len(oxy_counts) != 1:
#             oxy_most_common = oxy_counts[0][0] if oxy_counts[0][1] != oxy_counts[1][1] else 1
#             oxygen = list(filter(lambda x: x & (1 << pos) == oxy_most_common << pos, oxygen))

#         if len(co2_counts) != 1:
#             co2_least_common =  co2_counts[1][0] if co2_counts[0][1] != co2_counts[1][1] else 0
#             co2 = list(filter(lambda x: x & (1 << pos) == co2_least_common << pos, co2))

#     return oxygen[0] * co2[0]