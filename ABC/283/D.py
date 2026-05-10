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
    S = list(input())
    N = len(S)

    stack = [[]]
    c_set = set()

    res = 'Yes'
    for i in S:
        if i == '(':
            stack.append([])
        elif i == ')':
            for c in stack[-1]:
                c_set.remove(c)
            stack.pop()
        else:
            if i in c_set:
                res = 'No'
                break
            else: 
                c_set.add(i)
                stack[-1].append(i)
    
    print(res)

if __name__ == '__main__':
    main()