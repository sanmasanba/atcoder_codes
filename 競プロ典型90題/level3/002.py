import itertools
def isvalid(S):
    #計算してスコアが０を下回ったとき
    #かっこで閉じられなくなってしまう→　不成立
    score = 0
    for c in S:
        if c == '(':
            score += 1
        else:
            score -= 1
        
        if score < 0:
            return False
    
    return score == 0

def main():
    #input
    N = int(input())

    #全探索
    for S in itertools.product(['(', ')'], repeat=N):
        #判定を行い条件を満たすものなら出力
        if isvalid(S):
            print(*S, sep='')

if __name__ == '__main__':
    main()
