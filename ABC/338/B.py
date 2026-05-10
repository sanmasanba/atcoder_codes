#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from string import ascii_lowercase

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    S = Counter(list(input()))

    order = list(ascii_lowercase)
    res = ''
    cnt = 0
    for k ,v in zip(S.keys(), S.values()):
        if v >= cnt:
            if v == cnt: 
                tmp = min(order.index(res), order.index(k))
                res = order[tmp]
            else:
                res = k    
            cnt = v

    print(res)

if __name__ == '__main__':
    main()