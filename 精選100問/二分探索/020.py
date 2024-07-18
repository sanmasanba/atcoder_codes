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
    N = int(input())
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    C = list(map(int, input().split(' ')))
    A.sort()
    B.sort()
    C.sort()

    # Bに関して、全探索する
    res = 0
    for b in B:
        # bより小さいものがAの候補なので[0, b) 
        a_pos = bisect_left(A, b)
        # bより大きいものがCの候補なので(b, 10**9]
        c_pos = bisect_right(C, b)
        # bを固定したときの組み合わせの数は、a_pos * 1 * (N-c_pos)
        res += a_pos * (N - c_pos)
    print(res)

if __name__ == '__main__':
    main()