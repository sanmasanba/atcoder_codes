#library
from itertools import permutations, combinations

def check(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

N, K = map(int, input().split(' '))
S = input()
P = ["".join(i) for i in permutations(S)]
P.sort()
res = 0
for i in range(len(P)):
    if i > 0 and P[i] == P[i-1]:
        continue
    flag = True
    for j in range(N-K+1):
        if check(P[i][j:j+K]):
            flag = False
            break
    res += flag    
print(res)
