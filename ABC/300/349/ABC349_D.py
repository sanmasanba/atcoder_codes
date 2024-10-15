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
    L, R = map(int, input().split(' '))
    
    res = []
    while L != R:
        i = 0; j = 0
        if 0 < L:
            while L%2 == 0:
                i += 1
                L //= 2
            j = L
        else:
            i = 61; j = 0

        while 1:
            if (2**i)*(j+1) <= R:
                break
            i -= 1
            j *= 2
        res.append([(2**i)*(j), (2**i)*(j+1)])
        L = (2**i)*(j+1)

    print(len(res))
    for r in res:
        print(*r)

if __name__ == '__main__':
    main()