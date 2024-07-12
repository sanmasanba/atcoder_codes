import re

def input_to_10(N):
    x = 0 
    input_to_10 = 0
    while N > 0:
            n = N % 10  #１の位を求める
            N //= 10    #1の位を消す
            input_to_10 += (8 ** x) * n  #10進数に戻す
            x += 1
    return input_to_10

def input_to_9(N):
    res = 0
    x = 1
    while N > 0:
        res += (N % 9) * x 
        N //= 9
        x *= 10
    return res
     
def main():
    N, K = map(int, input().split(' '))
    
    ans = 0
    for _ in range(K):
        ans = input_to_10(N)    #inputを10進法に
        print(ans)
        ans = input_to_9(ans)   #inputを9進法に
        print(ans)

        N = int(str(ans).replace('8', '5'))

    print(N)

if __name__ == '__main__':
    main()
