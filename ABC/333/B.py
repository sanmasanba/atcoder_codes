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
    S = list(input())
    T = list(input())
    st ="ABCDEABCDE"
    s_left = 0
    s_right = 0
    tmp = S[0]
    for i in range(10):
        if st[i] == tmp:
            s_left = i
            break
    tmp = S[1]
    for i in range(s_left, 10):
        if st[i] == tmp:
            s_right = i
            break
    t_left = 0
    t_right = 0
    tmp = T[0]
    for i in range(10):
        if st[i] == tmp:
            t_left = i
            break
    tmp = T[1]
    for i in range(t_left, 10):
        if st[i] == tmp:
            t_right = i
            break
    t_len = 1 if t_right-t_left==1 or t_right-t_left==4 else 2  
    s_len = 1 if s_right-s_left==1 or s_right-s_left==4 else 2 

    print('Yes' if t_len==s_len else 'No') 
      
if __name__ == '__main__':
    main()