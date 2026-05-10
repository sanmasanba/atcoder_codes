#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, K = map(int, input().split(' '))
    inputAB = {}
    max_med = 0
    cumsum = []
    # その日ごとに何錠減るか
    for _ in range(N):
        a, b = map(int, input().split(' '))
        if a not in inputAB:
            inputAB[a] = 0
        inputAB[a] += b
        max_med += b
    AB = []
    # 減る日順にソート
    for k, v in inputAB.items():
        AB.append([k, v])
    AB.sort()

    # 累積和のリストを作る
    cumsum.append([0, max_med])
    for a, b in AB:
        cumsum.append([a+1, cumsum[-1][1]-b])
    
    # 線形探索
    for day, med_num in cumsum:
        if  med_num <= K:
            if day == 0:
                print(1)
            else:
                print(day)
            break

if __name__ == '__main__':
    main()