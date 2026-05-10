#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    grid = [[0 for _ in range(N)] for _ in range(N)]

    grid[(N)//2][(N)//2] = 'T'

    queue = deque([(1, 0), (0, -1), (-1, 0)])
    nextd = (0, 1)
    h, w, i = 0, 0, 1
    while grid[h][w] == 0:
        grid[h][w] = i
        i += 1
        # ぶつからないで、範囲内なら直進
        if 0 <= h+nextd[0] < N and 0 <= w+nextd[1] < N and grid[h+nextd[0]][w+nextd[1]] == 0:
                h, w = h+nextd[0], w+nextd[1]
        else:
            queue.append(nextd)
            nextd = queue.popleft()
            h, w = h+nextd[0], w+nextd[1]
    
    for i in grid:
         print(*i)

if __name__ == '__main__':
    main()