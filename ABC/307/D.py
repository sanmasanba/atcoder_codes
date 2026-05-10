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
    N = int(input())
    S = deque(input())

    # stackとカウンター
    res = []
    cnt = 0
    while S:
        s = S.popleft()
        # 左かっこが来たら数える
        if s == '(':
            cnt += 1
            res.append(s)
        # 積んだ文字が')'の時、0 < cntなら'('まで削除する。そうでないときは積む。
        elif s == ')' and 0 <cnt:
            while 1:
                tmp_s = res.pop()
                if tmp_s == '(':
                    cnt -= 1
                    break
        else:
            res.append(s)
    print("".join(res))

if __name__ == '__main__':
    main()