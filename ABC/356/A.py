def main():
    N, L ,R = map(int, input().split(' '))

    tmp1 = [i for i in range(1, N+1)]
    tmp2 = list(reversed(tmp1[L-1:R]))

    res = tmp1[:L-1] + tmp2 + tmp1[R:]
    for j in res:
        print(j, end=' ')

if __name__ == '__main__':
    main()