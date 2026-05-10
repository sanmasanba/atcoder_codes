#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N, S, K = map(int, input().split(' '))
    ans = 0
    for _ in range(N):
        x, y = map(int, input().split(' '))
        ans += x*y
    print(ans + (0 if ans >= S else K))

if __name__ == '__main__':
    main()