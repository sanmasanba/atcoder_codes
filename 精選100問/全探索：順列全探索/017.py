#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations
import copy

sys.setrecursionlimit(10**6)
INF = float('inf')

def check(Q):
    for q1, q2 in combinations(Q, 2):
        # 正方形である→縦と横の長さが等しい
        if abs(q1[0]-q2[0]) == abs(q1[1]-q2[1]):
            return False
    return True

#main
def main():
    K = int(input())
    q_set = set()
    for _ in range(K):
        a, b = map(int, input().split(' '))
        q_set.add((a, b))
    # 順列で、候補の位置を全列挙
    # この時、縦横は被らないので、順列をPとすると
    # 横の位置をi、縦の位置をP[i]に対応させることができる 
    P = permutations(range(8))
    
    # すべての順列を試す
    for p in P:
        q =set()
        # 候補位置を列挙
        for x, y in enumerate(p):
            q.add((x,y))
        # 候補位置がどれも制約を満たし、最初に置かれているクイーンが含まれる盤面
        if check(q) and all(map(lambda x: x in q, q_set)):
            break

    # 出力
    for i in range(8):
        for j in range(8):
            print("Q" if (i, j) in q else ".", end='')
        print()

if __name__ == '__main__':
    main()