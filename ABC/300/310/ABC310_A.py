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
    N, P, Q = map(int, input().split(' '))
    D = list(map(int, input().split(' ')))
    print(min(P, min([Q+d for d in D])))

if __name__ == '__main__':
    main()