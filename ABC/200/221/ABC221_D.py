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
    A, B = map(list, zip(*[list(map(int, input().split(' '))) for _ in range(N)]))
    tmp = set()
    for i in range(N):
        login_start, login_end = A[i], A[i]+B[i]
        tmp.add(login_start)
        tmp.add(login_end)
    
    day2num = {d: i for i, d in enumerate(sorted(list(tmp)))}
    num2day = {i: d for d, i in day2num.items()}

    schedule = [0] * len(tmp)
    for i in range(N):
        login_start, login_end = A[i], A[i]+B[i]
        schedule[day2num[login_start]] += 1
        schedule[day2num[login_end]] -= 1
    schedule = list(accumulate(schedule))

    res = [0] * N
    for i in range(len(schedule)-1):
        login_nums = schedule[i]
        login_term = num2day[i+1] - num2day[i]
        if login_nums > 0: res[login_nums-1] += login_term
    print(*res)

if __name__ == '__main__':
    main()