import heapq

with open('./input.txt', 'r') as file:
    raw_data = file.read()
    
def parse_input(raw_data):
    res = []
    for line in raw_data.split('\n'):
        res.append(list(map(int, line)))
    return res

CAVERN = parse_input(raw_data)
N, M = len(CAVERN), len(CAVERN[0])

def dijkstra(graph):
    r, c = len(graph), len(graph[0])
    costs = {}
    heap = [(0, 0, 0)]
    while heap:
        cost, i, j = heapq.heappop(heap)
        if (i, j) == (r - 1, c - 1):
            return cost
        for ni, nj in  ((i + 1, j), (i - 1, j), (i, j+1), (i, j-1)):
            if 0 <= ni < r and 0 <= nj < c:
                ncost = cost + graph[ni][nj]
                if cost.get((ni, nj), float('inf')) <= ncost:
                    continue
                costs[(ni, nj)] = ncost
                heapq.heappush(heap, (ncost, ni, nj))
                
def p1():
    return dijkstra(CAVERN)

print(p1())
