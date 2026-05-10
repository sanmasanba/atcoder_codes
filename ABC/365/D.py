#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

 # "R":0, "P":1 , "S":2
def check(t, a):
    if t == a:
        return 0
    elif (t == 0 and a == 1) or (t == 1 and a == 2) or (t == 2 and a == 0):
        return -1
    else:
        return 1

#main
def main():
    N = int(input())
    S = list(input())
    s2i = {"R":0, "P":1 , "S":2}

    # "R":0, "P":1 , "S":2
    dp = [[-1 for j in range(3)] for i in range(N)]

    # 勝ったときとあいこの時のみ更新
    for i in range(3):
        if check(i, s2i[S[0]]) == 1:
            dp[0][i] = 1
        elif check(i, s2i[S[0]]) == 0:
            dp[0][i] = 0

    # 2ターンめから回す
    for turn in range(1, N):
        # 前のターンの手
        for pre_choice in range(3):
            # 前の手が負けてたら、そこからの遷移は調べない
            if dp[turn-1][pre_choice] == -1:
                continue
            # 今のターンの手
            for t_choice in range(3):           
                # 前の手と被った時パス 
                if pre_choice == t_choice:
                    continue
                # 勝った時
                if check(t_choice, s2i[S[turn]]) == 1:
                    # 前の手の勝利数に1足して、最大値を取る
                    dp[turn][t_choice] = max(dp[turn][t_choice], dp[turn-1][pre_choice] + 1)
                # 負けた時
                elif check(t_choice, s2i[S[turn]]) == 0:
                    # 前の手の勝利数と比較
                    dp[turn][t_choice] = max(dp[turn][t_choice], dp[turn-1][pre_choice])
    
    print(max(dp[-1]))

if __name__ == '__main__':
    main()