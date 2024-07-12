#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N = int(input())
    A = set(list(map(int, input().split(' '))))
    M = int(input())
    B = set(list(map(int, input().split(' '))))
    L = int(input())
    C = set(list(map(int, input().split(' '))))
    Q = int(input())
    X = list(map(int, input().split(' ')))
    
    res = set()
    for a in A:
        for b in B:
            for c in C:
                res.add(a+b+c)

    for x in X:
        print('Yes' if x in res else 'No')
        
if __name__ == '__main__':
    main()