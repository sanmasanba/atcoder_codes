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
    N, Q = map(int, input().split(' '))
    G = {i:set() for i in range(N)}
    nodes = defaultdict(int)
    nodes[0] = N

    res = []
    for _ in range(Q):
        input_ = list(map(lambda x: int(x)-1, input().split(' ')))
        match input_[0]:
            case 0:
                _, u, v = input_
                nodes[len(G[u])] -=1
                G[u].add(v)
                nodes[len(G[u])] += 1
                
                nodes[len(G[v])] -= 1
                G[v].add(u)
                nodes[len(G[v])] += 1
                
                res.append(nodes[0])
            case 1:
                _, v = input_
                nodes[len(G[v])] -= 1
                discard_nodes = G[v]
                G[v] = set()
                nodes[len(G[v])] += 1

                for u in discard_nodes:
                    nodes[len(G[u])] -= 1
                    G[u].discard(v)
                    nodes[len(G[u])] += 1
                res.append(nodes[0])

    print(*res, sep='\n')

if __name__ == '__main__':
    main()