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
    S = list(input())
    
    # 移動方向
    move = {"R":(1, 0), "L":(-1, 0), "U":(0, 1), "D":(0, -1)}
    # 現在地
    now_pos = (0, 0)
    # 今までに行ったことある座標
    pos_set = set([(0, 0)])
    res = False
    for s in S:
        now_pos = (now_pos[0]+move[s][0], now_pos[1]+move[s][1])
        if now_pos in pos_set:
            res = True
        pos_set.add(now_pos)
    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()