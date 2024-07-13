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
    N, K = map(int, input().split(' '))
    A = set(list(map(int, input().split(' '))))
    
    socks = []
    for n in range(N):
        if n+1 in A:
            socks.append(n+1)
        else:
            socks.append(n+1)
            socks.append(n+1)
    # print(socks)
    res = 0
    if K%2==0:
        for i in range((2*N-K)//2):
            res += abs(socks[2*i] - socks[2*i+1])
    else:
        
            
    print(res)

if __name__ == '__main__':
    main()