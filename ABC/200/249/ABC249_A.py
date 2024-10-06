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
    A, B, C, D, E, F, X = map(int, input().split(' '))
    
    t_1set = A+C
    t_sets = X // t_1set
    a_1set = D+F
    a_sets = X // a_1set

    t_dist = B*(t_sets*A + min(A, X%t_1set))
    a_dist = E*(a_sets*D + min(D, X%a_1set))

    if t_dist < a_dist:
        print("Aoki")
    elif t_dist > a_dist:
        print("Takahashi")
    else:
        print("Draw")
    
if __name__ == '__main__':
    main()