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
    nums = []
    for n in range(1, 10):
        if N%n == 0:
            nums.append(n)
    for i in range(N+1): 
        tmp = []
        for j in nums:
            if i%(N//j) == 0:
                tmp.append(j)
        print(min(tmp) if tmp else '-', end='')

if __name__ == '__main__':
    main()