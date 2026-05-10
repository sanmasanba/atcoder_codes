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
    N, X = map(int, input().split(' '))
    S = list(input())
    T = []
    for s in S:
        if s=='U' and len(T) > 0 and (T[-1]=='L' or T[-1]=='R'):
            T.pop()
        else:
            T.append(s)

    for s in T:
        if s == 'U':
            if X == 1:
                continue
            X = X >> 1
        if s == 'R':
            X = X << 1
            X += 1
        if s == 'L':
            X = X << 1

    # output
    print(X)                

if __name__ == '__main__':
    main()