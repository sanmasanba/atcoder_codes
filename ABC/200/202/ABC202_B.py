inverse = {'6':'9', '9':'6'}

def main():
    S = list(str(input()))

    for _ in range(len(S)):
        res = S.pop()
        if res == '6' or res == '9':
            print(inverse[res], end = '')
        else:
            print(res, end = '')

if __name__ == '__main__':
    main()