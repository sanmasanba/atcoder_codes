def main():
    N = int(input())
    A = list(map(int, input().split(' ')))

    res = 0
    for i in A:
        if i > 10:
            res += i - 10

    print(res)

if __name__ == '__main__':
    main()