#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    A, B = map(int, input().split(' '))
    
    if A <= B <= 6*A:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()