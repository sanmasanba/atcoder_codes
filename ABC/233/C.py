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
    N, X = map(int, input().split(' '))
    L, A = [], {}
    for i in range(N):
        tmp = list(map(int, input().split(' ')))
        l, a = tmp[0], tmp[1:]
        L.append(l)
        A[i] = a
    # 答えの管理
    res = {i:{} for i in range(N)}
    # 最初はそのまま
    res[0] = Counter(A[0])

    # 二袋ごとに管理
    for i in range(1, N):
        for val, cnt in res[i-1].items():
            for a in A[i]:
                product = val*a
                # 答えの記録
                if product not in res[i]:
                    res[i][product] = 0
                res[i][product] += cnt
    print(res[N-1][X] if X in res[N-1] else 0)

if __name__ == '__main__':
    main()