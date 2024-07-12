def main():
    N, K = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))

    diff = 0
    for i in range(N):
        diff += abs(A[i] - B[i])
    
    if (K -diff) % 2 == 0 and K >= diff:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
