#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    if sum(A) <= M:
        print('infinite')
    else:
        # binary search
        # 最大と最小の設定
        low = -1
        high = 10**10
    
        # 探索開始
        # lowとhighが一致するまで(一致した点が挿入する点)
        while low+1 < high:
        # 中間点の設定
            mid = (low + high) // 2

            tmp_sum = 0
            for a in A:
                tmp_sum += min(mid, a)
    
            if tmp_sum <= M:
                low = mid 
            else:
                high = mid
        print(low)

if __name__ == '__main__':
    main()