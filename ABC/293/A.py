#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    S = deque(input())
    res = ''
    while S:
        s1 = S.popleft()
        if S:
            s2 = S.popleft()
        else:
            s2 = ''
        res += s2 + s1
    print(res)

if __name__ == '__main__':
    main()