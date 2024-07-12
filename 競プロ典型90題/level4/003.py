from collections import deque

INF = float('inf')

#最短距離を求める
def get_depth(start, N, G):
    #距離の初期化とキューの準備
    dist = [INF for i in range(N + 1)]
    Q = deque([start])
    #開始地点から自身への距離は０
    dist[start] = 0

    #Qの中に要素がある間ループする
    while Q:
        #Qを先頭から調べる
        pos = Q.popleft()
        #posが連結しているノードを調べる
        for to in G[pos]:
            #dist == INFはまだいっていないノード示している
            if dist[to] == INF:
                #たどりついたノードの前のノードまでの距離＋１が、
                #たどり着いたノードの長さ
                dist[to] = dist[pos] + 1
                #そのノード調べるリストに追加
                Q.append(to)
    return dist

def main():
    N = int(input())
    G = [[] for _ in range(N+1)]
    for _ in range(N-1):
            a, b = map(int, input().split(' '))
            G[a].append(b)
            G[b].append(a)

    #1番のノードからの、それぞれのノードまでの最短経路を求める
    dist = get_depth(1, N, G)
    maxn1 = -1
    maxid1 = -1

    #比較して、最大の最短経路長をもつノードを調べる
    for i in range(1, N+1):
        if maxn1 < dist[i]:
            maxn1 = dist[i]
            maxid1 = i
        
    #上で見つけたノードから、木の直径を求める
    dist = get_depth(maxid1, N, G)
    maxn2 = -1

    #最も長い経路を探す
    for i in range(1, N+1):
        maxn2 = max(maxn2, dist[i])

    print(maxn2 + 1)

if __name__ == '__main__':
    main()