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
    S = deque(input())
    T = deque(input())
    
    s_l = 0
    t_l = 0
    res = []
    while S:
        s = S.popleft()
        while T:
            t = T.popleft()
            t_l += 1
            if s == t:
                res.append(t_l)
                break

    print(*res)

if __name__ == '__main__':
    main()