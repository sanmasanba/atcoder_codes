mod = 1000000007
pow10 = [0 for _ in range(22)]

#繰り返し2乗法
def pow(a, b, m):
    p, q = 1, a

    for i in range(30):
        if (b & (1 << i)) != 0:
            p *= q
            p %= m
        q *= q
        q %= m
    return p

def Div(a, b, m):
    return (a * pow(b, m-2, m)) % m

def init():
    pow10[0] = 1
    for i in range(1, 20):
        pow10[i] = (10 * pow10[i-1])

def sum_N(N):
    v1 = N % mod
    v2 = (N + 1) % mod
    v = v1 * v2 % mod
    return Div(v, 2, mod)

def main():
    init()
    L, R = map(int, input().split(' '))

    ans = 0
    for i in range(1, 20): 
        v_l = max(L, pow10[i-1])
        v_r = min(R, pow10[i] - 1)
        if v_l > v_r:
            continue  
        x = (sum_N(v_r) - sum_N(v_l - 1) + mod) % mod
        ans += i * x
        ans %= mod

    print(ans) 

if __name__ == '__main__':
    main()