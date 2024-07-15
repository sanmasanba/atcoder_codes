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
    res = 0
    for n in range(1, N+1):
        tmp = 0
        if n%2:
            for j in range(1, n+1):
                if n%j == 0:
                    tmp += 1
            if tmp == 8:
                res += 1
    print(res) 

if __name__ == '__main__':
    main()