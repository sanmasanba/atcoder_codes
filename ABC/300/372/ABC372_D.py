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
    H = list(map(int, input().split(' ')))
    max_h = [0 for _ in range(N)]

    tmp_max = 0
    for i in range(N):
        if i == 0:
            max_h[i] = H[i]
        else:
            max_h[i] = max(H[i], max_h[i-1])
    print(max_h)

if __name__ == '__main__':
    main()