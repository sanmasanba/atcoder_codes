#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    name_score = {"tourist":3858, "ksun48":3679, "Benq":3658, "Um_nik":3648, "apiad":3638, "Stonefeang":3630, "ecnerwala":3613, "mnbvmar":3555, "newbiedmy":3516, "semiexp":3481}
    print(name_score[input()])
    
if __name__ == '__main__':
    main()