#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')
def ch_sec(t, l, r):
    if t == 1:
        return l, r
    elif t == 2:
        return l, r-0.1
    elif t == 3:
        return l+0.1, r
    else: 
        return l+0.1, r-0.1
    
#main
def main():
    N = int(input())
    T, L, R = [], [], []
    for _ in range(N):
        t, l, r = map(int, input().split(' '))
        T.append(t)
        L.append(l)
        R.append(r)
    
    res = 0
    cnt = 0
    # 全列挙で試す
    for i in range(N):
        for j in range(i, N):
            # iとjが一致するとき無視
            if i == j:
                continue
            # すべての組み合わせを数え上げ
            cnt += 1
            # 区間を修正する
            l_i, r_i = ch_sec(T[i], L[i], R[i])
            l_j, r_j = ch_sec(T[j], L[j], R[j])
            # 条件にはまらない組み合わせを数える
            if r_j < l_i or r_i < l_j: 
                res += 1
    # すべての組み合わせの数 - 条件外の数
    print(cnt - res)

if __name__ == '__main__':
    main()