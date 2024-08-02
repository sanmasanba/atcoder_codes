#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    
    for x in range(61):
        for y in range(61):
            if 10**18 < (2**x)*(3**y):
                break
            if N == (2**x)*(3**y):
                print('Yes')
                sys.exit(0)
    print('No')

if __name__ == '__main__':
    main()