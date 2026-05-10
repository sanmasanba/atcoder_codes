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
    # input
    N, M = map(int, input().split(' '))
    bit_N_length = len(bin(N)[2:])
    bit_M_length = len(bin(M)[2:])

    # 桁ごとの1の登場回数を数える
    res = [0] * bit_N_length
    for i in range(bit_N_length):
        bit_pattern = 2**(i+1)
        cnt1 = (N//bit_pattern)*(2**i)
        tmp_N = N % bit_pattern
        cnt2 = min(bit_pattern//2, max(0, tmp_N-bit_pattern//2+1))
        res[i] = cnt1+cnt2
    
    # Nで1が登場する桁のみ考える
    ans = 0
    for i in range(min(bit_M_length, bit_N_length)):
        if M >> i & 1:
            ans = (ans + res[i]) % MOD
    print(ans%MOD)  


if __name__ == '__main__':
    main()