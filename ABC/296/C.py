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
    N, X = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    A.sort()

    # 尺取り法
    right = 0
    res = False
    sum = A
    for left in range(N):
        while right+1 < N and abs(A[right] - A[left]) < abs(X):
            right += 1
        
        if abs(A[right] - A[left]) == abs(X):
            res = True
        
    print("Yes" if res else "No")

if __name__ == '__main__':
    main()