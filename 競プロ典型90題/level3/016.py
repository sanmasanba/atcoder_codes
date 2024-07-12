import sys

def main():
    #input
    N = int(input())
    A, B, C = map(int, input().split(' '))

    #最大数を仮定
    res = 10000
    for x in range(10000):
        for y in range(10000):
            tmp = x*A + y*B
            if (N-tmp)%C != 0 or tmp > N:
                continue
            z = (N - tmp) // C
            #現在の最小値より小さいなら更新
            if res > x+y+z:
                res = x + y + z
    
    print(res)

if __name__ == '__main__':
    main()
