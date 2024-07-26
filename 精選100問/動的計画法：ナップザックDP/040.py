#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations
from typing import List, Dict

sys.setrecursionlimit(10**6)
INF = float('inf')
MOD: int = 10000

#main
def main():
    N, K = map(int, input().split(' '))
    AB = [list(map(int, input().split(' '))) for _ in range(K)]
    
    # 予定を辞書に保存
    D: Dict[int, int] = {a: b - 1 for a, b in AB}
    # DPの準備
    # dp[i日目][j番目の味][0:前日に異なる味を食べた組み合わせ, 1:前日に同じ味を食べた組み合わせ]
    dp: List[List[List[int]]] = [[[0]*2 for j in range(3)] for i in range(N+1)]
    # 初日が決まっている場合と、それ以外で場合分け
    if 1 in D:
        dp[1][D[1]] = [1, 0]
        dp[1][(D[1]+1)%3] = [0, 0]
        dp[1][(D[1]+2)%3] = [0, 0]
    else:
        dp[1] = [[1, 0] for _ in range(3)]

    # DP
    for day in range(2, N+1):
        for flavor in range(3):
            # 前日と異なる味を食べる
            dp[day][flavor][0] = sum(dp[day-1][(flavor+1)%3]) + sum(dp[day-1][(flavor+2)%3])
            # 前日と同じ味を食べる
            dp[day][flavor][1] = dp[day-1][flavor][0]

            # MOD
            dp[day][flavor][0] %= MOD
            dp[day][flavor][1] %= MOD
        
        # もし、予定が決まっているなら、予定の味以外を0通りにする
        if day in D:
            dp[day][(D[day]+1)%3] = [0, 0]
            dp[day][(D[day]+2)%3] = [0, 0]
    
    res = 0
    for flavor in range(3):
        for i in range(2):
            res += dp[N][flavor][i]
    print(res%MOD)

if __name__ == '__main__':
    main()