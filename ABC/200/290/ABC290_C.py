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
    N, K = map(int, input().split(' '))
    A = set(map(int, input().split(' ')))
    
    res = 0
    for i in range(K):
        if i in A:
            res = i + 1
        else:
            break
    print(res)

if __name__ == '__main__':
    main()