import math 
import itertools

def main():
    #input
    N, M, K = map(int, input().split(' '))
    CAR = [list(input().split(' ')) for _ in range(M)]
    C, A, R = [], [], [] 

    #carを分ける
    for car in CAR:
        C.append(int(car[0]))
        A.append(list(map(int, car[1:-1])))
        R.append(car[-1])

    #全探索
    ans = 0
    #1 << N は 2 ** N　と同じ
    for mask in range(1 << N):
        ok = True
        for i in range(M):
            cnt = 0
            #条件と比較
            for a in A[i]:
                #maskのbitと鍵の番号を対応させて、鍵の数を調べる
                #例）mask == 001001、a = 3
                # mask >> 2 => 0010となり、最下位bitとの論理積は0
                cnt += (mask >> (a-1)) & 1
            ok &= (cnt >= K) == (R[i] == 'o')
        ans += ok

    print(ans)

if __name__ == '__main__':
    main()