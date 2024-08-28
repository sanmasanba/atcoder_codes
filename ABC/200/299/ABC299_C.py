#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    S = input()
    
    # 文字列圧縮
    compression = []
    pre_s = None
    cnt = 0
    for i in range(N):
        # 最初の文字列はスルー
        if i == 0:
            pre_s = S[i]
            cnt += 1
            continue
        if pre_s != S[i]:
            compression.append((pre_s, cnt))
            pre_s = S[i]; cnt = 1
        else:
            cnt += 1
    compression.append((pre_s, cnt))
    
    res = -1
    length = len(compression)
    # 長さ1なら達成不可
    if length == 1:
        pass
    # 長さ2なら'o'の長さが最大長
    elif length == 2:
        if compression[0][0] == '-':
            res = max(res, compression[1][1])
        else:
            res = max(res, compression[0][1])
    # 長さ3以上なら条件を満たす最大長
    else:
        for i in range(1, length-1):
            if compression[i][0] == '-':
                res = max(res, compression[i+1][1], compression[i-1][1])
            else:
                res = max(res, compression[i][1])
    print(res)

if __name__ == '__main__':
    main()


# 別解
# print(max(map(len, S.split('-'))) if 'o' in S and '-' in S else -1)
# 1)どちらかしか含まれないとき、達成不可
# 2)どちらも含まれるとき、必ず'-'と'o'が隣接している
#   ->'o'の最大長が答え