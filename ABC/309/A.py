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
    A, B = map(int, input().split(' '))
    print('Yes' if (A-1)//3 == (B-1)//3 and B-A == 1 else 'No')

if __name__ == '__main__':
    main()