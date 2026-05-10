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
    X = list(map(int, input()))

    # 桁上がりした、 1 ... 1　なる数が最大
    res = int("1" * (len(X)+1))
    x = 0
    for i, a in enumerate(X[::-1]): x += a*10**i

    # 先頭に足す
    for p in range(10):
        a = X[0] + p
        if 9 < a:
            break
        # 公差
        for d in range(-9, 10):
            base = a
            tmp = f"{base}"
            for _ in X[1:]:
                base += d
                if 0 <= int(base) <= 9:
                    tmp += f"{base}"
                else:
                    break
            if x <= int(tmp):
                res = min(res, int(tmp))
    
    print(res)

if __name__ == '__main__':
    main()