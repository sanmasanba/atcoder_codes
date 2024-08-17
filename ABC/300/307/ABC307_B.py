#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    S = [input() for _ in range(N)]
    res = 'No'
    for i, j in permutations([i for i in range(N)], 2):
        s = S[i] + S[j]
        f = 1
        for k in range(len(s)//2):
            if s[k] != s[len(s)-1-k]:
                f = 0
        if f:    
            res = 'Yes'
    print(res)

if __name__ == '__main__':
    main()