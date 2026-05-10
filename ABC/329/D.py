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
    A = list(map(int, input().split(' ')))
    # それぞれの候補の票数を管理
    votes = [0 for _ in range(N+1)]
    # 現在の候補者と得票数
    res = [-1, INF]

    for a  in A:
        # 票を追加
        votes[a] += 1
        # 最大が更新されないならスルー
        if votes[a] < res[0]:
            pass
        # 得票数が並んだら、小さいほうが候補に
        elif votes[a] == res[0]:
            res[1] = min(a, res[1])
        # 得票数が上回ったら、候補者と得票数を更新
        else:
            res[0], res[1] = votes[a], a
        print(res[1])
    
if __name__ == '__main__':
    main()