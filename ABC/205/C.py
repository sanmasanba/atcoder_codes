def main():
    A, B, C = map(int, input().split(' '))

    res = '='
    if C % 2 == 0:
        if abs(A) > abs(B):
            res = '>'
        if abs(A) < abs(B):
            res = '<'
    else:
        if A > B:
            res = '>'
        if A < B:
            res = '<'

    print(res)

if __name__ == '__main__':
    main()