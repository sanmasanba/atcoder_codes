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
    N, X = map(int, input().split(' '))
    S = list(map(int, input().split()))
    S.sort()
    print(sum([s if s <= X else 0 for s in S]))

if __name__ == '__main__':
    main()