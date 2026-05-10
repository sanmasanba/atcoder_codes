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
    N, Q = map(int, input().split(' '))
    # pos: number
    pos2num = {i:i+1 for i in range(N)}
    # number: pos
    num2pos = {i+1:i for i in range(N)}

    for _ in range(Q):
        l_num = int(input())
        # 処理する数字のposを調べる
        l_pos = num2pos[l_num]
        r_pos = l_pos + (-1 if l_pos == N-1 else 1)
        r_num = pos2num[r_pos]
        
        # posの入れ替え
        num2pos[l_num] = r_pos
        num2pos[r_num] = l_pos
        # ballの入れ替え
        pos2num[l_pos] = r_num
        pos2num[r_pos] = l_num
    for _, v in pos2num.items():
        print(v, end=' ')

if __name__ == '__main__':
    main()