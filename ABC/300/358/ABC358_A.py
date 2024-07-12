import re

def main():
    S, T = input().split(' ')

    flag = 'No'
    if re.fullmatch(S, 'AtCoder') and re.fullmatch(T, 'Land'):
        flag = 'Yes'
    print(flag)

if __name__ == '__main__':
    main()