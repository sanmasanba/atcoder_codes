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
    # 入力
    N = int(input())
    A = set(map(int, input().split(' ')))
    
    # 最小値で割り続けて、最小値が変わらなくなったら終わり
    res = min(A)
    while 1:
        target_set = set()
        for a in A:
            calc_a = a%res
            if calc_a != 0:
                target_set.add(a%res)
        # 全部が割り切れた時か、最小値が不変の時終了
        if not target_set or res == min(target_set):
            print(res)
            sys.exit(0)
        res = min(target_set)

if __name__ == '__main__':
    main()