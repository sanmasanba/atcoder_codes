```Python
def scc(G: List[List[int]], H: List[List[int]], N: int):
    used = [False] * N
    I = []

    def dfs1(G: List[List[int]], v: int, used: List[bool], I: List[int]):
        used[v] = True
        for nextv in G[v]:
            if not used[nextv]:
                dfs1(G, nextv, used, I)
        I.append(v)

    for i in range(N):
        if not used[i]:
            dfs1(G, i, used, I)
    
    def dfs2(G: List[List[int]], v: int, used: List[bool], connected_nodes: List[int]):
        used[v] = True
        connected_nodes.append(v)
        for nextv in G[v]:
            if not used[nextv]:
                dfs2(G, nextv, used, connected_nodes)

    I.reverse()
    used = [False] * N
    res = []
    for i in I:
        if used[i]:
            continue
        connected_nodes = []
        dfs2(H, i, used, connected_nodes)
        res.append(connected_nodes)

    return res
```