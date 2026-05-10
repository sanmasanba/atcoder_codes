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
    A, B, C, D = map(int, input().split(' '))
    diff = C*D - B
    res = -1
    if 0 < diff:
        res = (A+diff-1)//diff
    print(res)

if __name__ == '__main__':
    main()