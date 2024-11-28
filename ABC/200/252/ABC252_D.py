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
    A = list(map(int, input().split(' ')))
    counter = Counter(A)

    res = 0    
    nums = len(counter)
    res = (N*(N-1)*(N-2))//6

    for _, v in counter.items():
        if 1 < v:
            res -= (N - v) * (v*(v-1))//2
        if 2 < v:
            res -= (v*(v-1)*(v-2))//6

    print(res)

if __name__ == '__main__':
    main()