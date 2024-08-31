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

def main():
    H, W = map(int, input().split(' '))
    S, T = [None for _ in range(H)], [None for _ in range(H)]
    for h in range(H):
        S[h] = list(input())
    for h in range(H):
        T[h] = list(input())
    S = list(map(tuple, zip(*S)))
    T = list(map(tuple, zip(*T)))
    S.sort()
    T.sort()

    res = True
    for w in range(W):
        if S[w] != T[w]:
            res = False

    print("Yes" if res else "No")

if __name__ == '__main__':
    main()
