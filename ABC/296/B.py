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
    S = []
    for i in range(8):
        S.append(input())

    j2n = {j:n for j, n in enumerate('abcdefgh')}

    for i in range(8):
        for j in range(8):
            if S[i][j] == '*':
                print(f"{j2n[j]}{8-i}")

if __name__ == '__main__':
    main()