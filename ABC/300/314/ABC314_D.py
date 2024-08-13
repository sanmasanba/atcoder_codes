#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    S = list(input())
    Q = int(input())
    Query = [list(input().split(' ')) for _ in range(Q)]
    # 小文字は1、大文字は0とする
    char_set = set()
    char_mode = 1
    for i in range(N):
        if 65 <= ord(S[i]) <= 90:
            char_set.add(i)
    
    # クエリの処理
    for i, j, k in Query:
        # クエリをそれぞれ変換
        t, x, c = int(i), int(j)-1, k 
        if t == 1:
            S[x] = c
            # 大文字モードの時
            if char_mode == 0:
                # 追加された文字が小文字なら追加
                if 97 <= ord(c) <= 122:
                    char_set.add(x)
                # ->大文字だったら削除
                else:
                    if x in char_set: char_set.discard(x) 
            # 小文字モードの時
            else:
                # 追加された文字が大文字なら追加
                if 65 <= ord(c) <= 90:
                    char_set.add(x)
                    # ->小文字だったら削除
                else:
                    if x in char_set: char_set.discard(x) 
        elif t == 2:
            # 基本は小文字で、大文字だけ記録
            char_mode = 1
            char_set = set()
        else:
            # 基本は大文字で、小文字だけ記録
            char_mode = 0
            char_set = set()

    if char_mode:
        print("".join([S[i].upper() if i in char_set else S[i].lower() for i in range(N)]))
    else:
        print("".join([S[i].lower() if i in char_set else S[i].upper() for i in range(N)]))

if __name__ == '__main__':
    main()