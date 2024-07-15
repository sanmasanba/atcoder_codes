#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split(' '))
    NM = [list(map(int, input().split(' '))) for _ in range(N)]
    res = 0
    for ms in combinations([i for i in range(M)], 2):
        tmp = 0
        for i in range(N):
            tmp += max(NM[i][ms[0]], NM[i][ms[1]])
        res = max(res, tmp)
    print(res)
if __name__ == '__main__':
    main()