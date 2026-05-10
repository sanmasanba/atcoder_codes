#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

class Trains:
    def __init__(self, N):
        self.prev = [None] * N
        self.next = [None] * N

    def concat(self, x, y):
        # x
        self.next[x] = y
        # y
        self.prev[y] = x

    def separate(self, x, y):
        # x
        self.next[x] = None
        # y
        self.prev[y] = None

    def find(self, x):
        while 1:
            if self.prev[x] is None:
                return x
            x = self.prev[x]

#main
def main():
    # input
    N, Q = map(int, input().split(' '))
    trains = Trains(N)
    res = []
    for _ in range(Q):
        inline = input()
        match inline[0]:
            case '1':
                _, x, y = map(lambda x:int(x)-1, inline.split(' '))
                trains.concat(x, y)
            case '2':
                _, x, y = map(lambda x:int(x)-1, inline.split(' '))
                trains.separate(x, y)
            case '3':
                _, x = map(lambda x:int(x)-1, inline.split(' '))
                x = trains.find(x)
                tmp_res = []
                while 1:
                    tmp_res.append(x+1)
                    x = trains.next[x]
                    if x == None:
                        break
                res.append((len(tmp_res), tmp_res))
    
    # output
    for c, r in res:
        print(c, *r, sep=' ')

if __name__ == '__main__':
    main()