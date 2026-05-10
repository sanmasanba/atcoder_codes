#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')
def per(R:list, N:int, K:int, i:int, crr:list):
    if i == N-1:
        return list(map(str, R[i]))
    r = R[i]
    res = []
    for n in r:
        for j in per(R, N, K, i+1, crr):
            res.append(str(n)+str(j))
    return res

#main
def main():
    N, K = map(int, input().split(' '))
    R = list(map(int, input().split(' ')))
    res = []
    r = [[j for j in range(1, R[i]+1)] for i in range(N)]
    # 全列挙する
    res = per(r, N, K, 0, [])
    # 評価する
    for r in res:
        r = list(map(int, list(r)))
        if sum(list(map(int, r)))%K == 0:
            print(*r)

if __name__ == '__main__':
    main()