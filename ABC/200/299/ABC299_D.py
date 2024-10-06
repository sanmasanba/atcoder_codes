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
    S = ['x']*N
    not_opened = set([i for i in range(1, N-1)])
    S[0] = '0'; S[-1] = '1'

    # 二分探索で範囲を減らしていく
    last_open = 0
    low = 0
    high = N-1
    while 1:
        # check
        is_top = (last_open == 0)
        is_end = (last_open == N-1)
        if not is_end and (S[last_open] != S[last_open+1]) and (S[last_open] != "x" and S[last_open+1] != "x"):
            print(f"! {last_open+1}", flush=True)
            sys.exit(0)
        if not is_top and (S[last_open] != S[last_open-1]) and (S[last_open] != "x" and S[last_open-1] != "x"):
            print(f"! {last_open}", flush=True)
            sys.exit(0)
        
        # input
        last_open = (high + low) // 2
        not_opened.discard(last_open)
        print(f"? {last_open+1}", flush=True)
        number = input()
        S[last_open] = number
        # 入力が1なら[0, ..., 1, ..., 1]となり、
        # 入力が1なら[0, ..., 0, ..., 1]となるので、
        # 徐々に範囲を狭くしていくことができる
        if number == '1':
            high = last_open
        else:
            low = last_open
        
if __name__ == '__main__':
    main()