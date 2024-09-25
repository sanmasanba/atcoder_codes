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
    S = list(input())
    
    b_pos = [i for i, s in enumerate(S) if s == 'B']
    res = b_pos[0]%2 != b_pos[1]%2
    res &= S.index('R') < S.index('K') < (7-list(reversed(S)).index('R'))

    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()