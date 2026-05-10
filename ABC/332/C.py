#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split(' '))
    S = list(input().split('0'))

    w_t = M
    l_t = 0
    for i in S:
        s = list(i)
        s_cnt = Counter(s)
        l_t = max(l_t, s_cnt['2'])
        tmp_t = w_t + l_t - s_cnt['2']
        if tmp_t >= s_cnt['1']:
            pass
        else:
            l_t += s_cnt['1'] - tmp_t
    print(l_t)

if __name__ == '__main__':
    main()