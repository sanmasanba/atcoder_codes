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
    T = input()
    N = int(input())
    As = []
    for _ in range(N):
        _, *s = list(input().split(' '))
        s.extend([''])
        As.append(s)
    
    # dp[n][s] := n袋目までで作れる文字列sの最小コスト
    dp = [{'': 0} for i in range(N+1)]
    for i in range(N):
        for start, cost in dp[i].items():
            for s in As[i]:
                new_s = start + s
                if T.startswith(new_s):
                    if new_s not in dp[i+1]:
                        dp[i+1][new_s] = INF
                    dp[i+1][new_s] = min(dp[i+1][new_s], cost + (1 if s != '' else 0))

    # output
    res = INF
    for S, cost in dp[-1].items():
        if S == T:
            res = min(res, cost)
    print(-1 if res == INF else res)

if __name__ == '__main__':
    main()