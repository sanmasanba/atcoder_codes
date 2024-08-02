```python
@lru_cache
def LevenshteinDistance(s1:str, s2:str):
    # levenshtein距離を求める

    # もし片方が空文字からもう一方の長さが編集距離
    if not s1: return len(s2)
    if not s2: return len(s1)

    # もし一致するなら、次の文字から求める
    if s1[0] == s2[0]: return LevenshteinDistance(s1[1:], s2[1:])
    # 一致しないとき、
    l1 = LevenshteinDistance(s1, s2[1:])        # 追加 
    l2 = LevenshteinDistance(s1[1:], s2)        # 削除
    l3 = LevenshteinDistance(s1[1:], s2[1:])    # 置換
    return 1 + min(l1, l2, l3)
```

# 引用
1. 編集距離（レーベンシュタイン距離）を理解し、実装する
>https://qiita.com/tanuk1647/items/5a591da10e2ea5bedef6