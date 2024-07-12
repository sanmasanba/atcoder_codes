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
    H = list(map(int, input().split(' ')))
    
    res = -1
    for i in range(1, N):
        if H[0] < H[i]:
            res = i + 1
            break
    print(res)        

if __name__ == '__main__':
    main()