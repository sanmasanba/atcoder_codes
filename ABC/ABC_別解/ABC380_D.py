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
    S = list(input())
    Q = int(input())
    K = list(map(lambda x: int(x)-1, input().split(' ')))
    N = len(S)

    for k in K:
        # 何ブロック目かと何文字目か
        blk = k//N
        pt = k%N

        # blkのpopcountが奇数なら反転
        if blk.bit_count()%2:
            print(S[pt].swapcase(), end=' ')
        else:
            print(S[pt], end=' ')

if __name__ == '__main__':
    main()