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
    M = int(input())
    
    res = []
    while 0 < M:
        i = 0
        while i < 11:
            if M-3**(i+1) > 0:
                i += 1
            else:
                break
        M -= 3**i
        res.append(i)
    ans = []
    for i in range(11):
        cnt = 0
        for a in res:
            if a == i:
                cnt += 1
        if cnt < 3:
            ans += [i]*cnt
        else:
            tmp = [i+1]*(cnt//3)
            ans += tmp + [i]*(cnt%3)

    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()