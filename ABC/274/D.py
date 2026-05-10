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
    # input
    N, X, Y = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    x_move = []; y_move = []
    for i, a in enumerate(A):
        if i%2:
            y_move.append(a)
        else:
            if 0 < i:
                x_move.append(a)
    
    # split x and y
    x_pos = [set() for _ in range(len(x_move)+1)]
    y_pos = [set() for _ in range(len(y_move)+1)]
    x_pos[0].add(A[0])
    y_pos[0].add(0)
    for i, dx in enumerate(x_move):
        for x in x_pos[i]:
            x_pos[i+1].add(x+dx)
            x_pos[i+1].add(x-dx)
    for i, dy in enumerate(y_move):
        for y in y_pos[i]:
            y_pos[i+1].add(y+dy)
            y_pos[i+1].add(y-dy)

    # output
    res =  X in x_pos[-1] and Y in y_pos[-1]
    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()