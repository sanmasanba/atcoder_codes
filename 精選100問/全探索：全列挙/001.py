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
    N, X = [], []
    while 1:
        n ,x = map(int, input().split(' '))
        if n == 0 and x == 0:
            break
        N.append(n)
        X.append(x)
    for n, x in zip(N,  X):
        if N == 0 and X == 0:
            break
        cnt = 0
        for j in combinations([i+1 for i in range(n)], 3):
            if j[0] + j[1] + j[2] == x:
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()