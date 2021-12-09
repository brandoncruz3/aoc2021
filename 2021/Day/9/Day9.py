
from aocd import data 
import sys
import networkx as nx
import heapq
import math
from zgrid import ZGrid

g = ZGrid(data)
print("part a:", sum(1 + int(n) for z0, n in g.items() if all(n < g.get(z, 'z') for z in g.near(z0))))
basin_sizes = [len(b) for b in nx.connected_components(g.graph(extra="012345678"))]
print(basin_sizes)
print("part b:", math.prod(heapq.nlargest(3, basin_sizes)))