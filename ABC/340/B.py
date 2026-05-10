#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    Q = int(input())
    stack = []
    res = []
    for _ in range(Q):
        q, x = input().split(' ')
        if q == '1':
            stack.append(int(x))
        else:
            res.append(stack[-int(x)])

    for i in res:
        print(i)

if __name__ == '__main__':
    main()