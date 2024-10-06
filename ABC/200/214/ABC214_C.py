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
    # input
    N = int(input())
    S = list(map(int, input().split(' ')))
    T = list(map(int, input().split(' ')))
    
    # 時刻tを、先に記録
    get_time = [0] * (2*N)
    for i, t in enumerate(T):
        get_time[i] = t; get_time[i+N] = t

    # simurate
    for i in range(2*N-1):
        get_time[i+1] = min(get_time[i+1], get_time[i]+S[i%N])

    # output
    for i in range(N):
        print(min(get_time[i], get_time[i+N]))

if __name__ == '__main__':
    main()