import sys

def main():
    N, T = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))

    H = [0 for j in range(N)]
    W = [0 for j in range(N)]
    RD = 0
    LD = 0

    for n, i in enumerate(A):
        H[int((i - 1)/N)] += 1
        W[int((i - 1)%N)] += 1
        if int((i - 1)/N) == int((i - 1)%N):
            RD += 1
        if int((i - 1)/N) + int((i - 1)%N) == N-1:
            LD += 1
        if H[int((i - 1)/N)]  == N or W[int((i - 1)%N)]  == N or RD == N or LD == N:
            print(n+1)
            sys.exit(0)
    print(-1)

if __name__ == '__main__':
    main()