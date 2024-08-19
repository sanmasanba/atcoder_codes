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
    N = int(input())
    r = N%5
    if N%5 == 0:
        print(N)
    else:
        if r < 3:
            print(N-r)
        else:
            print(N+(5-r))

if __name__ == '__main__':
    main()