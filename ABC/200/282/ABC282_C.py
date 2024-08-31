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
    
    flg = 0
    for s in S:
        if s == '"':
            flg = (flg+1)%2
            print(s, end='')
        elif not flg and s == ',':
            print('.', end='')
        else:
            print(s, end='')

if __name__ == '__main__':
    main()