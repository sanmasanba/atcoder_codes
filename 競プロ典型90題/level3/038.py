import math 

def main():
    A, B = map(int, input().split(' '))

    res = 0
    if math.lcm(A, B) <= 1e18:
        res = math.lcm(A, B)
    else:
        res = 'Large'

    print(res)

if __name__ == '__main__':
    main()