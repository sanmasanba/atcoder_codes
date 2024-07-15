#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, combinations_with_replacement

sys.setrecursionlimit(10**6)
INF = float('inf')

def check(S, queue:deque):
    res = False
    for s in S:
        if queue[-1] == int(s):
            q = queue.pop()
        if len(queue) == 0:
            res = True
            break
    return res

#main
def main():
    N = int(input())
    S = list(input())
    
    cnt = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                tmp = check(S, deque([k, j, i]))
                cnt += tmp
    print(cnt)
if __name__ == '__main__':
    main()