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
    S1 = input()
    S2 = input()
    S3 = input()

    if 10 < len(set(S1+S2+S3)):
        print('UNSOLVABLE')
        return
    
    c2i = {c:i for i, c in enumerate(set(S1+S2+S3))}
    n1_lower = 10**(len(S1)-1)
    n2_lower = 10**(len(S2)-1)
    n3_lower = 10**(len(S3)-1)
    for perm in permutations(range(10), len(c2i)):
        n1, n2, n3 = 0, 0, 0
        for length, c in enumerate(S1): n1 += 10**(len(S1)-1-length)*perm[c2i[c]]
        for length, c in enumerate(S2): n2 += 10**(len(S2)-1-length)*perm[c2i[c]]
        for length, c in enumerate(S3): n3 += 10**(len(S3)-1-length)*perm[c2i[c]]

        if n1 < n1_lower or n2 < n2_lower or n3 < n3_lower:
            continue
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return 
    print('UNSOLVABLE')

if __name__ == '__main__':
    main()