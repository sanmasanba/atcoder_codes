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
    H, W, N = map(int, input().split(' '))
    T = list(input())
    S = [list(input()) for _ in range(H)]
    
    move = []
    for j in range(N):
        i = N-1 - j 
        if T[i] == 'R':
            move.append([0, -1])
        elif T[i] == 'L':
            move.append([0 , 1])
        elif T[i] == 'U':
            move.append([1, 0])
        elif T[i == 'D']:
            move.append([-1, 0])

    res = 0
    for i in range(H):
        for j in range(W):
            # print([i, j], end=' ')
            if S[i][j] == '#':
                pass
            else:
                x, y, flag = 0, 0, True
                for m in move:
                    x += m[0]
                    y += m[1]
                    # print([i+x, j+y], end=' ')
                    if S[i+x][j+y] == '#':
                        flag = False
                        break
                if flag:
                    res += 1
            # print()
        # print()

    print(res)

if __name__ == '__main__':
    main()