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
    s = input()
    S = re.split(r'[BDEFHIJKLMNOPQRSUVWYZ]+', s)
    print(max([len(x) for x in S]))

if __name__ == '__main__':
    main()