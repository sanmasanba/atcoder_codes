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
    Y = int(input())
    if Y%4 != 0:
        print("365")
    elif Y%4 == 0 and Y%100 != 0:
        print("366")
    elif Y%100 == 0 and Y%400 != 0:
        print("365")
    elif Y%400 == 0:
        print("366")

if __name__ == '__main__':
    main()