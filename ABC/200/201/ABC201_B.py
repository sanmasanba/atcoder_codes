#文字列とint型で返す
def catch(a):
    return str(a[0]), int(a[1])

def main():
    N = int(input())
    T2S = {} 
    S = [0]*N
    T = [0]*N

    for i in range(N):
        S[i], T[i] = catch(input().split(' '))
        T2S[T[i]] = S[i]
    T.sort()

    print(T2S[T[-2]])

if __name__ == '__main__':
    main()