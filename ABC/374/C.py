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
    # input
    N = int(input())
    K = list(map(int, input().split(' ')))

    #bit_search
    res = INF
    for bit in range(2**N):
        team_a = 0
        team_b = 0
        for i in range(N):
            if (bit >> i) & 1:
                team_a += K[i]
            else:
                team_b += K[i]
        if 0 < team_a and 0 < team_b:
            res = min(res, max(team_a, team_b))

    # output
    print(res)

if __name__ == '__main__':
    main()