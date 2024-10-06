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
    N, K = map(int, input().split(' '))
    c = list(map(int, input().split(' ')))
    
    candy_set = Counter(c[:K])
    res = len(candy_set)

    # N = Kのとき、全部食べられる
    if K == N:
        print(res)
        return
    
    # 先頭と終わりだけ管理
    for i in range(N-K):
        candy_set[c[i]] -= 1
        if candy_set[c[i]] == 0:
            candy_set.pop(c[i])
        if c[i+K] not in candy_set:
            candy_set[c[i+K]] = 0
        candy_set[c[i+K]] += 1
        res = max(res, len(candy_set))
    
    # 出力
    print(res)

if __name__ == '__main__':
    main()