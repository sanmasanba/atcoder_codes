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

class RollingHash:
    """rolling hash
    Attributes:
        _MOD1 (int): 素数の法1
        _MOD2 (int): 素数の法2
        _BASE (int): hashの基数
    """
    _MOD1 = MOD1e7
    _MOD2 = MOD998
    _BASE = 1007
    def __init__(self, s:str):
        self.s = s
        self.n = len(s)
        self._hash1 = [0] * (self.n + 1)
        self._hash2 = [0] * (self.n + 1)
        self._pow1 = [1] * (self.n + 1)
        self._pow2 = [1] * (self.n + 1)
        self.generate_hash()
    
    def generate_hash(self):
        """hashの事前計算
        """
        for i in range(self.n):
            char_code = ord(self.s[i])
            # calc hash
            self._hash1[i+1] = (self._hash1[i] * self._BASE + char_code) % self._MOD1
            self._hash2[i+1] = (self._hash2[i] * self._BASE + char_code) % self._MOD2
            # calc pow
            self._pow1[i+1] = (self._pow1[i] * self._BASE) % self._MOD1
            self._pow2[i+1] = (self._pow2[i] * self._BASE) % self._MOD2
    
    def get_hash(self, l:int, r:int) -> Tuple[int, int]:
        """[l, r)のhashを獲得

        Args:
            l (int): 部分文字列の左端
            r (int): 部分文字列の右端

        Raises:
            ValueError: 範囲が不正

        Returns:
            Tuple[int, int]: 二つのハッシュのタプル
        """
        if not (0 <= l <= r <= self.n):
            raise ValueError('Invalid range for get_hash')
        # get hash
        h1 = self._hash1[r] - (self._hash1[l] * self._pow1[r-l]) % self._MOD1
        if h1 < 0: h1 += self._MOD1
        h2 = self._hash2[r] - (self._hash2[l] * self._pow2[r-l]) % self._MOD2
        if h2 < 0: h2 += self._MOD2

        return (h1, h2)

#main
def main():
    # intput
    S = input().strip()
    T = S[::-1]
    s_hash = RollingHash(S)
    t_hash = RollingHash(T)

    for i in range(len(S)):
        s_substr_hash = s_hash.get_hash(i, len(S))
        t_substr_hash = t_hash.get_hash(0, len(S)-i)

        if s_substr_hash == t_substr_hash:
            print(S + T[len(S)-i:])
            return
    print(S + S[::-1])

if __name__ == '__main__':
    main()