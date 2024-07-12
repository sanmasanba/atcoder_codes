# itertools
itertoolsはpythonの標準ライブラリの一つで、イテレータを
提供してくれる。文字列も数値もどっちもける。

# 実装例と解説
## itertools.count
itertools.count(start, [,step]) -> itertor\
\
上限のないrange関数を提供してくれる。止める操作をしないと無限ループに陥るので注意。
```Python
for i in itertools.count(start=10, step=2):
    if i > 40:
        break 
    print(i, end=' ') 
    #10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 
```

## itertools.cycle
itertools.cycle(iterable) -> iterator
iterableな引数を先頭から順に出力してくれる。同じく無限ループに注意
```Python
count = 0
for i in itertools.cycle([5,4,3,2,1]):
    if count >= 10:
        break
    print(i, end=' ')
    count += 1 # -> 5 4 3 2 1 5 4 3 2 1
```

## itertools.repeat
itertools.repeat(element, [,n]) -> iterator\
elementをn回ぶん出力してくれる。nの指定がないと無限ループになる。
```Python
list(itertools.repeat("a", 5)) 
# -> ['a', 'a', 'a', 'a', 'a']

for i in itertools.repeat(1, 5):
    print(i, end=' ') 
    # -> 1 1 1 1 1
```

## itertools.accumulate
itertools.accumulate(p, [,func]) -> iterator\
デフォルトは累加関数で、funcを指定すればいろんな処理が可能
```Python
list(itertools.accumulate([1, 2, 3, 4, 5])) 
# -> [1, 3, 6, 10, 15]

for i in itertools.accumulate([1, 2, 3, 4, 5]):
    print(i, end=' ') 
    # -> 1 3 6 10 15

import operator
data = [5, 4, 3, 2, 1]
list(itertools.accumulate(data, operator.mul)) 
# -> [5, 20, 60, 120, 120]

list(itertools.accumulate(data, lambda x, y: x+2*y)) 
# -> [5, 13, 19, 23, 25]
```

## itertools.chain
itertools.chain(iterable1, iterable2, ...) -> iterator\
複数なiterablesを一つのイテレータにまとめることが出来る。
```Python
list(itertools.chain([1, 2, 3], (4, 5, 6))) 
# -> [1, 2, 3, 4, 5, 6]

list(itertools.chain(map(str, [1, 2, 3]), map(str, (4, 5, 6)), "aabc")) 
# -> ['1', '2', '3', '4', '5', '6', 'a', 'a', 'b', 'c']
```

## itertools.chain.from_iterrable
itertools.chain.from_iterable(iterable) -> iterator\
一個のiterableからchainのようなイテレータを作る
```Python
list(itertools.chain.from_iterable(["abc", (1, 2, 3)])) 
# -> ['a', 'b', 'c', 1, 2, 3]
```

## itertools.compress
itertools.compress(iterable, selectors) -> iterator\
iterableから要素を取り出すとき、selectorが真になるように取り出してくれる。selectorをフィルターみたいに使うことができる。
```Python
list(itertools.compress([1,2,3,4,5,6], [1,0,1])) 
# -> [1, 3]
```

## itertools.dropwhile
iterableの各要素に対して、predicateの評価値が偽になったら、その要素以降を返すイテレータを返してくれる。
```Python
dropwhile(lambda x: x<5, [1,4,6,4,1]) 
# -> 6 4 1

list(itertools.dropwhile(lambda x: x < "b", sorted(["a", "r", "e", "c", "d"])))
# -> ['c', 'd', 'e', 'r']
```

## itertools.filterfalse
filterが偽になるとき、predicateの要素を返してくれる。
```Python
list(itertools.filterfalse(lambda x: x % 2 == 0, range(10))) 
# -> [1, 3, 5, 7, 9]

list(filter(lambda x: x % 2 != 0, range(10))) 
# -> [1, 3, 5, 7, 9]
```

## itertools.groupby
itertools.groupby(iterable, [, key]) -> iterator\
SQLのgroubyと一緒
```Python
a = [("b", 3), ("a", 1), ("c", 2), ("a", 2), ("b", 1)]
a.sort(key=operator.itemgetter(0))
for (k, g) in itertools.groupby(a, key=operator.itemgetter(0)):
    print("key: {}".format(k), list(g))
# key: a [('a', 1), ('a', 2)]
# key: b [('b', 1), ('b', 3)]
# key: c [('c', 2)]

l = [1, 2, 3, 4, 6, 8]
grouped = itertools.groupby(l, key=lambda x: x%2)
for k, g in grouped:
    print(list(g))
# [1]
# [2]
# [3]
# [4, 6, 8]
```

