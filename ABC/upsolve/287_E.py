# library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict, namedtuple
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, NamedTuple, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998 = 998244353
MOD1e7 = 1000000007

class Node:
    def __init__(self):
        self.children = {}
        self.count = defaultdict(int)
        
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node.count[ch] += 1
            node = node.children[ch]

    def search(self, word: str) -> bool:
        node = self.root
        res = 0
        for ch in word:
            if node.count.get(ch) < 2:
                return res
            res += 1
            node = node.children[ch]
        return res

# main
def main():
    # intput
    N = int(input())
    trie = Trie()
    S = []
    for _ in range(N):
        tmp = input().strip()
        S.append(tmp)
        trie.insert(tmp)

    for s in S:
        print(trie.search(s))

if __name__ == '__main__':
    main()