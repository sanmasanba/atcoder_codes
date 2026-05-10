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
    H, W, K = map(int, input().split(' '))
    S = [input() for _ in range(H)]
    
    # "x"を含まないchunkを調べる
    chunks = set()
    for row in S:
        chunks = chunks | set(row.split('x'))
    for col in zip(*S):
        chunks = chunks | set(''.join(list(col)).split('x'))
    
    # 累積和で、最小手数を調べる
    res = INF
    for chunk in chunks:
        chunk_length = len(chunk)
        if chunk_length < K:
            continue
        partial_str = {'o': 0, '.': 0}
        for i in range(K):
            partial_str[chunk[i]] += 1
        for str_pos in range(chunk_length-K+1):
            res = min(res, K-partial_str['o'])
            if chunk_length <= str_pos+K:
                break
            partial_str[chunk[str_pos]] -= 1
            partial_str[chunk[str_pos+K]] += 1

    # output
    print(res if res != INF else -1)

if __name__ == '__main__':
    main()