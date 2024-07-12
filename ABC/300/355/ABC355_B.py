def main():
    N, M = map(int, input().split(' '))
    A = [ [int(i), 0] for i in input().split(' ')]
    B = [ [int(i), 1] for i in input().split(' ')]
    C = A + B
    C.sort()

    res = 'No'
    for i in range(N+M-1):
        if C[i+1][1] == 0 and C[i][1] == 0:
            res = 'Yes'

    print(res)

if __name__ == '__main__':
    main()