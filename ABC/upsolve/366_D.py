# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

class cumsum3d:
    """
    3次元累積和
    """
    def __init__(self, A: List[int]):
        X = len(A)
        Y = len(A[0])
        Z = len(A[0][0])
        self.cumsum = [[[0]*(Z+1) for _ in range(Y+1)] for _ in range(X+1)]
        for x in range(X):
            for y in range(Y):
                for z in range(Z):
                    self.cumsum[x+1][y+1][z+1] = (
                        A[x][y][z]
                        + self.cumsum[x][y+1][z+1]
                        + self.cumsum[x+1][y][z+1]
                        + self.cumsum[x+1][y+1][z]
                        - self.cumsum[x][y][z+1]
                        - self.cumsum[x][y+1][z]
                        - self.cumsum[x+1][y][z]
                        + self.cumsum[x][y][z]
                    )
    
    def get(self, lx: int, rx: int, ly: int, ry: int, lz: int, rz: int) -> int:
        """
        (lx, ly, lz)と(rx, ry, rz)で囲まれた空間の累積を求める
        """
        return (
            self.cumsum[rx][ry][rz]
            - self.cumsum[lx][ry][rz]
            - self.cumsum[rx][ly][rz]
            - self.cumsum[rx][ry][lz]
            + self.cumsum[lx][ly][rz] 
            + self.cumsum[lx][ry][lz] 
            + self.cumsum[rx][ly][lz] 
            - self.cumsum[lx][ly][lz]
        )

# main
def main():
    # intput
    N = int(input())
    A = [[list(map(int, input().split())) for _ in range(N)] for _ in range(N)]
    
    c = cumsum3d(A)

    Q = int(input())
    for _ in range(Q):
        lx, rx, ly, ry, lz, rz = map(lambda x: int(x)-1, input().split())
        print(c.get(lx, rx+1, ly, ry+1, lz, rz+1))

if __name__ == '__main__':
    main()