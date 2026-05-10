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
    res = ''
    while N >= 1:
        res += str(N%2)
        N //= 2
    
    cnt = 0
    for i in res:
        if i == '0':
            cnt+=1
        else:
            break
    print(cnt)

if __name__ == '__main__':
    main()