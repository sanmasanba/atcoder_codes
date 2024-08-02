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
    A.sort()
    
    res = 0
    tmp_res = 0
    right = 0
    # 尺取り法
    for left in range(N):
        # 一番左のプレゼントから+Mの座標まで
        while right < N and A[right]-A[left] < M:
            right += 1
            tmp_res += 1
        # 今の最大と比較
        res = max(res, tmp_res)

        # 左を進める前に左のプレゼントを取る
        tmp_res -= 1
        # 左と右が一致したら、右を進める
        right += 1 if left == right else 0
    print(res)

if __name__ == '__main__':
    main()