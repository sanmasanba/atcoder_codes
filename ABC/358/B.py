def main():
    N, A = map(int, input().split(' '))
    T = list(map(int, input().split(' ')))

    res = [0]
    for i in range(N):
        if T[i] <= res[-1]:
            res.append(res[-1] + A)
        else:
            tmp = T[i] - res[-1]
            res.append(res[-1] + A + tmp)

    for i in res[1:]:
        print(i)

if __name__ == '__main__':
    main()