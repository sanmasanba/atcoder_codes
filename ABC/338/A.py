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
    print('Yes' if S[0] == S[0].upper() and S[1:] == S[1:].lower() else 'No')

if __name__ == '__main__':
    main()