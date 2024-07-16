#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    M = int(input())
    target = [tuple(map(int, input().split(' '))) for _ in range(M)]
    N = int(input())
    stars = set([tuple(map(int, input().split(' '))) for _ in range(N)])
    
    m0 = target[0]
    for n in stars:
        flag = True
        for m in target[1:]:
            dx = m[0] - m0[0]
            dy = m[1] - m0[1]
            if (n[0] + dx, n[1] + dy) not in stars:
                flag = False
        if flag:
            res = n
            break
    print(res[0]-m0[0], res[1]-m0[1])

if __name__ == '__main__':
    main()