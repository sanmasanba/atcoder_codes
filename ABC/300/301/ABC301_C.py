#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations
from string import ascii_lowercase

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    S = input()
    T = input()

    # 重複文字を管理
    s_set = {c:0 for c in ascii_lowercase}; s_set['@'] = 0
    t_set = {c:0 for c in ascii_lowercase}; t_set['@'] = 0

    # それぞれに登場する文字を記録
    for s, t in zip(S, T):
        s_set[s] += 1
        t_set[t] += 1

    res = True
    #
    for c in ascii_lowercase:
        # 'atcoder'以外の文字は最初から一致する必要がある
        if c not in 'atcoder' and s_set[c] != t_set[c]:
            res = False
        # 'atcoder'の文字なら、足りない分を補う
        if c in 'atcoder':
            if s_set[c] < t_set[c]:
                s_set['@'] -= (t_set[c] - s_set[c])
            elif s_set[c] > t_set[c]:
                t_set['@'] -= (s_set[c] - t_set[c])
    # '@'が負になった時、必要な枚数より'@'の数が足りない
    if t_set['@'] < 0 or s_set['@'] < 0:
        res = False
    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()