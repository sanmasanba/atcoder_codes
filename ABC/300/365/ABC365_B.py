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
    tmp = list(map(int, input().split(' ')))
    A = []
    for i in range(N):
        A.append([tmp[i], i+1])
    A.sort()
    print(A[-2][1])

if __name__ == '__main__':
    main()