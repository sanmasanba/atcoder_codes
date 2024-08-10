#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations
import numpy as np

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    S = [list(input()) for _ in range(N)]

    max_len = max([len(s) for s in S])
    for i in range(N):
        S[i] += "*"*(max_len-len(S[i]))
    output_list = []
    for n in range(max_len):
        tmp = []
        for s in S[::-1]:
            tmp.append(s[n])    
        output_list.append(tmp)
    for s in output_list:
        for n in range(N):
            if s[n] == "*" and all(list(map(lambda x: x != "*", s[n:]))):
                print("*", end="")
            elif s[n] == "*" and all(list(map(lambda x: x == "*", s[n:]))):
                continue
            else:
                print(s[n], end="")
        print()

if __name__ == '__main__':
    main()