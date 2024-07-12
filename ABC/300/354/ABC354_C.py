#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N = int(input())
    ac = []
    for i in range(N):
        tmp = tuple(map(int, (f"{input()} {i+1}").split(' ')))
        ac.append(tmp)
    ac.sort(key=lambda x: x[1])

    res_list = []
    res = 0
    max_a = 0
    for a, c, v in ac:
        if a > max_a:
            max_a = a
            res += 1
            res_list.append(v)

    res_list.sort()
    print(res)
    print(*res_list)        

if __name__ == '__main__':
    main()