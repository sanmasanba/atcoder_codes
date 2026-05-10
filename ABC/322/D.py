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

H, W = 4, 5

def preprocess():
    # ミノを90度回転
    def rotate(x):
        return [list(reversed(y)) for y in zip(*x)]
    
    # input
    tmp = []
    for _ in range(4):
        x = list(input().strip())
        if any(xx != '.' for xx in x):
            tmp.append(x)
    X = [list(x) for x in zip(*tmp) if any(xx != '.' for xx in x)]
    
    minos = []    
    for i in range(4):
        mino = 0
        for x in X:
            tmp = 0
            for xx in x:
                tmp += (1 if xx == '#' else 0)
                tmp <<= 1
            tmp >>= 1
            mino += tmp
            mino = (mino << W)
        mino >>= W
        minos.append(mino)
        X = rotate(X)
    return minos    

#main
def main():
    # intput
    X = [preprocess() for _ in range(3)]    
    # ミノの合計が16ではないとき、敷き詰められない
    if sum(x[0].bit_count() for x in X) != 16:
        print('No')
        return

    def solve(s: int, L):
        # 0ならOK
        if not s: return True
        
        # すべての位置で試す
        for i in range(s.bit_length()):
            for j in range(len(L)):
                # すべての回転を試す
                for x in X[L[j]]:
                    if (s >> i) & x == x and solve(s ^ (x << i), L[:j]+L[j+1:]):
                        return True
        return False
    
    grid = ((1 << H*W) - 1)//((1 << W) - 1)*((1 << W-1) - 1)    
    res = solve(grid, [0, 1, 2])
    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()