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
    x1, y1, x2, y2 = map(int, input().split(' '))
    
    coordinate = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
            
    res = False
    for dx, dy in coordinate:
        res |= (dx)**2+(dy)**2 - ((x1+dx-x2)**2+(y1+dy-y2)**2) == 0

    print("Yes" if res else "No")

if __name__ == '__main__':
    main()