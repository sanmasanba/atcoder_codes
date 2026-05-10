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

def is_out_of_range(x:int, y:int, Xmi:int, Xma:int, Ymi:int, Yma:int) -> bool:
    return not (Xmi <= x < Xma and Ymi <= y < Yma)

#main
def main():
    # intput
    H, W = map(int, input().split(' '))
    A = [list(input()) for _ in range(H)]

    # 文字列の指定がないときはmove2dを消す
    move2d = {'^':0, 'v':1, '<':2, '>':3}
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    mp = [[-1]*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if A[h][w] == '#':
                mp[h][w] = INF
            elif A[h][w] == '.' or A[h][w] == 'S' or A[h][w] == 'G':
                if A[h][w] == 'S':
                    start = (h, w)
                elif A[h][w] == 'G':
                    goal = (h, w)
            else:
                mp[h][w] = INF
                cnt = 1
                dh, dw = d[move2d[A[h][w]]]
                while not is_out_of_range(h+dh*cnt, w+dw*cnt, 0, H, 0, W):
                    if A[h+dh*cnt][w+dw*cnt] == '.':
                        mp[h+dh*cnt][w+dw*cnt] = INF
                    else:
                        break
                    cnt += 1

    queue = deque()
    mp[start[0]][start[1]] = 0
    queue.append(start)
    while queue:
        h, w = queue.popleft()
        for dh, dw in d:
            nh = h+dh
            nw = w+dw
            if is_out_of_range(nh, nw, 0, H, 0, W):
                continue
            if mp[nh][nw] != -1:
                continue
            mp[nh][nw] = mp[h][w] + 1
            if A[nh][nw] == 'G':
                print(mp[nh][nw])
                return
            queue.append((nh, nw))
    print(-1)

if __name__ == '__main__':
    main()