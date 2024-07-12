def main():
    H, W = map(int, input().split(' '))
    A = [0] * H #行方向の総和
    B = [0] * W #列方向の総和
    C = []
    for i in range(H):
        tmp = list(map(int, input().split(' ')))
        C.append(tmp)
        A[i] = sum(tmp)
        for j in range(W):
            B[j] += tmp[j]
            #print(B)

    for i in range(H):
        for j in range(W):
            print(A[i] + B[j] - C[i][j], end = ' ')
        print('')

if __name__ == '__main__':
    main()