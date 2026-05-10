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
    X = list(input())
    if X[-3] == "0" and X[-2] == "0" and X[-1] == "0":
        print("".join(X[:-4]))
    elif X[-2] == "0" and X[-1] == "0":
        print("".join(X[:-2]))
    elif X[-1] == "0":
        print("".join(X[:-1]))
    else:
        print("".join(X))

if __name__ == '__main__':
    main()