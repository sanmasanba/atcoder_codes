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
    S = list(input())
    S.sort()
    
    res = 0
    for n in range(10**7):
        s = str(n**2)
        # 桁数が足りないとき達成不可
        if len(s) > N:
            break
        # 0埋めして、桁数を合わせたうえでリストが一致するか調べる
        s = sorted(list(s.zfill(N)))
        res += S == s
    
    # output
    print(res)

if __name__ == '__main__':
    main()