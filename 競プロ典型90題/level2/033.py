def main():
    H, W = map(int, (input().split(' ')))

    h = int(H//2) + int(H%2) 
    w = int(W//2) + int(W%2)

    if H == 1 or W == 1:
        print(H*W)    
    else:
        print(h*w)

if __name__ == '__main__':
    main()
