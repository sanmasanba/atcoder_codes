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
    
    res = 0
    for i in range(1000001):
        k = i*i*i
        if k > N:
            break
        else:
            K = str(k)
            K_inv = K[::-1]
            if K == K_inv:
                res = k
    print(res)

if __name__ == '__main__':
    main()