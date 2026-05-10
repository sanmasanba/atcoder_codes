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
    h1, h2, h3, w1, w2, w3 = map(int, input().split(' '))
    
    res = 0
    for a in range(1, 29):
        for b in range(1, 29):
            for d in range(1, 29):
                for e in range(1, 29):
                    c = h1 - (a + b)
                    f = h2 - (d + e)
                    g = w1 - (a + d)
                    h = w2 - (b + e)
                    if c < 1 or f < 1 or g < 1 or h < 1:
                        continue
                    if h3 - (g + h) == w3 - (c + f) and w3 - (c + f) > 0 and h3 - (g + h) > 0:
                        res += 1

    print(res)

if __name__ == '__main__':
    main()