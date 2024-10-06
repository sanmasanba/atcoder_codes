#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations
from string import ascii_uppercase

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    S = list(input())
    
    s2i = {c:i for i, c in enumerate(S)}

    res = 0
    pos = -1
    for c in ascii_uppercase:
        if c == 'A':
            pos = s2i[c]
        else:
            res += abs(pos-s2i[c])
            pos = s2i[c]
    print(res)

if __name__ == '__main__':
    main()