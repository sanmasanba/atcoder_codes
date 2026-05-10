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
    S, T = input().split(' ')
    
    res = 'No'
    for w in range(1, len(S)):
        for k in range(1, w+1):
            tmp = ""
            c = (w-k-1) % w
            while c < len(S):
                tmp += S[c]
                c += w
            if T == tmp:
                res = 'Yes'

    print(res)

if __name__ == '__main__':
    main()