#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, log
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    B = int(input())
    res = -1
    A = 1
    while 1:
        ans = A**A
        if B - ans == 0:
            res = A
            break
        if B < ans:
            break
        A += 1
    print(res)
if __name__ == '__main__':
    main()