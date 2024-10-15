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
    N = int(input())
    S = list(input())
    C = list(map(int, input().split(' ')))

    new_S = []
    for i in range(N):
        new_S.append((int(S[i])+i%2)%2)
    front_flip0 = [0] * (N+1)
    front_flip1 = [0] * (N+1)
    back_flip0 = [0] * (N+1)
    back_flip1 = [0] * (N+1)
    for i in range(N):
        if new_S[i]:
            front_flip0[i+1] = front_flip0[i]
            front_flip1[i+1] = front_flip1[i] + C[i]
        else:
            front_flip0[i+1] = front_flip0[i] + C[i]
            front_flip1[i+1] = front_flip1[i]
    for i in range(N-1, -1, -1):
        if new_S[i]:
            back_flip0[i] = back_flip0[i+1]
            back_flip1[i] = back_flip1[i+1] + C[i]
        else:
            back_flip0[i] = back_flip0[i+1] + C[i]
            back_flip1[i] = back_flip1[i+1]
    
    # 仕切りを動かして、返すコインを決める
    res = INF
    for partition in range(1, N):
        res = min(res, front_flip0[partition]+back_flip1[partition])
    for partition in range(1, N):
        res = min(res, front_flip1[partition]+back_flip0[partition])
    print(res)

if __name__ == '__main__':
    main()