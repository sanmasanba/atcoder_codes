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
class Bisectlist:
    def __init__(self, L: List[int] = None) -> None:
        self.datas = dict()
        if L is None:
            self.datas[0] = [None, None]
            return
        
        self.datas[0] = [None, L[0]] 
        if len(L) == 1:
            self.datas[L[0]] = [0, None]
            return
        
        for i in range(len(L)):
            if i == 0: 
                self.datas[L[i]] = [0, L[i+1]]
            elif 0 < i < len(L)-1:
                self.datas[L[i]] = [L[i-1], L[i+1]]
            else:
                self.datas[L[i]] = [L[i-1], None] 

    def concat(self, x: int, y: int) -> None:
        _, z = self.datas[x]
        self.datas[y] = [x, z]
        self.datas[x][1] = y
        if z is not None:
            self.datas[z][0] = y
    
    def delete(self, x:int) -> None:
            y, z = self.datas[x]
            self.datas[y][1] = z
            if z is not None:
                self.datas[z][0] = y
            self.datas[x] = [None, None]

#main
def main():
    N = int(input())
    bisect_list = Bisectlist()
    A = list(map(int, input().split(' ')))
    Q = int(input())
    bisect_list = Bisectlist(A)
    for _ in range(Q):
        query = list(map(int, input().split(' ')))
        match query[0]:
            case 1:
                _ , x, y = query
                bisect_list.concat(x, y)
            case 2:
                _, x = query
                bisect_list.delete(x)

    res = 0
    while 1:
        res = bisect_list.datas[res][1]
        if res is None:
            return
        print(res, end=' ')

if __name__ == '__main__':
    main()