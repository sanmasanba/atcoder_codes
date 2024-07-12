def main():
    #input
    N = int(input())
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    A.sort()
    B.sort()

    res = 0
    for i in range(N):
        res += abs(A[i] - B[i])        
    print(res)

if __name__ == '__main__':
    main()