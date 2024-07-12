from itertools import permutations

def list_c(keys, values):
    res = ''
    for key, value in zip(keys, values):
        res += str(key)*value
    return res

def main():
    MOD = 998244353 
    K = int(input())
    c = list(map(int, input(). split(' ')))
    C = {}
    for v, i in enumerate(c):
        if i > 0:
            C[v] = i

    res = 0
    for i in range(1, K+1):
        tmp_set = set()
        for j in permutations(list_c(C.keys(), C.values()), i):
            tmp_set.add(j)
        res += len(tmp_set) % MOD
    
    print(res % MOD)

if __name__ == '__main__':
    main()