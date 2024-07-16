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
    conn = [[False for j in range(N)] for i in range(N)]
    for _ in range(M):
        a, b = map(int, input().split(' '))
        conn[a-1][b-1] = True
    
    # 辺に対して、bit_search
    res = 1
    for i in range(2**N):
        tmp = []
        for j in range(N):
            # 派閥の構成員を列挙
            if (i >> j) & 1:
                tmp.append(j)
        # ひとり以下しかいないなら、スルー
        if len(tmp) < 2:
            continue
        edge = combinations(tmp, 2)
        #組み合わせを全列挙してチェック
        if all(map(lambda x: conn[x[0]][x[1]], edge)):
            res = max(res, len(tmp))
    print(res)

if __name__ == '__main__':
    main()