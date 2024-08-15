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
    P = list(map(int, input().split(' ')))
    res = -1
    for i in P[1:]:
        res = max(res, i-P[0])
    print(0 if res == -1 else res+1)

if __name__ == '__main__':
    main()