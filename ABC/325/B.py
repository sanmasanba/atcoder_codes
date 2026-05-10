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
    WX = [list(map(int, input().split(' '))) for _ in range(N)]
    
    res = 0
    for time in range(24):
        tmp_res = 0
        for w, x in WX:
            if 9 <= (x + time)%24 <= 17:
                tmp_res += w
        res = max(res, tmp_res)
    print(res)

if __name__ == '__main__':
    main()