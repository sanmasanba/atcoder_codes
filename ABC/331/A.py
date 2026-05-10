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
    M, D = map(int, input().split(' '))
    y, m, d = map(int, input().split(' '))
    
    res_d = (d+1)%D
    d_carry = floor(d/D)
    res_m = (m+d_carry)%M
    m_carry = floor((m+d_carry-1)/M)
    res_y = y+m_carry

    print(res_y, M if res_m == 0 else res_m, D if res_d == 0 else res_d)

if __name__ == '__main__':
    main()