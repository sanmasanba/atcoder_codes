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
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())

    # すでにあるフォルダと数字を管理
    seen = {}
    for s in S:
        if s not in seen:
            seen[s] = 0
            print(s)
        else:
            print(s + f'({seen[s]})')    
        seen[s] += 1

if __name__ == '__main__':
    main()