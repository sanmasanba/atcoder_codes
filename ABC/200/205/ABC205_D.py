import bisect

def main():
    #input
    N, Q = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    K = [int(input()) for _ in range(Q)] 

    #A[i]以下の有効な整数を数える
    #A_iまでの要素の数は、
    #(A_iまでの全整数の個数)-(A_i-1までに除外された数)
    low = [A[i] - (i+1) for i in range(N)]
    
    ANS = []
    for q in K:
        #lowリストに対してKの値を二分探索して、左側挿入点を返す
        idx = bisect.bisect_left(low, q)
        #分割点が一番後ろ(qはA[-1]よりも後ろ)
        if idx == N:
            ANS.append(A[N-1] + (q-low[N-1]))
        #そうじゃなかったら、A[i]とA[i-1]の間
        else:
            ANS.append(A[idx] - (low[idx] - q + 1))

    for ans in ANS:
        print(ans)

if __name__ == '__main__':
    main()