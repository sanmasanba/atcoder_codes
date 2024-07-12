import time

def main():
    A, B, K = map(int, input().split(' '))
    x = 0
    for i in range(A):
        x += 2 ** i

    cnt = 0
    while 1:
        if x.bit_count() != A:
            pass
        else: 
            cnt += 1
            print('ok')
            if cnt == K:
                
                break
        x += 1

    print(x, cnt)
    x += cnt
    print(bin(x))

if __name__ == '__main__':
    main()