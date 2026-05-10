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

#main
def main():
    # input
    N = int(input())
    POS = [list(map(int, input().split(' '))) for _ in range(N)]
    
    # permutations
    magic_set = set()
    for i, j in permutations([i for i in range(N)], 2):
        current_town = POS[i]
        next_town = POS[j]
        dx = current_town[0]-next_town[0]
        dy = current_town[1]-next_town[1]
        magic = tuple(map(lambda x: x // gcd(dx, dy), [dx, dy]))
        magic_set.add(magic)
    
    # output
    print(len(magic_set))
    
if __name__ == '__main__':
    main()