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
    S = list(input())
    cnt = Counter(S)
    res = []
    for s, v in cnt.items():
        if v == 1:
            res.append(s)
    if len(res):
        print(res[0])
    else:
        print(-1)

if __name__ == '__main__':
    main()