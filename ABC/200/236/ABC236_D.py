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

def solve(N: int, A: list):
    vec = []
    used = [False] * (2*N)

    def dfs():
        # 全ペアが確定したら計算
        if len(vec) == N:
            res = 0
            for p in vec:
                res ^= A[p[0]][p[1]]
            return res

        l = -1
        # 最小値を選択
        for i in range(2*N):
            if not used[i]:
                l = i
                break
        
        used[l] = True
        # 再帰的に、組み合わせを列挙
        res = 0
        for i in range(2*N):
            if not used[i]:
                vec.append((l, i))
                used[i] = True
                res = max(res, dfs())
                vec.pop()
                used[i] = False
        used[l] = False
        return res
    
    return dfs()

#main
def main():
    # intput
    N = int(input())
    A = [[0] * (2*N) for _ in range(2*N-1)]
    for i in range(2*N-1):
        tmp = list(map(int, input().split(' ')))
        for j in range(i+1, 2*N):
            A[i][j] = tmp[j-i-1]

    print(solve(N, A))

if __name__ == '__main__':
    main()