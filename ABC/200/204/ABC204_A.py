def main():
    x, y = map(int, input().split(' '))

    if x != y:
        if x == 0:
            if y == 1:
                print(2)
            else:
                print(1)
        if x == 1:
            if y == 0:
                print(2)
            else:
                print(0)
        if x == 2:
            if y == 0:
                print(1)
            else:
                print(0)
    else:
        print(x)

if __name__ == '__main__':
    main()