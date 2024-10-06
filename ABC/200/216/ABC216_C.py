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
    # 入力
    N = int(input())

    res = ''
    while N:
        if N%2:
            res = 'A' + res
            N -= 1
        else:
            res = 'B' + res
            N //= 2
    # 出力
    print(res)

if __name__ == '__main__':
    main()