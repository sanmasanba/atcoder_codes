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
    S = list(input())
    N = len(S)
    res = N * N

    # それぞれの文字が文字列中に何回登場するか
    cnt = {}
    for s in S:
        if s not in cnt:
            cnt[s] = 0
        cnt[s] += 1
    v = cnt.values()
    # 最終的な答えは(N**2 - sigma(それぞれの文字の登場数**2))//2
    for i in v:
        res -= i*i
    res //= 2
    # もし2回以上登場する文字が存在するなら、
    # その時は、元に戻るパターンがあるので+1する。
    if max(v)>1:
        res += 1
    print(res)    

if __name__ == '__main__':
    main()