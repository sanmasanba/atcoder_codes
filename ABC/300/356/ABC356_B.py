def main():
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    Xs = [list(map(int, input().split(' '))) for _ in range(N)] 

    flag = 'Yes'
    for m in range(M):
        tmp = 0
        for n in range(N):
            tmp += Xs[n][m]
        if A[m] > tmp:
            flag = 'No'
        
    print(flag)

if __name__ == '__main__':
    main()