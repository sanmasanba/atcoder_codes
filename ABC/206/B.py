def main():
    N = int(input())
    day = 1
    S = 0
    while 1:
        S = day * (day + 1) / 2
        if S >= N:
            break
        day += 1

    print(day)

if __name__ == '__main__':
    main()