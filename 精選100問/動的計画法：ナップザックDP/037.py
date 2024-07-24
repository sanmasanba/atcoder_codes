#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split(' '))
    C = list(map(int, input().split(' ')))
    C.sort()

    # DPの準備
    dp = [[INF for j in range(N+1)] for i in range(M+1)]
    dp[0][0] = 0

    # コインごとに考える
    for num in range(M):
        for bill in range(N+1):    
            # 支払い金額に対して、コインがまだ払えるなら比較
            if bill >= C[num]:
                # コインの金額分引いたところに+1か、足さなかったときの比較をする
                #　min(１つ小さい金額の差額分の枚数を引いて＋１枚, いまの金額の差額分の枚数を引いて＋１枚, 追加しない)
                dp[num+1][bill] = min(dp[num][bill-C[num]]+1, dp[num+1][bill-C[num]]+1, dp[num][bill])
            # 支払い金額を超えているときは、そのまま
            else:
                dp[num+1][bill] = dp[num][bill]
    print(dp[M][N])

if __name__ == '__main__':
    main()