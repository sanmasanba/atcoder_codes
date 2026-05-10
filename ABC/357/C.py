def check(i, j, N):
    if i // (3**(N-1)) % 3 == 1 and j // (3**(N-1)) % 3 == 1:
        return True
    
    if N > 0:
        return check(i, j, N - 1)
    else:
        return False

def main():
    N = int(input())
    
    for i in range(3**N):
        for j in range(3**N):
            if check(i, j, N):
                print('.', end='')
            else:
                print('#', end='')
        print('')

if __name__ == '__main__':
    main()