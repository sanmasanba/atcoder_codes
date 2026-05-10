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
    N = int(input())
    H = deque(map(int, input().split(' ')))
    T = 0

    while H:
        h = H.popleft()
        # 3の倍数ターンにする
        if T%3 == 2 and T > 0:
            T += 1
            h -= 3
        elif T%3 == 1 and T > 0:
            T += 1
            h -= 1
            if h < 1:
                continue
            T += 1
            h -= 3
        # まだ残っているとき
        if h > 0:
            t = h//5
            T += t*3
            h -= t*5
            if h < 3:
                T += h
            else:
                T += 3
    print(T)

if __name__ == '__main__':
    main()