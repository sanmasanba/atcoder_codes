#library
import time
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
    # input
    N = int(input())
    nums = []
    unique_nums = set()
    nums_cnt = defaultdict(int)
    for _ in range(N):
        s, c = map(int, input().split(' '))
        nums_cnt[s]+= c
        nums.append(s)
        unique_nums.add(s)
    heapq.heapify(nums)
    
    res = 0
    while nums:
        num = heapq.heappop(nums)
        cnt = nums_cnt[num]

        merge_num = 2 * num
        merge_cnt = cnt // 2

        res += cnt%2
        if cnt < 2:
            continue

        if merge_num not in unique_nums:
            heapq.heappush(nums, merge_num)
        nums_cnt[merge_num] += merge_cnt

    # output
    print(res)

if __name__ == '__main__':
    main()