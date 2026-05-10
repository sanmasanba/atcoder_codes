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
    X = list(map(int, input().split(' ')))
    P = list(map(int, input().split(' ')))
    cumsumP = [0]
    for i in range(N):
        cumsumP.append(cumsumP[-1]+P[i])

    res = []
    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split(' '))
        left = bisect_left(X, l)
        right = bisect_right(X, r)
        tmp = cumsumP[right]-cumsumP[left]
        res.append(tmp)
    print(*res, sep='\n')

if __name__ == '__main__':
    main()