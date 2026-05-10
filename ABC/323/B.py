#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    res = []
    for i in range(N):
        S = list(input())       
        tmp = 0
        for j in range(N):
            if S[j] == 'o':
                tmp += 1
        res.append([tmp, i+1])   
    res.sort(key=lambda x: (-x[0], [1]))
    for i in res:
        print(i[1], end=' ')

if __name__ == '__main__':
    main()