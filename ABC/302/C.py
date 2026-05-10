#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')
# 距離を調べる
def solve(M, t1, t2):
    cnt = 0
    for m in range(M):
        cnt += t1[m] != t2[m]
    return False if cnt > 1 else True
#main
def main():
    N, M = map(int, input().split(' '))
    S = [input() for _ in range(N)]
    res = False
    # 全列挙
    for T in permutations(S):
        if all([solve(M, T[i], T[i+1]) for i in range(N-1)]):
            res = True
    print("Yes" if res else "No")

if __name__ == '__main__':
    main()