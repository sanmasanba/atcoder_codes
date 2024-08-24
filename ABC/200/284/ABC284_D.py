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
#prime_factorization
def solve(N) -> list:
    res = []
    p = 0
    for i in range(2, N):
        # 割れないときはスルー
        if N % i != 0:
            continue
        # 割れるときは一回割って、その数をqとする
        if N % i == 0:
            n = N // i
            p = i
            break
    # 最初に割れた素数がpならnでもう一度割れる
    if n%p == 0:
        return (p, n//p)
    #　qなら割ることができない
    else:
        return (int(sqrt(n)), p)

#main
def main():
    T = int(input())
    res = []
    for _ in range(T):
        tmp = int(input())
        res.append(solve(tmp))
    
    # p, qの順で出力
    for r in res:
        print(r[0], r[1])
    
if __name__ == '__main__':
    main()