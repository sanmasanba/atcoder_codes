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
def solve(sx, sy, gx, gy):
    return sqrt((gx-sx)**2+(gy-sy)**2)*(10**7)


#main
def main():
    N = int(input())
    X, Y = [0], [0]
    for _ in range(N):
        a, b = map(int, input().split(' '))
        X.append(a)
        Y.append(b)
    X.append(0)
    Y.append(0)
            
    res = 0
    for i in range(N+1):
        sx, sy = X[i], Y[i]
        gx, gy = X[i+1], Y[i+1]
        res += solve(sx, sy, gx, gy)

    print(res/(10**7))

if __name__ == '__main__':
    main()