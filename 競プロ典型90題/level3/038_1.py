import math

def main():
    A, B = map(int, input().split(' '))

    g = math.gcd(A, B)
    res = A//g * B

    if res > 1e18:
        res = 'Large'
    print(f"{res}")

if __name__ == '__main__':
    main()