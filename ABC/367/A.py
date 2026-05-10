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
    A, B, C = map(int, input().split(' '))
    if B > C:
        C += 24
        A += 24
    print('Yes' if not B <= A <= C else 'No')

if __name__ == '__main__':
    main()