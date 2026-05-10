def main():
    X = [0] * 100010

    N = int(input())
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    C = list(map(int, input().split(' ')))

    for i in C:
        index = B[i - 1]
        X[index] += 1
    
    res = 0

    for j in A:
        res += X[j]

    print(res)

if __name__ == '__main__':
    main()