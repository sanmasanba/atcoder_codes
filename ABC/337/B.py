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
    S = deque(list(input()))
    N = len(S)

    com = deque()
    pre = S[0]
    chc = {'A':0, 'B':1, 'C':2}
    for i in range(1, N):
        if pre == S[i]:
            pre = S[i]
        else:
            com.append(chc[pre])
            pre = S[i] 
    com.append(chc[pre])
    
    res = 'Yes'
    for i in range(len(com)-1):
        if com[i] > com[i+1]:
            res = 'No'
    print(res)

if __name__ == '__main__':
    main()