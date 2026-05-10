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
    S = list(input())
    
    res = 'No'
    if N < 2:
        pass
    else:
        for i in range(N-1):
            if (S[i] == "a" and S[i+1] == "b") or (S[i+1] == "a" and S[i] == "b"):
                res = 'Yes'
    print(res)

if __name__ == '__main__':
    main()