#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations, accumulate

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    potion_monster = defaultdict(deque)
    x_set = set()
    T = []
    potin_turn = []
    for i in range(N):
        t, x = map(int, input().split(' '))
        x_set.add(x)
        T.append(t)
        if t == 1:
            potin_turn.append(i)
        potion_monster[x].append((i, t))
    
    not_pick = set()
    res = 0
    for x in x_set:
        stack = []
        x_event = potion_monster[x]
        while x_event:
            i, t = x_event.popleft()
            match t:
                case 1:
                    stack.append(i)
                case 2:
                    if stack:
                        res += 1
                        stack.pop()
                    else:
                        print(-1)
                        return
        not_pick |= set(stack)
    
    # output
    res = 0
    have_potin = 0
    for i in range(N):
        t = T[i]
        if t == 1:
            if i not in not_pick:
                have_potin += 1
        else:
            have_potin -= 1
        res = max(res, have_potin)
    
    print(res)
    print(*list(1 if i not in not_pick else 0 for i in potin_turn), sep=' ')

if __name__ == '__main__':
    main()