#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

def check(s1, s2):
    # もしs1のほうが長いなら、s2と入れ替え
    if len(s1) > len(s2):
        return check(s2, s1)
    # 文の長さが、2以上違うなら調べない
    if len(s1) < len(s2) - 1:
        return False
    i, j, miss = 0, 0, 0
    # s1をすべて調べる
    while i < len(s1):
        # どちらも等しいときは、どっちも次の文字を見る
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            miss += 1
            # 編集距離が2以上になったら条件外
            if miss > 1:
                return False
            # 長さが等しいとき、置換しかしない
            if len(s1) == len(s2):
                i += 1
            # 長さが異なるとき、s2に挿入があったと考える
            j += 1
    return True

#main
def main():
    tmp = input().split(' ')
    N, T = int(tmp[0]), tmp[1]
    res = []
    for i in range(N):
        S = input()
        if check(S, T):
            res.append(i+1)
        
    print(len(res))
    print(*res)

if __name__ == '__main__':
    main()