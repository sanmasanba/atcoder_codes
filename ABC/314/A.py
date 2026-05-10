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
    S = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    print(f"3.{S[:N]}")

if __name__ == '__main__':
    main()