#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, List, Tuple, Dict, TypeVar, Optional
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    if N <= 10:
        print(N-1)
        return
    
    order_list = [0]
    add = 9
    for i in range(1, 30):
        order_list.append(order_list[-1]+add)
        order_list.append(order_list[-1]+add)
        add *= 10

    order = bisect_left(order_list, N-1)
    res = order_list[order-1] + 1
    if order%2:
        res = 10**((order+2)//2-1) + N - res -1
        tmp = str(res)[::-1]
        print(res, tmp[1:], sep='')
    else:
        res = 10**(order//2-1) + N - res - 1
        tmp = str(res)[::-1]
        print(res, tmp, sep='')

if __name__ == '__main__':
    main()