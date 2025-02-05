#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

seen = set()
def dfs(depth: int, group_cnt: int, N: int, A: List[int], 
        group_sums: List[int], xor_val: int):
    for i in range(group_cnt+1):
        # 袋depthをいずれかのグループに追加する
        xor_val ^= group_sums[i]
        group_sums[i] += A[depth]
        xor_val ^= group_sums[i]

        # 全ての袋を割り当てたら、計算結果を追加
        if depth == N-1:
            seen.add(xor_val)
        # 既存のグループに追加
        elif i < group_cnt:
            dfs(depth+1, group_cnt, N, A, group_sums, xor_val)
        # 新規のグループに追加
        else:
            dfs(depth+1, group_cnt+1, N, A, group_sums, xor_val)
        # 袋depthをグループiから取り除いておく
        xor_val ^= group_sums[i]
        group_sums[i] -= A[depth]
        xor_val ^= group_sums[i]

#main
def main():
    # intput
    N = int(input())
    A = list(map(int, input().split()))
    group_sums = [0]*N
    xor_val = 0
    dfs(0, 0, N, A, group_sums, xor_val)
    print(len(seen))

if __name__ == '__main__':
    main()