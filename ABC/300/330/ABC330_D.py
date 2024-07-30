#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, factorial
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    S = []
    col_cnt = [0 for _ in range(N)]
    row_cnt = [0 for _ in range(N)]
    cnt_sum = 0

    for i in range(N):
        s = list(input())
        S.append(s)
        tmp_counter = Counter(s)
        # row方向の'o'の数
        row_cnt[i] = tmp_counter['o']
        cnt_sum += tmp_counter['o']
    # col方向の'o'の数
    for i in range(N):
        for j in range(N):
            col_cnt[i] += (1 if S[j][i] == 'o' else 0)
    
    res = 0
    for row in range(N):
        # 行に一つしか'o'がないとき、条件を満たさない
        if row_cnt[row] <= 1:
            continue
        for col in range(N):
            # S[i][j]に'o'があるとき
            if S[row][col] == 'o':
                # S[i][j]を使って条件を満たすのは
                # S[i][j]を中心に十字を考えて、(縦の個数-1)*(横の個数-1)
                res += (row_cnt[row]-1)*(col_cnt[col]-1) 
    print(res)

if __name__ == '__main__':
    main()