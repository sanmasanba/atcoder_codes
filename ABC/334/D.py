#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, Q = map(int, input().split(' '))
    R = list(map(int, input().split(' ')))
    Query = [int(input()) for _ in range(Q)]
    R.sort()
    # 少ない順に累積和を求める
    cumsumR = [0]
    for r in R:
        cumsumR.append(cumsumR[-1]+r)
    # 二分探索して、挿入点を求めて出力
    for q in Query:
        res = bisect_right(cumsumR, q)
        print(res-1)
    
if __name__ == '__main__':
    main()