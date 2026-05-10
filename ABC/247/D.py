#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    Q = int(input())
    queue = deque()
    res = []
    for _ in range(Q):
        query = input().split(' ')
        if len(query) == 3:
            x, c = int(query[1]), int(query[2])
            queue.append([x, c])
        else:
            c = int(query[1])
            tmp = 0
            while c > 0:
                # ボールを取り出す
                push_balls = c if c <= queue[0][1] else queue[0][1]
                x = queue[0][0]
                # キューの調整
                queue[0][1] -= push_balls
                if queue[0][1] == 0:
                    queue.popleft()
                tmp += push_balls*x
                c -= push_balls
            res.append(tmp)
    for r in res:
        print(r)

    

if __name__ == '__main__':
    main()