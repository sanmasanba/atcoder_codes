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
    A = list(map(int, input().split(' ')))
    A.sort()

    left = 0
    right = 0
    res = 0
    while left < N:
        # 同じ靴下の枚数を数える
        cnt = 0
        while right < N and A[left] == A[right]:
            right += 1
            cnt += 1
        res += cnt//2

        left = right
    print(res)

if __name__ == '__main__':
    main()