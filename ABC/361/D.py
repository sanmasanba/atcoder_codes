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
    N = int(input()) + 2
    S = input() + ".."
    T = input() + ".."
    
    d = {S:0}
    q = deque([S])
    ans = -1
    while q:
        s = q.popleft()
        if s == T:
            ans = d[s]
            break
        # .の座標を探す
        empty = s.find(".")
        for i in range(N-1):
            # 石が２個連続した部分なら
            if "." not in s[i:i+2]:
                # strをlistに変換
                t = list(s)
                # .を連続した石に置き換えて 
                t[empty:empty+2] = t[i:i+2]
                # 置き換えた石を..にする
                t[i:i+2] = [".", "."]
                t = "".join(t)
                # まだ試したことがないなら追加
                if t not in d:
                    # 交換回数の記録
                    d[t] = d[s] + 1
                    # スタックに積む
                    q.append(t)

    print(ans)

if __name__ == '__main__':
    main()