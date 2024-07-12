#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    H, W = map(int, input().split(' '))
    As = [list(map(int, input().split(' '))) for _ in range(H)]

    dp = [[0 for j in range(W+1)] for i in range(H+1)]
    pair = [[set() for j in range(W+1)] for _ in range(H+1)]

    dp[0][0] = 1
    pair[0][0].add(As[0][0])

    res = 0
    for i in range(2**(H+W-2)):
        #ここで判定用の変数を初期化する
        tmp = set([As[0][0]])
        h, w = 0, 0
        for j in range((H+W-2)):
            if (i >> j) & 1:
                #ここで何か操作を入れる
                h += 1
            else:
                w += 1
            if h < H and w < W:
                tmp.add(As[h][w])
            else:
                break
        #組み合わせに関して、要素を満たすか判定する
        #print(tmp)
        if len(tmp) == (H+W-1) and (h+1 == H or w+1 == W):
               res += 1
            
    print(res)

if __name__ == '__main__':
    main()