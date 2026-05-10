#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, factorial
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations
from string import ascii_lowercase

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    S = list(input())
    
    # 初期値
    left = 0
    right = 0
    # それぞれの文字の最大長を保存
    ch_list = {s:0 for s in ascii_lowercase}
    # 尺取り法
    for left in range(N):
        # 左の文字と比較
        left_ch = S[left]
        # 文字列が同一文字の間、右に進める
        while right < N and S[right] == left_ch:
            right += 1
            # 同じ文字で構成されたものを追加していく
        # 最大長を更新
        ch_list[left_ch] = max(ch_list[left_ch], right-left)

    # 出力
    res = 0
    for _, v in ch_list.items():
        res += v
    print(res)
        
if __name__ == '__main__':
    main()