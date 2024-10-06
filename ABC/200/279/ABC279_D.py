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

def func(A, B, t):
    return A/sqrt(1+t)+B*t

#main
def main():
    # input
    A, B = map(int, input().split(' '))
    
    # 三分探索
    low = 0
    high = A/B
    while 2 < high - low:
        mid1 = (low*2+high)//3
        mid2 = (low+high*2)//3

        time_mid1 = func(A, B, mid1)
        time_mid2 = func(A, B, mid2)

        if time_mid1 > time_mid2:
            low = mid1
        else:
            high = mid2

    # output
    res = INF
    for t in range(int(low), int(high)+1):
        res = min(res, func(A, B, t))
    print(f"{res:.10f}")

if __name__ == '__main__':
    main()