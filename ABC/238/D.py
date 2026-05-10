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
    T = int(input())

    for _ in range(T):
        a, s = map(int, input().split(' '))
        N = max(a.bit_length(), s.bit_length())
        
        res = True
        buf = 0
        for i in range(N):
            # それぞれのi桁目
            ai = a >> i & 1
            si = s >> i & 1

            if not ai:
                # ai = 0の時、xi,yiの組み合わせは [01, 10, 00] 
                # xi + yi + buf = si より
                # 01) 0 + 1 + 1 = 0(10), 0 + 1 + 0 = 1(01)
                # 10) 1 + 0 + 1 = 0(10), 1 + 0 + 0 = 1(01)
                # 00) 0 + 0 + 1 = 1(01), 0 + 0 + 0 = 0(00) 
                # より、(buf and not si)なら桁上がりが起きる 
                if buf  and not si:
                    buf = 1
                else:
                    buf = 0
            else:
                # ai = 1の時、xi + yi + buf = siについて
                # 1) 1 + 1 + 0 = 0
                # 2) 1 + 1 + 1 = 0 -> 矛盾
                # 3) 1 + 1 + 0 = 1 -> 矛盾
                # 4) 1 + 1 + 1 = 1
                # -> 
                if buf ^ si:
                    res = False
                    break
                buf = 1

            # 最後の桁で桁上がりするのは矛盾
            if i == N-1 and buf:
                res = False

        print('Yes' if res else 'No') 

if __name__ == '__main__':
    main()