## itertools.islice
itertools.islice(iterable, [,start], stop, [,step]) -> iterator\
iterableをスライスして、返してくれる。
```Python
list(itertools.islice('ABCDEFG', 2)) 
# -> ['A', 'B']

list(itertools.islice('ABCDEFG', 2, None)) 
# -> ['C', 'D', 'E', 'F', 'G']

list(itertools.islice(range(10000000), 12345, None, 1000000))
# [12345, 1012345, 2012345, 3012345, 4012345, 5012345, 6012345, 7012345, 8012345, 9012345]
```

## itertools.statmap
itertools.starmap(function, iterable) -> iterator\
iterableの各要素にfunstionを適用したiteratorを作ってくれる。
```Python
list(itertools.starmap(lambda x, y, z: (x - y)**z, [(1, 2, 2), (2, 0, 3), (3, 1, 4)]))
# -> [1, 8, 16]
```

## itertools.takewhile
itertools.takewhile(predicate, iterable) -> iterator\
iterableの各要素に対して、predicateの評価値が真になったら、その要素以降を出力し、偽になったら以降は無視するiteratorを作る。
```Python
list(itertools.takewhile(lambda x: x < "b", sorted(["a", "r", "e", "c", "d"]))) 
# -> ['a']

list(itertools.dropwhile(lambda x: x < "b", sorted(["a", "r", "e", "c", "d"]))) 
# -> ['c', 'd', 'e', 'r']
```

## itertools.tee
itertools.tee(iterable, n=2) -> n_iterators\
iterableから、n個のiteratorを作成する。
```Python
it1, it2, it3 = itertools.tee(range(5), 3)
list(it1) # -> [0, 1, 2, 3, 4]
next(it2) # -> 0
list(it2) # -> [1, 2, 3, 4]
tuple(it3) # -> (0, 1, 2, 3, 4)
```

## itertools.zip_longest
itertools.zip_longest(iterable1, iterable2, ..., fillvalue=None) -> iterator\
zipしたいiterableの長さが一致しないときに使う。\
fillvalueに指定した値で、足りないところを埋めてくれる。
```Python
for a, b, c in zip([1, 2], [3, 4], [5, 6]):
    print(a, b, c)
# 1 3 5
# 2 4 6

for a, b, c, d in itertools.zip_longest([1, 2], [3, 4, 7], [5], "6"):
    print(a, b, c, d)
# 1 3 5 6
# 2 4 None None
# None 7 None None

for a, b, c, d in itertools.zip_longest([1, 2], [3, 4, 7], [5], "6", fillvalue="?"):
    print(a, b, c, d)
# 1 3 5 6
# 2 4 ? ?
# ? 7 ? ?
```

## itertools.product
itertools.product(iterable1, ..., [,repeat=1]) -> iterator\
入力されたiterablesのデカルト積/直積を返すイテレータを作る。
重複を許す組み合わせを列挙するのに便利そう。
```Python
list(itertools.product("AB", repeat=3))
# [('A', 'A', 'A'),
#  ('A', 'A', 'B'),
#  ('A', 'B', 'A'),
#  ('A', 'B', 'B'),
#  ('B', 'A', 'A'),
#  ('B', 'A', 'B'),
#  ('B', 'B', 'A'),
#  ('B', 'B', 'B')]

list(itertools.product("ABC", "123"))
# [('A', '1'),
#  ('A', '2'),
#  ('A', '3'),
#  ('B', '1'),
#  ('B', '2'),
#  ('B', '3'),
#  ('C', '1'),
#  ('C', '2'),
#  ('C', '3')]
```

## itertools.permutation
iterableから順列を返す。rは順列の長さを指定できる。
```Python
list(itertools.permutations("ABC"))
# [('A', 'B', 'C'),
#  ('A', 'C', 'B'),
#  ('B', 'A', 'C'),
#  ('B', 'C', 'A'),
#  ('C', 'A', 'B'),
#  ('C', 'B', 'A')]

list(map(lambda x: int(x[0]) + int(x[1]), itertools.permutations("12345", 2)))
# ->[3, 4, 5, 6, 3, 5, 6, 7, 4, 5, 7, 8, 5, 6, 7, 9, 6, 7, 8, 9]
```

## itertools.combinations
itertools.combinations(iterable, r) -> iterator\
iterableから組み合わせを返すiteratorを作る。
```Python
combinations('ABCD', 2) 
# -> AB AC AD BC BD CD
```

## itertools.combinations_with_replacement
combinationsと違って、重複のある組み合わせの全列挙をしてくれる。
```Python
combinations_with_replacement('ABCD', 2) 
# -> AA AB AC AD BB BC BD CC CD DD
```
