#library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998244353 = 998244353
MOD1000000007 = 1000000007

#main
def main():
    # intput
    N, Q = map(int, input().split())
    b2l = [i for i in range(N)]
    l2b = [i for i in range(N)]
    p2b = [i for i in range(N)]

    for _ in range(Q):
        input_ = input().strip()
        if input_[0] == '1':
            _, p, to = map(lambda x: (int(x)-1), input_.split())
            # labelに対応する巣に対して移動
            p2b[p] = l2b[to]
        elif input_[0] == '2':
            _, label0, label1 = map(lambda x: (int(x)-1), input_.split())
            # labelに対応する巣を入れ替える
            l2b[label0], l2b[label1] = l2b[label1], l2b[label0]
            # 巣に対応するlabelを入れ替える
            b2l[l2b[label0]], b2l[l2b[label1]] = b2l[l2b[label1]], b2l[l2b[label0]]
        elif input_[0] == '3':
            _, a = map(lambda x: (int(x)-1), input_.split())
            print(b2l[p2b[a]]+1)    

if __name__ == '__main__':
    main()