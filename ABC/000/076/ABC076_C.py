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
    S = input()
    T = input()
    
    if len(S) < len(T):
        print('UNRESTORABLE')
        return
    
    for i in range(len(S)-1, len(T)-2, -1):
        if all([S[i-j] == T[-j-1] for j in range(len(T)) if S[i-j] != '?']):
            st = i-len(T)+1
            S = S.replace('?', 'a')
            S = list(S)
            for k in range(len(T)):
                S[st+k] = T[k]
            print(''.join(S))
            return

    print('UNRESTORABLE')

if __name__ == '__main__':
    main()