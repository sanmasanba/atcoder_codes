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

def find_lefttop(l, H, W):
    for h in range(H):
        for w in range(W):
            if l[h][w] == '#':
                return (h, w)
    return None

def check(l1, l2, H1, W1, H2, W2, l1_lefttop, hx, wx):
    l1_lefttop_h, l1_lefttop_w = l1_lefttop
    dh, dw = hx- l1_lefttop_h, wx - l1_lefttop_w
    res = set()
    for h in range(H1):
        for w in range(W1):
            l2h = h + dh
            l2w = w + dw
            if 0 <= l2h < H2 and 0 <= l2w < W2:
                if l1[h][w] == '.':
                    continue
                elif l1[h][w] == '#' and l2[l2h][l2w] == '#':
                    res.add((l2h, l2w))
                elif l1[h][w] == '#' and l2[l2h][l2w] == '.':
                    return None
            else:
                if l1[h][w] == '#':
                    return None
    return res

#main
def main():
    # intput
    Ha, Wa = map(int, input().split(' '))
    A = [list(input()) for _ in range(Ha)]
    Hb, Wb = map(int, input().split(' '))
    B = [list(input()) for _ in range(Hb)]
    Hx, Wx = map(int, input().split(' '))
    X = [list(input()) for _ in range(Hx)]

    x_hash_pos = set([(h, w) for w in range(Wx) for h in range(Hx) if X[h][w] == '#'])

    a_lefttop = find_lefttop(A, Ha, Wa)
    b_lefttop = find_lefttop(B, Hb, Wb)
    A_pos = []
    B_pos = []
    for hx in range(Hx):
        for wx in range(Wx):
            if X[hx][wx] == '#':
                tmp = check(A, X, Ha, Wa, Hx, Wx, a_lefttop, hx, wx)
                if tmp:
                    A_pos.append(tmp)
    for hx in range(Hx):
        for wx in range(Wx):
            if X[hx][wx] == '#':
                tmp = check(B, X, Hb, Wb, Hx, Wx, b_lefttop, hx, wx)
                if tmp:
                    B_pos.append(tmp)
    
    if A_pos and B_pos:
        for a in A_pos:
            for b in B_pos:
                if x_hash_pos == (a | b):
                    print('Yes')
                    return
    print('No')


if __name__ == '__main__':
    main()