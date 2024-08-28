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
    N, M = map(int, input().split(' '))
    N_set = set([i+1 for i in range(N)])
    A = []
    for _ in range(M):
        _ = int(input())
        A_set = set(map(int, input().split(' ')))
        A.append(A_set)

    #bit_search
    res = 0
    for bit in range(2**M):
        total_set = set()
        for i in range(M):
            # bitが立っている集合を足す
            if (bit >> i) & 1:
                total_set |= A[i]
        # N_setがtotal_setの下位集合なら+1
        if N_set <= total_set:
            res += 1  

    print(res)

if __name__ == '__main__':
    main()