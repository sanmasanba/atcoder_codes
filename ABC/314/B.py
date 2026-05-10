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
    N = int(input())
    C = []
    A = []
    for _ in range(N):
        c = int(input())
        a = list(map(int, input().split(' ')))
        C.append(c)
        A.append(set(a))
    X = int(input())
    res = {}
    for i in range(N):
        if X in A[i]:
            if C[i] not in res:
                res[C[i]] = []
            res[C[i]].append(i+1)
    if not res:
        print(0)
        print()
    else:
        min_k = INF
        min_list = None
        for k, v in res.items():
            if k < min_k:
                min_k = k
                min_list = v
        print(len(min_list))
        min_list.sort()
        print(*min_list)

if __name__ == '__main__':
    main()