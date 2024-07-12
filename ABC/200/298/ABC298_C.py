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
    N = int(input())
    Q = int(input())
    Qs = [input().split(' ') for _ in range(Q)]
    
    #箱iに入っているカードのリスト
    b_C = {}
    #カードiが入っている箱リスト
    box = {}
    for q in Qs:
        if len(q) == 3:
            _, i, j = q[0], int(q[1]), int(q[2])
            if j not in b_C:
                b_C[j] = []
            b_C[j].append(i)

            if i not in box:
                box[i] = set()
            box[i].add(j)
        
        else:
            i, j = q[0], int(q[1])
            if i == '2':
                b_C[j].sort()
                print(*b_C[j])
            else:                
                print(*sorted(box[j]))

if __name__ == '__main__':
    main()