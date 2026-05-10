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
    N, M = map(int, input().split(' '))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split(' '))
        G[b].append(a)
    res = -1
    for i in range(N):
        if not G[i] and res == -1:
            res = i+1
        elif not G[i] and res != -1:
            res = -1
            break
    print(res)

if __name__ == '__main__':
    main()