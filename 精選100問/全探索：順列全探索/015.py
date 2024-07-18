#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    X, Y = [], []
    for _ in range(N):
        a, b = map(int, input().split(' '))
        X.append(a)
        Y.append(b)
    
    res = 0
    # すべての巡り順に関して求める
    for root in permutations([i for i in range(N)]):
        for s, g in zip(root[:-1], root[1:]):
            res += sqrt(((X[s]-X[g])**2)+((Y[s]-Y[g])**2))
    # N!を求める
    n = 1
    for i in range(1, N+1):
        n *= i 
    print(res/n)

if __name__ == '__main__':
    main()