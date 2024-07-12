def main():
    N = int(input())
    res = 'Yay!'
    if int(N * 1.08) == 206:
        res = 'so-so'
    elif 206 < int(N * 1.08):
        res = ':('
    print(res)

if __name__ == '__main__':
    main()