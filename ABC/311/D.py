#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations, accumulate

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    # input
    N, M = map(int, input().split(' '))
    Sx = []; Sy = []
    Sx = [input() for _ in range(N)]
    Sy = list(zip(*Sx))
    X_list = [[i for i, s in enumerate(x) if s == '#'] for x in Sx]
    Y_list = [[i for i, s in enumerate(y) if s == '#'] for y in Sy]

    # bfs
    visited = set()
    visited.add((1, 1))
    res = set()
    res.add((1, 1))
    queue = deque()
    queue.append((1, 1))
    while queue:
        x, y = queue.popleft()
        next_pos = []
        xrange = (X_list[y][bisect_right(X_list[y], x)-1]+1, X_list[y][bisect_left(X_list[y], x)]-1)
        yrange = (Y_list[x][bisect_right(Y_list[x], y)-1]+1, Y_list[x][bisect_left(Y_list[x], y)]-1)
        for xx in range(xrange[0], xrange[1]+1):
            res.add((xx, y))
        for xx in xrange:
            if Sx[y][xx] == '.' and (xx, y) not in visited:
                visited.add((xx, y))
                queue.append((xx, y))
        for yy in range(yrange[0], yrange[1]+1):
            res.add((x, yy))
        for yy in yrange:
            if Sx[yy][x] == '.' and (x, yy) not in visited:
                visited.add((x, yy))
                queue.append((x, yy))

    # output
    print(len(res))

if __name__ == '__main__':
    main()