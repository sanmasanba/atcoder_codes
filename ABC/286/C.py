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

def check(S, N, B):
    res = 0
    # 文字が異なるときにB円で操作
    for i in range(N//2):
        if S[i] != S[N-1-i]:
            res += B
    return res

#main
def main():
    N, A, B = map(int, input().split(' '))
    S = list(input())
    S += S
    # 操作順によらないので、Aをi回して、何回のBで回文にできるかを求める
    res = INF
    for i in range(N):
        res = min(res, A*i + check(S[i:i+N], N, B))
    print(res)

if __name__ == '__main__':
    main()