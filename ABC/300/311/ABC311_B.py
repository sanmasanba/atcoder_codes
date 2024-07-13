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
    N, D = map(int, input().split(' '))
    Ss = [input() for _ in range(N)]
    
    chc = {'o':0, 'x':1}
    res = ''
    for i in range(D):
        tmp = 0
        for j in range(N):
            tmp += chc[Ss[j][i]]
        res += str(1 if tmp else 0)
    
    # print(res)
    cnt_max = 0
    cnt = 0
    for i in res:
        if i == '0':
            cnt += 1
        else:
            cnt = 0
        cnt_max = max(cnt_max, cnt)
    print(cnt_max)

if __name__ == '__main__':
    main()