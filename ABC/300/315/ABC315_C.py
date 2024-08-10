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
    flavor = [list(map(int, input().split(' '))) for _ in range(N)]
    sort_flavor = sorted(flavor, key=lambda x: (-x[1], x[0]))
    tmp_res = sort_flavor[0][1]
    res = 0
    for f, s in sort_flavor[1:]:
        if sort_flavor[0][0] == f:
            res = max(res, tmp_res+s//2)
        else:
            res = max(res, tmp_res+s)
    print(res)

if __name__ == '__main__':
    main()