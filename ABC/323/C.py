#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

def func(Sn):
    tmp = sorted(list(set(Sn)))
    return tmp[-2]

#main
def main():
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    # 入力と点数の計算
    # それぞれの現在の点
    Sn = []
    # 未回答の問題
    Q = []
    for p in range(1, N+1):
        S = list(input())
        Sn.append(sum([A[i] if s == 'o' else 0 for i, s in enumerate(S)]) + p)
        tmp = []
        for i, s in enumerate(S):
            if s == 'x': tmp.append(A[i]) 
        tmp.sort(reverse=True)
        Q.append([0] + tmp)
    
    for p in range(N):
        # 未解決の問題を解いていく
        sum_max = func(Sn) if max(Sn) == Sn[p] else max(Sn)
        sum_point = Sn[p]
        for q in range(len(Q[p])):
            sum_point += Q[p][q]
            if sum_max < sum_point:
                print(q)
                break

if __name__ == '__main__':
    main()