def root(i, A, visited):
    if visited[i]:
        return 0
    visited[i] = True

    if not A[i]:  # A[i] が空リストの場合
        return 1
    
    count = 1  # 自分自身を含める
    for j in A[i]:
        count += root(j, A, visited)
    
    return count

def main():
    N, M = map(int, input().split(' '))
    A = [[] for _ in range(N + 10)]

    # 1-indexed
    for _ in range(0, M):
        a, b = map(int, input().split(' '))
        A[b].append(a)
        
    res = 0
    for i in range(1, N + 1):
        visited = [False] * (N + 10)
        res += root(i, A, visited)

    print(res)

if __name__ == '__main__':
    main()
