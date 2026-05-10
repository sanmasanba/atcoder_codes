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
    # input
    S, K = input().split(' ')
    S = list(S); K = int(K)

    # 順列全列挙
    str_set = set()
    for perm in permutations(S):
        str_set.add(''.join(list(perm)))
    ordered_list = sorted(list(str_set))

    # 出力
    print(ordered_list[K-1])

if __name__ == '__main__':
    main()