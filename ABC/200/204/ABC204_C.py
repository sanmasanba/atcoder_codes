import sys
sys.setrecursionlimit(10000)

def root(i, A, visited):
    #訪問済みなら無視する
    if visited[i]:
        return 0
    visited[i] = True
    
    #今いるノードが空(終端)なら１を返す
    if not A[i]:
        return 1
    
    #自分自身も含む
    cnt = 1
    for j in A[i]:
        cnt +=  root(j, A, visited)
    
    return cnt

def main():
    #input
    N, M = map(int, input().split(' '))
    A = [[] for _ in range(N + 10)]

    #あるノードに入ってくるルートを保存
    for _ in range(0, M):
        a, b = map(int, input().split(' '))
        A[b].append(a)
        
    
    res = 0
    for i in range(1, N + 1):
        #訪れたことがあるノードにフラッグを立てる
        visited = [False] * (N + 10)
        res = res + root(i, A, visited)

    print(res)
 
if __name__ == '__main__':
    main()