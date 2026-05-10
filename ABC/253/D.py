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
    N, A, B = map(int, input().split(' '))
    res = (N*(N+1))//2
    # Nまでに出てくるA, B, A*Bの倍数の数を求める
    AB = lcm(A, B)
    Ai = N//A; Bi = N//B; ABi = N//(AB)
    # それぞれの倍数の総和を求める
    sumA = A*((Ai*(Ai+1))//2)
    sumB = B*((Bi*(Bi+1))//2)
    # ABは二回引かれるので足す
    sumAB = AB*((ABi*(ABi+1))//2)
    print(res-sumA-sumB+sumAB)

if __name__ == '__main__':
    main()