def prime_factorization(N):
    res = 0

    for p in range(2, N):
        #p**2がNを超えることはない
        if p * p > N:
            break

        #Nがpで割り切れないならスルー
        if N % p != 0:
            continue

        #今のpを何回かけているかを求める
        e = 0
        while N % p == 0:
            #カウントして
            e += 1
            #Nをpで割る
            N //= p 

        res += e
    
    if N != 1:
        res += 1
    
    return res
            
def main():
    N = int(input())

    res = prime_factorization(N)

    if res == 1:
        print('0')
    else:
        ans = 0
        #
        for i in range(21):
            if (1 << i) >= res:
                ans = i
                break
        print(ans)

if __name__ == '__main__':
    main()