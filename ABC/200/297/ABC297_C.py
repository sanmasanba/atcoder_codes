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
    H, W = map(int, input().split(' '))
    S = []
    for _ in range(H):
        S.append(list(input()))

    for h in range(H):
        for w in range(W-1):
            if S[h][w] == "T" and S[h][w+1] == "T":
                S[h][w], S[h][w+1] = "P", "C"

    for s in S:
        print(*s, sep='') 

if __name__ == '__main__':
    main()