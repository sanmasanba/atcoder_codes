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
    S = list(input())
    
    res = 0
    for i in range(1, N-1):
        if S[i-1] == '#' and S[i] == '.' and S[i+1] == '#':
            res += 1
    print(res)

if __name__ == '__main__':
    main()