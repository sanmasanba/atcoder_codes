def main():
    N, P, Q = map(int, (input().split(' ')))
    A = list(map(int, input().split(' ')))

    ans = 0
    for a in range(N):
        for b in range(a):
            for c in range(b):
                for d in range(c):
                    for e in range(d):
                        if (((((A[a]*A[b])%P)*A[c]%P)*A[d]%P)*A[e]%P) == Q:
                            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
