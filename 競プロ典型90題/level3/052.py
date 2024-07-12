def main():
    N= int(input())
    res = [1 for _ in range(6)]

    for _ in range(N):
        inputs = list(map(int, input().split(' ')))
        for i in range(6):
            res[i] = res[i] * sum(inputs)

    print(res[0] % 1000000007)

if __name__ == '__main__':
    main()