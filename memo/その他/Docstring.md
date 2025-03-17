# 1.docstringとは

Pythonのコードの可読性を上げるために記述するコメントのこと。以下に例を示す。

```Python: docstring.py
call Sample:
    """
    サンプルコードのためのオブジェクト
    """
    def func(self, name: str, t: int):
        """
        Description

        Args:
            name (str): 車の名前
            t (int): 走行可能距離

        Returns:
            int: 返り値
        
        Raise:
            TypeError: 型が不一致の際に発生します

        """
```

# 2.記述ルール
docstringには、いくつかの記述ルールがあるがここではGoogle styleを参考にした記述方法を述べる。

## 2-1.基本ルール
- docstringは`class`、`def`、`module`に対して記述する。
- `"""`を用いて、コメントブロックを作成し記述する。

## 2-2.クラスの記述ルール
```Python: class.py
calss sample:
    """クラスの解説タイトル

        クラスについての説明

        Attributes:
            member1 int: descriptopn01
            method1 
    """
```
## 2-3.関数の記述ルール
```Python: def.py
def func(x: int, y: str):
    """関数の説明タイトル

        関数についての説明
    
    Args:
        x (int): xの説明
        y (str): yの説明
    
    Returns:
        int: 戻り値の説明
    """
```

## 2-4.セクションの解説
### Attributes   
クラスの属性の型、名前など、クラスの属性の説明を記載する。   
```Python
Attributes:
    属性名 (型): 属性の説明
    属性名 (型): 属性の説明
```
### Args   
引数の名前、型などを説明する。   
- selfは省略可能。
- 型の部分でoptionalを指定した引数は省略可能な引数。
```
Args:
    引数の名前 (引数の型): 引数の説明
    引数の名前 (引数の型, optional): 引数の説明
```
### Returns
関数の戻り値の型や説明を記載する。
```
Returns:
    戻り値の型: 戻り値の説明
```
### Yiled
Yiled文を利用した際の戻り値について記載する。
```
Yiled:
    戻り値の型: 戻り値の説明
```

### Raise
例外処理が発生した際の説明を記載する。
```
Raise:
    例外の名前: 例外の説明
```

### Examples
実際に利用した場合の例を記述する。
```
Examples:
    print("example")
    >> example
```

### Note
その他注意事項があれば記載する。
