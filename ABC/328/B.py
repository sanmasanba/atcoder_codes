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
    D = list(map(int, input().split(' ')))
    
    res = 0
    for m in range(1, N+1):
        for d in range(1, D[m-1]+1):
            tmp_set = set(list(str(m)) + list(str(d)))
            if len(tmp_set) == 1:
                res += 1
    print(res)

if __name__ == '__main__':
    main()