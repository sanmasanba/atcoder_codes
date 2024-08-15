#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    low = 1
    high = max(max(A), max(B))+1
    while low+1 <= high:
        x = (low+high)//2
        a_cnt = 0
        b_cnt = 0
        for i in range(max(N, M)):
            # 今の市場価格xが希望価格Aより高いなら販売する
            a_cnt += 1 if i < N and A[i] <= x else 0
            # 今の市場価格xが希望価格Bより安いなら購入する
            b_cnt += 1 if i < M and x <= B[i] else 0

        if a_cnt >= b_cnt:
            high = x
        else:
            low = x+1
    print(low)

if __name__ == '__main__':
    main()