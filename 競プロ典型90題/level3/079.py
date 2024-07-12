def main():
    H, W = map(int, input().split(' '))
    A = [list(map(int, input().split(' '))) for _ in range(H)]
    B = [list(map(int, input().split(' '))) for _ in range(H)]
    
    res_A, res_B = 0, 0
    res = 0

    for i in range(H-1):
        for j in range(W-1):
            diff = B[i][j] - A[i][j] 
            A[i][j] += diff
            A[i+1][j] += diff
            A[i][j+1] += diff
            A[i+1][j+1] += diff
            res += abs(diff)

    if A == B:
        print('Yes')
        print(res)
    else:
        print('No')

if __name__ == '__main__':
    main()