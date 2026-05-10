#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

import time

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N, Q = map(int, input().split(' '))
    A, B = [], []
    for _ in range(Q):
        a, b = input().split(' ')
        A.append(int(a))
        B.append(b)
    
    pos = [[0, 0]]
    #[x, y]
    pre_pos = [0, 0]
    cnt = 0
    res = []
    for i in range(Q):
        if A[i] == 1:
            cnt += 1
            if B[i] == 'R':
                pair = zip(pre_pos, [1, 0])
                pre_pos = [a + b for a, b in pair]
            elif B[i] == 'L':
                pair = zip(pre_pos, [-1, 0])
                pre_pos = [a + b for a, b in pair]
            elif B[i] == 'U':
                pair = zip(pre_pos, [0, 1])
                pre_pos = [a + b for a, b in pair]
            else:
                pair = zip(pre_pos, [0, -1])
                pre_pos = [a + b for a, b in pair]
            pos.append(pre_pos)
        else:
            if int(B[i]) > cnt:
                res.append([int(B[i]) - cnt, 0])
            else:
                res.append([1 + pos[-int(B[i])][0], 0 + pos[-int(B[i])][1]])

    for x, y in res:
        print(x, y)

if __name__ == '__main__':
    main()