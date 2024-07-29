# cppでも解いたので、atcoder_cpp/精選100問/044.cppを参照
# url : https://github.com/sanmasanba/atcoder_cpp/blob/master/%E7%B2%BE%E9%81%B8100%E5%95%8F/044.cpp

#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

def main():    
    # 最終的な状態しか結果に影響しないので、dpテーブルは１次元でいい
    # （重複を許すDP）
    dp_all = [INF] * 1000001
    dp_odd = [INF] * 1000001
    
    # init_dp
    dp_all[0] = 0
    dp_odd[0] = 0

    # init_num2sq
    # all
    num2sq_all = [(n * (n + 1) * (n + 2)) // 6 for n in range(1, 201)]
    # odd
    num2sq_odd = [num for num in num2sq_all if num % 2 == 1]

    # execute dp
    # all
    for num in num2sq_all:
        for tmp_sum in range(num, 1000001):
            dp_all[tmp_sum] = min(dp_all[tmp_sum], dp_all[tmp_sum - num] + 1)
    # odd
    for num in num2sq_odd:
        for tmp_sum in range(num, 1000001):
            dp_odd[tmp_sum] = min(dp_odd[tmp_sum], dp_odd[tmp_sum - num] + 1)

    reses = []
    while True:
        N = int(input())
        if N == 0:
            break

        tmp_res_all = dp_all[N]
        tmp_res_odd = dp_odd[N]

        reses.append((tmp_res_all, tmp_res_odd))

    for res in reses:
        print(res[0], res[1])

if __name__ == "__main__":
    main()