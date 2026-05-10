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
    # 入力
    N = int(input())
    AB = [list(map(int, input().split(' '))) for _ in range(N)]
    AB.sort(key=lambda x: -x[1])

    # シミュレーション
    t = 0
    while AB:
        task_time, time_over = AB.pop()
        t += task_time
        if time_over < t:
            print('No')
            sys.exit(0)

    # 出力    
    print('Yes')

if __name__ == '__main__':
    main()