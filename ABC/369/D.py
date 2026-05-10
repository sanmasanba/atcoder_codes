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
    A = list(map(int, input().split(' ')))

    # 奇数倒した時と偶数倒したときでdp
    dp_odd, dp_even = 0, -INF

    for a in A:
        # 偶数と倒しているとする
        tmp = dp_odd
        # 倒さないか、倒すかで遷移
        dp_odd = max(dp_even+2*a, dp_odd)
        dp_even = max(tmp + a, dp_even)

    print(max(dp_odd, dp_even))

if __name__ == '__main__':
    main()