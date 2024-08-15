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
    S = set()
    for _ in range(N):
        s = tuple(input())
        s_r = tuple(reversed(s))
        if s not in S and s_r not in S: 
            S.add(s)
    print(len(S))

if __name__ == '__main__':
    main()