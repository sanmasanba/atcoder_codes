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
def check(A):
        res = 0
        for a in A:
            if 0 < a:
                res += 1
        return res

#main
def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    
    res = 0
    while 1:
        A.sort(reverse=True)
        if 1 >= check(A):
            break
        A[0] -= 1
        A[1] -= 1
        res += 1
    print(res)

if __name__ == '__main__':
    main()