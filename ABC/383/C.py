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
    H, W, D = map(int, input().split(' '))
    S = [list(input()) for _ in range(H)]

    que = deque()
    mp =  [[INF]*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if S[h][w] == 'H':
                que.append((h, w))
                mp[h][w] = 0
    
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while que:
        h, w = que.popleft()
        if D < mp[h][w]+1:
            continue
        for dh, dw in d:
            nh = h + dh
            nw = w + dw
            if not (0 <= nh < H and 0 <= nw < W):
                continue
            if S[nh][nw] == '#' or S[nh][nw] == 'H':
                continue
            
            if mp[h][w]+1 < mp[nh][nw]:
                mp[nh][nw] = mp[h][w]+1
                que.append((nh, nw))

    for m in mp:
        print(*m, sep='\t')

    res = 0
    for h in range(H):
        for w in range(W):
            if mp[h][w] != INF:
                res += 1
    print(res)

if __name__ == '__main__':
    main()