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
    S = list(input())
    
    res = 0
    while S:
        if len(S) > 1:
            if S[-1] == "0" and S[-2] == "0":
                S.pop()
                S.pop()
            else:
                S.pop()
        else:
            S.pop()
        res += 1
    print(res)

if __name__ == '__main__':
    main()