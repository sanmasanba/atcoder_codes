# 実装例
```python
class UnionFind():
    """
    UnionFindの実装
    """
    # 初期化
    def __init__(self, n):
        # 要素の数
        self.n = n 
        # 各要素の親要素の番号を持つリスト
        # 要素が根の場合は、-(そのグループの要素数)
        self.parents = [-1] * n
    
    # 要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
        
    # 要素xが属するグループと要素yが属するグループを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # 要素xが属するグループのサイズを返す
    def size(self, x):
        return -self.parents[self.find(x)]

    # 要素xと要素yが同じグループに属するかを返す
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    # 根のリストを返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # グループの数を返す
    def group_count(self):
        return len(self.roots())

    # {根:[そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    
    # print()での表示
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
```
# 使える場面


# 実装の解説

# 引用
1. [PythonでのUnion-Find（素集合データ構造）の実装と使い方](https://note.nkmk.me/python-union-find/)
2. [Union find(素集合データ構造)](https://www.slideshare.net/slideshow/union-find-49066733/49066733)