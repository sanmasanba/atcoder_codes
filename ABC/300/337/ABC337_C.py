#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

def print_ans(res, n, N):
    if n not in res:
        return print('')
    else:
        print(res[n], end=' ')
        return print_ans(res, res[n], N)

#main
def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    res = {}
    for i, v in enumerate(A):
        res[v] = i+1
    
    print_ans(res, -1, N)

if __name__ == '__main__':
    main()