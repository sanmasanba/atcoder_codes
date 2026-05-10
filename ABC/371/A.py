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
    A = list(input().split(' '))
    
    if A[0] == '<' and A[2] == '<':
        print("B")
    elif A[0] == ">" and A[2] == ">":
        print('B')
    elif A[0] == ">" and A[2] == "<":
        if A[1] == "<":
            print('A')
        else:
            print("C")
    else:
        if A[1] == "<":
            print('C')
        else:
            print('A')

if __name__ == '__main__':
    main()