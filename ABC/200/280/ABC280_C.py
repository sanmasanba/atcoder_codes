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
    S = list(input())
    T = list(input())
    

    res = -1
    for i in range(len(S)):
        if S[i] != T[i]:
            res = i+1
            break
    
    # 与えられた文字列Sが最後まで一致したら、最後の文字が答え
    print(res if res != -1 else len(T))

if __name__ == '__main__':
    main()