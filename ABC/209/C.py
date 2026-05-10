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
MOD = 10**9+7

#main
def main():
    # 入力
    N = int(input())
    C = list(map(int, input().split(' ')))

    # ソートして考える
    # (10, 10, 10)の時
    # 1桁目は、どの桁も選べるので、10通り
    # 2桁めは、1桁目で選んだ数字が選べないので9通り
    # 3桁めは、1桁目と2桁目で選んだものが選べないので8通り
    # したがって、i桁目はC[i]-i個の選択ができる
    C.sort()
    res = 1
    for i in range(N):
        res = res * max(0, C[i]-i) % MOD

    # 出力
    print(res)

if __name__ == '__main__':
    main()