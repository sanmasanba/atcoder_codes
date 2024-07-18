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
    d = int(input())
    n = int(input())
    m = int(input())
    di = [0] + [int(input()) for _ in range(n-1)]
    ki = [int(input()) for _ in range(m)]
    di.sort()

    res = 0
    for k in ki:
        pos = bisect_left(di, k)
        if pos >= n:
            res += min(d-k, k-di[-1])
        else:
            res += min(max(0, k - di[pos-1]), di[pos] - k)

    print(res)

if __name__ == '__main__':
    main()