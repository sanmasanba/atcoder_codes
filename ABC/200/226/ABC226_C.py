#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

def search(T, K, A, V, x):
    if V[x]:
        return 0
    V[x] = 1
    if K[x] == 0:
        return T[x]
    else:
        s = 0
        for i in A[x]:
            s += search(T, K, A, V, i-1)
        return T[x] + s

#main
def main():
    N = int(input())
    T, K, A, V = [], [], [], []
    for _ in range(N):
        t, k, *a = map(int, input().split(' '))
        T.append(t)
        K.append(k)
        A.append(a)
        V.append(0)

    root = N-1
    res = search(T, K, A, V, root)

    print(res)

if __name__ == '__main__':
    main()