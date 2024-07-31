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
    S = list(input())
    stack = []

    # スタックに積んでいき、末尾が'ABC'なら削除を繰り返す
    for s in S:
        stack.append(s)
        if 3 <= len(stack) :
            if stack[-3] == "A" and stack[-2] == "B" and stack[-1] == "C":
                for _ in range(3):
                    stack.pop()

    for s in stack:
        print(s, end='')    

if __name__ == '__main__':
    main()