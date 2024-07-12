def main():
    H = int(input())

    i = 0
    h = 0
    while 1:
        h += 2 ** i
        if h > H:
            break
        i += 1
        
    print(i+1)

if __name__ == '__main__':
    main()