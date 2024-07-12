def main():
    AB = []
    N, K = map(int, input().split(' '))

    for i in range(N):
        a, b = map(int, input().split(' '))
        AB.append(b)
        AB.append(a-b)

    res = 0
    #最大値順にする
    AB.sort(reverse=True)
    #最大値から順に足す
    for i in range(K):
        res += AB[i]

    print(res)

if __name__ == '__main__':
    main()