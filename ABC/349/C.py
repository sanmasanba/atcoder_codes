#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
import copy

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    S = deque(list(input()))
    T = input()
    T_str = deque(list(copy.deepcopy(T)))
    N = len(S)

    code = ""
    while T_str:
        t = T_str.popleft()
        while S:
            s = S.popleft().upper()
            if s == t:
                code += t
                break
    if len(code) == 2: code += "X"
    print("Yes" if code == T else "No")

if __name__ == '__main__':
    main()