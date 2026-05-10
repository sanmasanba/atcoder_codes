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
    N = int(input())
    Q = {}
    for _ in range(N):
        a, c = map(int, input().split(' '))
        if c+1 not in Q:
            Q[c+1] = INF
        Q[c+1] = min(Q[c+1], a)
    A = [v for v in Q.values()]
    print(max(A))
        
if __name__ == '__main__':
    main()