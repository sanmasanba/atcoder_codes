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
    R = int(input())
    if 0 < R <= 99:
        print(100-R)
    elif 100 <= R < 200:
        print(200-R)
    elif 200 <= R < 300:
        print(300-R)

if __name__ == '__main__':
    main()