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
    
    res = 'No'
    s = S.popleft()
    if s == '<':
        while S:
            s = S.popleft()
            if s == '=':
                pass
            else:
                break
        if len(S) == 0 and s == '>':
            res = 'Yes'
        else:
            pass
    else:
        pass
    print(res)

if __name__ == '__main__':
    main()