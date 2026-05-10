def main():
    N, M = map(int, input().split(' '))
    Hs = list(map(int, input().split(' ')))

    res = 0
    sum_H = 0
    for i in range(N):
        if Hs[i] <= M:
            M -=Hs[i]
            res += 1
        else:
            break

    print(res)

if __name__ == '__main__':
    main()