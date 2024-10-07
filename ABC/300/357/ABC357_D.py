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
MOD = 998244353

#main
def main():
    N = int(input())
    order = len(str(N))

    # 等比数列の公式で考える
    x = pow(10, order, MOD)
    # 逆元
    inv = pow(x-1, MOD-2, MOD)
    res = N * (pow(x, N, MOD)-1)*inv
    print(res%MOD)

if __name__ == '__main__':
    main()