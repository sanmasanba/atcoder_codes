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
    q = int(input())
    Q = []
    res = []
    for _ in range(q):
        X = input()
        Y = input()
        Q.append([X, Y])
    for X, Y in Q:
        dp = [[0 for j in range(len(X)+1)] for i in range(len(Y)+1)]

        for i in range(1, len(Y)+1):
            for j in range(1, len(X)+1):
                # 文字が一致するとき
                if Y[i-1] == X[j-1]:
                    # 文字数が少ないときの最大一致と今の最大値を比較
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # 今の最大値で代入
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # for i in dp:
        #     print(i)
        res.append(dp[-1][-1])
    for i in res:
        print(i)

if __name__ == '__main__':
    main()