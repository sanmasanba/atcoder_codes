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
MOD998 = 998244353
MOD1e7 = 1000000007

def decimal_to_base_P(n: int, b: int, K: int=0) -> str:
    """
    convert n to base b
    n: target
    b: base
    K: return value length
    """
    if n == 0:
        return '0'.zfill(K)
    res = []
    while n:
        res.append(int(n % b))
        n //= b
    return ''.join(str(x) for x in res[::-1]).zfill(K)


#main
def main():
    # intput
    A = int(input())
    N = int(input())
    
    seen = set()
    res = 0

    def check(_s: str):
        for i in range(len(_s)//2):
            if _s[i] != _s[-(i+1)]:
                return False
        return True
        
    for n in range(1, 10**6+10):
        tmp = str(n)
        a = ''.join([tmp, tmp[-1::-1]])
        int_a = int(a)
        b = ''.join([tmp, tmp[-2::-1]])
        int_b = int(b)
        if int_a <= N:
            if check(decimal_to_base_P(int_a, A)):
                res += int_a
        if int_b <= N:
            if check(decimal_to_base_P(int_b, A)):
                res += int_b
    print(res)        

if __name__ == '__main__':
    main()