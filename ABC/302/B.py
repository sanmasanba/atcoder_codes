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
def solver(S, h, w, H, W):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]
    target = 'snuke'
    for dh, dw in directions:
        res = []
        for i in range(5):
            nh, nw = h+dh*i, w+dw*i
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == target[i]:
                res.append((nh, nw))
            else:
                break
        if len(res) == 5:
            return res
    return None

#main
def main():
    H, W = map(int, input().split(' '))
    MAP = []
    for _ in range(H):
        MAP.append(input())
    
    for h in range(H):
        for w in range(W):
            res = solver(MAP, h, w, H, W)
            if res:
                for r in res:
                    print(r[0]+1, r[1]+1)
                return


if __name__ == '__main__':
    main()