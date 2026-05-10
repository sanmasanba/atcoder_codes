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

#main
def main():
    # intput
    N = int(input())
    G = [set() for _ in range(N)]
    degs = [0] * N
    for _ in range(N-1):
        a, b = map(lambda x: int(x)-1, input().split())
        G[a].add(b)
        G[b].add(a)
        # 各頂点の次数
        degs[a] += 1
        degs[b] += 1
    
    # 星の数がM個とする。
    # 開始時には次数1の頂点は、N-M個含まれる
    # 操作によって、次数1は次数2に頂点になるので、N-3M+2個
    # (両端は一つずつ頂点が減り、中間は2個ずつ減っていく->2M-2)
    M = (N + 2 - len([cnt for cnt in degs if cnt == 1]))//3

    # 操作後の次数に対して、大きいほうからM個を取れば開始前の状況
    # において、星の中央の次数を列挙できる
    degs.sort()
    print(*degs[-M:])

if __name__ == '__main__':
    main()