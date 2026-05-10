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
    A, B = map(int, input().split(' '))
    
    res = 0
    for x in range(-300, 300):
        if x - A == A - B:
            res += 1
        elif A - x == x - B:
            res += 1
        elif A - B == B - x:
            res += 1
    print(res)

if __name__ == '__main__':
    main()