#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    S = input()
    print('Yes' if 0 < int(S[3:]) < 350 and int(S[3:]) != 316 else 'No')

if __name__ == '__main__':
    main()