#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, Q = map(int, input().split(' '))
    # folloerの管理
    follower = set()
    res = []
    for _ in range(Q):
        t, a, b = map(int, input().split(' '))
        if t == 1:
            follower.add((a, b))
        elif t == 2:
            follower.discard((a, b))
        else:
            if (a, b) in follower and (b, a) in follower:
                res.append('Yes')
            else:
                res.append('No')
    for r in res:
        print(r)

if __name__ == '__main__':
    main()