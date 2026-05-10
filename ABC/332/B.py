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
    K, G, M = map(int, input().split(' '))
    
    g, m = 0, 0
    for k in range(K):
        if g == G:
            g = 0
        elif g < G and m == 0:
            m = M
        else:
            tmp = G - g
            tmp = min(tmp, m)
            g += tmp
            m -= tmp
    print(g, m)    

if __name__ == '__main__':
    main()