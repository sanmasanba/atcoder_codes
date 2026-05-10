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
    A = list(map(int, input().split(' ')))

    # 長さ2までの数列は必ず等差数列
    res = 2*N-1
    r = 0
    l = 0
    # 長さ３以上の等差数列を探す
    while l < N-2:
        r  = l+1
        d = A[l+1] - A[l]
        while r+1 < N and d == A[r+1] - A[r]:
            r += 1
        if l-r == 1:
            continue
        t = r-l
        res += ((t-1)*t)//2
        l = r
    print(res)
        
if __name__ == '__main__':
    main()