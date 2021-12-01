from aocd import data

measurements = [int(m) for m in data.split()]
print("part a:", sum(m2 > m1 for m1, m2 in zip(measurements, measurements[1:])))
print("part b:", sum(m2 > m1 for m1, m2 in zip(measurements, measurements[3:])))