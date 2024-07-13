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
    N = int(input())
    # 桁数を上限12桁としてrepunitを作る
    repunits = [1]
    for i in range(11):
        repunits.append(repunits[-1]*10+1)
    order = set()
    # 全列挙をする
    for a in repunits:
        for b in repunits:
            for c in repunits:
                order.add(a+b+c)
    # ソートしてN番目を求める
    res = list(order)
    res.sort()
    print(res[N-1])            

if __name__ == '__main__':
    main()