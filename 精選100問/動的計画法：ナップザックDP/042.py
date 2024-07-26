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
    dists = [int(input()) for _ in range(N)]
    weathres = [int(input()) for _ in range(M)]
    
    # j日かけて、i番目までの町まで行った時の最小疲労度
    dp = [[INF] * (M+1) for _ in range(N+1)]
    # 最初の町は、0日目の疲労度が0
    for day in range(M+1):
        dp[0][day] = 0

    # 町iで
    for city in range(N):
        # j日目において
        for day in range(M):
            # 町iにj日かけてきたときに
            # j日目は、町i-1から移動してきたときと
            # j日目は、町iに待機しているときで比較
            dp[city+1][day+1] = min(dp[city][day]+dists[city]*weathres[day], dp[city+1][day])

    print(dp[-1][-1])

if __name__ == '__main__':
    main()