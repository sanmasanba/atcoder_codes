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
    A = list(map(int, input().split(' ')))
    # それぞれの要素が登場する位置を調べる
    unique = {}
    for i, a in enumerate(A, start=1):
        if a not in unique:
            unique[a] = [0]
        unique[a].append(i)

    res = 0
    # それぞれの要素が含まれない連続部分列の総和を調べる
    for _, pos_list in unique.items():
        pos_list.append(N+1)
        cnt = (N*(N+1))//2
        for i in range(len(pos_list)-1):
            tmp = pos_list[i+1]-pos_list[i]-1
            if tmp:
                cnt -= (tmp*(tmp+1))//2
        res += cnt
    
    print(res)

if __name__ == '__main__':
    main()