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
    ax, ay = map(int, input().split(' '))
    bx, by = map(int, input().split(' '))
    cx, cy = map(int, input().split(' '))
    dx, dy = map(int, input().split(' '))

    grad_ac = (cy-ay)/(cx-ax+1e-20)
    bias_ac = cy - grad_ac * cx
    grad_bd = (dy-by)/(dx-bx+1e-20)
    bias_bd = by - grad_bd * bx

    res = True
    if (cy < grad_bd*cx+bias_bd and ay < grad_bd*ax+bias_bd) or (grad_bd*cx+bias_bd < cy and grad_bd*ax+bias_bd < ay):
        res = False
    if (by < grad_ac*bx+bias_ac and dy < grad_ac*dx+bias_ac) or (grad_ac*bx+bias_ac < by and grad_ac*dx+bias_ac < dy):
        res = False
    
    print("Yes" if res else "No")

if __name__ == '__main__':
    main()