def main():
    A, B, C = map(int, input().split(' '))

    if A == B:
        print(C)
    elif B == C:
        print(A)
    elif C == A:
        print(B)
    else:
        print(0)

if __name__ == '__main__':
    main()