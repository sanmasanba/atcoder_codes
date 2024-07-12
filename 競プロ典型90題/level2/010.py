def main():
    N = int(input())
    A = [0] * (N+1) 
    B = [0] * (N+1) 
    for i in range(1, N+1):
        C, P = list(map(int, input().split(' ')))

        if C == 1:
                A[i] = A[i-1] + P
                B[i] = B[i-1]
        else:
            if i != 0:
                B[i] = B[i-1] + P
                A[i] = A[i-1]

    Q = int(input())
    LR = [list(map(int, input().split(' '))) for _ in range(Q)]
    for i in range(Q):
        L = LR[i][0]
        R = LR[i][1]
        print(f"{A[R] - A[L-1]} {B[R] - B[L-1]}")

if __name__ == '__main__':
    main()