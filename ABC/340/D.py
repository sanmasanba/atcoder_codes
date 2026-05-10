import sys
from heapq import heappush, heappop
from collections import defaultdict

sys.setrecursionlimit(10**6)
INF = float('inf')

def dijkstra(G, N, s):
    distances = [INF] * N
    distances[s] = 0

    target_nodes = []
    heappush(target_nodes, (0, s))

    while target_nodes:
        current_dist, current_node = heappop(target_nodes)

        if current_dist > distances[current_node]:
            continue

        for next_node, weight in G[current_node]:
            dist = current_dist + weight
            if dist < distances[next_node]:
                distances[next_node] = dist
                heappush(target_nodes, (dist, next_node))

    return distances

def main():
    # input
    N = int(input())
    G = defaultdict(list)
    for i in range(N-1):
        a, b, x = map(int, input().split())
        x -= 1
        G[i].append((i+1, a))
        G[i].append((x, b))
    # ゴールのノードを追加
    G[N-1] = []

    reached_time = dijkstra(G, N, 0)
    print(reached_time[-1])

if __name__ == '__main__':
    main()
