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
def offset(start, S, current_pos):
    return (10**6)*(sqrt((start[0]-current_pos[0])**2 + (start[1]-current_pos[1])**2))

def move_length(start, end):
    return sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2)
#main
def main():
    # input
    N, S, T = map(int, input().split(' '))
    operates = []
    for _ in range(N):
        a, b, c, d = map(int, input().split(' '))
        operates.append(([a, b], [c, d]))
    
    res = INF
    for perm in permutations(operates):
        # dp_l:=左から刻印、dp_r:=右から刻印
        dp_l, dp_r = 0, 0
        # l_pos:=ひとつ前の左、r_pos:=ひとつ前の右
        l_pos, r_pos = [0, 0], [0, 0]
        for next_l, next_r in perm:
            # 移動量は固定
            move = (move_length(next_l, next_r)*(10**6))/T
            # 左から刻印
            rllr = offset(next_l, S, l_pos)/S # r(i-1) -> l(i-1) -> l(i) -> r(i)
            lrlr = offset(next_l, S, r_pos)/S # l(i-1) -> r(i-1) -> l(i) -> r(i)
            # 右から刻印
            rlrl = offset(next_r, S, l_pos)/S # r(i-1) -> l(i-1) -> r(i) -> l(i)
            lrrl = offset(next_r, S, r_pos)/S # l(i-1) -> r(i-1) -> r(i) -> l(i)
            # update
            new_dp_l = min(dp_r + rllr, dp_l + lrlr) + move
            new_dp_r = min(dp_l + lrrl, dp_r + rlrl) + move
            dp_l = new_dp_l
            dp_r = new_dp_r
            l_pos = next_l
            r_pos = next_r
        # update res
        res = min(res, min(dp_l, dp_r))
    
    # output
    print(res/(10**6))

if __name__ == '__main__':
    main()