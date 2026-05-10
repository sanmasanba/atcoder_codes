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
    N, K, X = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    # 0円以上になるまで一旦使う
    for i in range(N):
        if K == 0:
            break
        use_coupon = min(A[i]//X, K)
        A[i] -= use_coupon*X
        K -= use_coupon
    # 大きい順でソート
    A.sort(reverse=True)

    # 残り枚数が0ならこれ以上減らせない
    if K == 0:
        print(sum(A))
    # 残り枚数が商品より多いなら、全部0円に
    elif K >= N:
        print(0)
    # 残り枚数分だけ、高いほうから0円に
    else:
        print(sum([max(0, A[i]-X) if i < K else A[i] for i in range(N)]))

if __name__ == '__main__':
    main()