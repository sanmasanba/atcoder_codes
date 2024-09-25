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
    N = int(input())
    S = input()
    W = list(map(int, input().split(' ')))

    sort_w = []
    ans = 0
    # 閾値を0として、大人の数を数える
    for i, w in enumerate(W):
        if S[i] == '1':
            ans += 1
        sort_w.append([w, S[i]])
    sort_w.sort()

    # 閾値を０から少しずつ大きくする
    x = ans
    for i in range(N):
        threshold, flg = sort_w[i]
        # 値を移動させて、大人か子供か判定しなおす
        if flg == '1':
            x -= 1
        else:
            x +=1
        # 閾値が更新されるときに、結果の更新をする
        if i < (N-1):
            if threshold != sort_w[i+1][0]:
                ans = max(ans, x)
        else:
            ans = max(ans, x)
    print(ans)

if __name__ == '__main__':
    main()