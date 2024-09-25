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
    S = list(input())
    
    # それぞれの数字の数を数える
    # 下三桁がわかればいいので、３ケタ以内に収める
    s_cnt = Counter(S)
    combi_s = []
    for k, v  in s_cnt.items():
        combi_s += [int(k)] * min(int(v), 3)
    
    # 下三桁が８の倍数か判定する
    res = False
    if len(combi_s) == 1:
        res |= combi_s[0]%8 == 0
    elif len(combi_s) == 2:
        for c in permutations(combi_s, 2):
            res |= int(''.join(list(map(str, c))))%8 == 0
    else:
        for c in permutations(combi_s, 3):
            res |= int(''.join(list(map(str, c))))%8 == 0
    
    # 出力
    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()