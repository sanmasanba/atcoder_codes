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

    # 全探索
    res = 0
    # aの取りうる範囲は、1 <= a <= (N)^(1/3)
    for a in range(1, N+1):
        if N < a**3: break
        # bの取りうる範囲は、a <= b <= (N/a)^(1/2)
        for b in range(a, N+1):
            if N < a*b*b: break
            # c の取りうる範囲は、b <= c <= N/(AB) 
            # -> 実行回数はN/(AB)-b+1になるので、変形して足す
            res += N//a//b-b+1

    print(res)

if __name__ == '__main__':
    main()