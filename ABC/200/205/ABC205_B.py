def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    A.sort()

    flag = 'Yes'
    for i in range(N - 1):  
        if A[i+1] - A[i] != 1:
            flag = 'No'

    print(flag)

if __name__ == '__main__':
    main()