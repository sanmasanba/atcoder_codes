import math

def main():
    R, X, Y = map(int, input().split(' '))

    theta = math.atan(Y / X)
    L = math.sqrt(Y**2 + X**2)

    res = math.ceil(L / R)
    res += 1 if res == 1 and L < R else 0
    print(res)

if __name__ == '__main__':
    main()