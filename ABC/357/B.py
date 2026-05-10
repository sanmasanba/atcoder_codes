import re
def main():
    S = input()

    cnt_s = 0
    for s in S:
        if re.search(r'[a-z]', s):
            cnt_s += 1

    if cnt_s > len(S) // 2:
        print(str.lower(S))
    else:
        print(str.upper(S))

if __name__ == '__main__':
    main()