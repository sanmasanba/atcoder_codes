def main():
    N, M = map(int, input().split(' '))
    S = [set() for _ in range(N+1)]

    for i in range(M):
        a, b = map(int, input().split(' '))
        S[a].add(b)
        S[b].add(a)

    ans = 0
    for n in range(1, N+1):
        s = S[n]
        flag = 0
        for ele in s:
            if n > ele:
                flag += 1
        if flag == 1:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
