def main():
    A, B = map(int, input().split(' '))

    kcal = A / 100 * B
    print(kcal)

if __name__ == '__main__':
    main()