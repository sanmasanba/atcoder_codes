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
    N, W = map(int, input().split(' '))
    cheeses = []
    for _ in range(N):
        a, b = map(int, input().split(' '))
        cheeses.append([a, b])
    cheeses.sort()

    # 貪欲法
    res = 0
    while cheeses:
        cheese = cheeses.pop()
        if 0 <= W-cheese[1]:
            res += cheese[0]*cheese[1]
            W -= cheese[1]
        else:
            res += cheese[0]*W
            break
    print(res)

if __name__ == '__main__':
    main()