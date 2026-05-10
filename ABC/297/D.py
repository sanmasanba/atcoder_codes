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
    A, B = map(int, input().split(' '))
    
    res = 0
    while 1:
        if A < B:
            A, B = B, A
        operates = A//B
        if A%B == 0:
            res += (operates-1)
            break
        A -= operates*B
        res += operates

    print(res)

if __name__ == '__main__':
    main()