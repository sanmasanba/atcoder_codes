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
    # input
    N = int(input())
    A = list(map(int, input().split(' ')))
    X = int(input())
    
    # 総和で割って、あまりだけ考える
    sum_A = sum(A)
    res = (X//sum_A)*N
    X = X%sum_A
    s = 0
    for a in A:
        if X < s:
            break
        s += a
        res += 1

    # output
    print(res)

if __name__ == '__main__':
    main()