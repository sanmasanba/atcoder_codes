from itertools import combinations
def marge(N):
    res = 0
    for j in N:
        res = res | j
    return res

def main():
    N, M = map(int, input().split(' '))
    S = []
    for _ in range(N):
        tmp = str(input())
        tmp = tmp.translate(str.maketrans({'o':'1', 'x':'0'}))
        S.append(int(tmp, 2))
    res =0

    for i in range(1, N+1):
        for j in combinations(S, i):
            if marge(j) == int(bin(2**M - 1), 2) and res == 0:
                res = i
                break
            else:
                pass

    print(res)

if __name__ == '__main__':
    main()