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
    N, X = map(int, input().split(' '))
    AB = []
    for _ in range(N):
        a, b = map(int, input().split(' '))
        AB += [a]*b
    AB.sort()

    dp = [[0 for x in range(X+1)] for _ in range(len(AB)+1)]
    dp[0][0] = 1
    for i, a in enumerate(AB):
        # 足してX円以下になる金額まで
        for j in range(X+1):
            # a円を選択したとき
            if dp[i][j] and j+a <= X:
                dp[i+1][j+a] = 1
            # 選択しないとき
            if dp[i][j]:
                dp[i+1][j] = 1

    print("Yes" if dp[-1][-1] else "No")

if __name__ == '__main__':
    main()