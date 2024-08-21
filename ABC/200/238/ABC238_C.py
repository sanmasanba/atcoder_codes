#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
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
    res = 0

    # 桁数
    digit = len(str(N))
    # 桁数が少ないやつは全部足す
    for i in range(digit-1):
        n = int("9" + "0"*i)
        res += (n*(n+1))//2
        res %= MOD

    # 残りを足す
    under = int("9"*(digit-1) if 1 < digit else "0")
    num = N - under
    res += ((num+1)*num)//2
    print(res%MOD)

if __name__ == '__main__':
    main()