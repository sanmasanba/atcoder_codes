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
    N, K = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    A_set = set(A)

    stack = [A[0]]
    not_use = -1
    if K%2:
        if K == 1:
            not_use = A[0]
        else:
            for i in range(1, K):
                if A[i-1]+1 == A[i]:
                    stack.append(A[i])
                else:
                    if len(stack)%2:
                        not_use = stack.pop()
                        break
                    stack = [A[i]]
        if not_use == -1 and len(stack)%2:
            not_use = stack[-1]

    socks = []
    for n in range(N):
        if n+1 == not_use:
            continue
        if n+1 in A_set:
            socks.append(n+1)
        else:
            socks.append(n+1)
            socks.append(n+1)

    res = 0
    for i in range((2*N-K)//2):
        res += abs(socks[2*i] - socks[2*i+1])
    print(res)

if __name__ == '__main__':
    main()