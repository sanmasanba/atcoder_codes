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
    N = int(input())
    A = list(map(int, input().split(' ')))
    
    # 最大公約数を求める
    g = A[0]
    for i in range(1, N):
        g = gcd(g, A[i])
    
    res = 0
    # 割れるだけ割って、余りが1にならないなら不可能
    for i in range(N):
        a = A[i]//g
        for p in [2, 3]:
            while a % p == 0:
                res += 1
                a //= p
        if a != 1:
            return -1
    return res

if __name__ == '__main__':
    print(main())