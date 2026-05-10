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

def solve(T):
    ope = 0
    for i in range(3):
        for j in range(3-i-1):
            if T[j] > T[j+1]:
                ope += 1
                T[j+1], T[j] = T[j], T[j+1]
    return ope

#main
def main():
    S = list(input().split(' '))
    T = list(input().split(' '))
    c2i = {c:i for i, c in enumerate(S)}
    
    MAX_ope = 10**18
    cnt = solve([c2i[t] for t in T])

    print('No' if (MAX_ope-cnt)%2 else 'Yes')

if __name__ == '__main__':
    main()