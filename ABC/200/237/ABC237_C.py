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
    S = input()
    N = len(S)
    
    # 文頭のaの数が文末のaの数より多いとき、回文にならない
    top_a, tail_a = 0, 0
    for i in range(N):
        if S[i] != 'a':
            top_a = i
            break
    for i in range(N):
        if S[-i-1] != 'a':
            tail_a = i
            break
    if top_a > tail_a:
        print("No")
        return 
    
    # 文頭、文末のaは無視できる
    s = S.strip('a')
    res = True
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            res = False
    print("Yes" if res else "No")

if __name__ == '__main__':
    main()