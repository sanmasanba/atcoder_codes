N, L = map(int, input().split(' '))
K = int(input())
A = list(map(int, input().split(' ')))

def check(x):
    num = 0
    cnt = 0

    for i in A:
        if i - cnt >= x:
            cnt = i
            num += 1

    if L - cnt >= x:
        num += 1 

    return num >= K+1

def main():
    low = -1
    high = L + 1

    while high - low > 1:
        mid = (low + high) // 2
        if check(mid):
            low = mid
        else:
            high = mid

    print(low)

if __name__ == '__main__':
    main() 