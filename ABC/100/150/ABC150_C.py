from itertools import permutations

def main():
    N = int(input())
    P = list(map(int, input().split(' ')))
    Q = list(map(int, input().split(' ')))

    sort_P = sorted(P)

    pos_P = 0
    pos_Q = 0
    for i, v in enumerate(permutations(sort_P)):
        if tuple(P) == v:
            pos_P += i
        if tuple(Q) == v:
            pos_Q += i

    print(abs(pos_P - pos_Q))

if __name__ == '__main__':
    main()