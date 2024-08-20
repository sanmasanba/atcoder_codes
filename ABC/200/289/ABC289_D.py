#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

# ライブラリはここに貼り付け

sys.setrecursionlimit(10**6)
INF = float('inf') 

#main
def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    M = int(input())
    B = set(map(int, input().split(' ')))
    X = int(input())
    
    # 各段にと立つできるかを管理
    dp = [0 for i in range(X+1)]
    # 0段目は確実にいる
    dp[0] = 1
    for x in range(X):
        # あり得る段だけかんがえる　
        if dp[x]:
            # 全部試す
            for a in A:
                next_step = x+a
                if next_step <= X and next_step not in B:
                    dp[next_step] = 1
    print('Yes' if dp[X] else 'No')

if __name__ == '__main__':
    main()