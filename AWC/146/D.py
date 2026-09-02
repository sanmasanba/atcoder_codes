# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

# main
def main():
    # intput
    N, M, Q = map(int, input().split())
    C, S, T = [], [], []
    for _ in range(N):
        S.append(list(input().strip()))
        C.append(list(input().strip()))
    for _ in range(N):
        T.append(list(input().strip()))

    # res[i][j][k] := S[i]とT[j]の回転量kの際の差
    res = [[[0]*M for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(M):
                for p in range(M):
                    if C[i][p] == '0' and S[i][p] != T[j][(p+k)%M]:
                        res[i][j][k] += 1

    # p の増減だけ考える
    for _ in range(Q):
        q, i, p, x = input().split()
        i, p = int(i)-1, int(p)-1
        if q == '1':
            for j in range(N):
                for k in range(M):
                    if C[i][p] == '0' and S[i][p] != T[j][(p+k)%M]:
                        res[i][j][k] -= 1
                    if C[i][p] == '0' and x != T[j][(p+k)%M]:
                        res[i][j][k] += 1
            S[i][p] = x
        elif q == '2': 
            for j in range(N):
                for k in range(M):
                    if C[i][p] == '0' and S[i][p] != T[j][(p+k)%M]:
                        res[i][j][k] -= 1
                    if x == '0' and S[i][p] != T[j][(p+k)%M]:
                        res[i][j][k] += 1
            C[i][p] = x
        elif q == '3': 
            j = i
            for i in range(N):
                for k in range(M):
                    if C[i][(p-k)%M] == '0' and S[i][(p-k)%M] != T[j][p]:
                        res[i][j][k] -= 1
                    if C[i][(p-k)%M] == '0' and S[i][(p-k)%M] != x:
                        res[i][j][k] += 1
            T[j][p] = x

        ans = INF
        for perm in permutations(range(N)):
            for k in range(M):
                ans = min(ans, sum(res[i][j][k] for i, j in enumerate(perm)))
        print(ans)
    
if __name__ == '__main__':
    main()
