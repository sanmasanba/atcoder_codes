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
    N = int(input())
    nums = list(map(int, input().split(' ')))
    
    # i個めまでの符号において、部分和がjとなるもの探す
    dp = [[0 for j in range(21)] for i in range(len(nums)-1)]
    dp[0][nums[0]] = 1
    for num in range(len(nums)-2):
        for p_sum in range(21):
            # 0 ≦ 部分和_k ± nums_k+1 ≦ 20でないなら0を代入
            tmp_add = dp[num][p_sum+nums[num+1]] if 0 <= p_sum+nums[num+1] <= 20 else 0
            tmp_dif = dp[num][p_sum-nums[num+1]] if 0 <= p_sum-nums[num+1] <= 20 else 0
            # 部分和がp_sumのなるのは、±nums[num+1]の個数を二つとも足す
            dp[num+1][p_sum] = tmp_add + tmp_dif

    print(dp[-1][nums[-1]])

if __name__ == '__main__':
    main()