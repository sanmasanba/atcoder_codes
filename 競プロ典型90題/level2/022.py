import math

def main():
    ABC = list(map(int, input().split(' ')))
    
    a = ABC[0]
    for i in range(2):
        b = ABC[i+1]
        a = math.gcd(a, b)

    print(sum(ABC)//a - 3)

if __name__ == '__main__':
    main()