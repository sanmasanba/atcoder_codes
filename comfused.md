# 整数
## MOD
### 互いに素な正の整数A、Bが与えられたときに、Nを法とすると、B, 2B, ..., (N-1)Bはすべて異なる。
A、Bが互いに素でないときの場合   
$ gcd(A, B) = g(\neq-1) $としたとき、D(N/g)は0に戻る。

    類題
    - ABC290.D - Marking

## 約数
### 約数の数は、素因数分解で   
Nの素因数分解が　$ N = p^{a}q^{b}...r^{c} $　のとき、　$ prime\_cnt = (a+1)(b+1)...(c+1) $　で個数を求めることができる。[wikipedia-約数](https://ja.wikipedia.org/wiki/%E7%B4%84%E6%95%B0)   

    類題
    - ABC383.D - 9 Divisors

# 階乗
### $ N! $を素数$p$で何回割れるかはルジャンドルの定理

```math
\sum^{\infty}_{i=1}{{\left\lfloor \frac{N}{p^i}\right\rfloor}} = {\left\lfloor \frac{N}{p^1}\right\rfloor}+ {\left\lfloor \frac{N}{p^2}\right\rfloor} + {\left\lfloor \frac{N}{p^3}\right\rfloor} + \dots
```
これを利用すれば、ある数で最大何回割ることができるかも求められる   
（例題）100!の末尾にはいくつの０が付くか   
すなわち、10で何回割れるかを求めればいいので、10=2*5より2で割り切れる回数か5で割り切れる回数のうち小さいほうが答え   
2の場合は
\begin(equa)
```math
\begin{align*}
\sum^{\infty}_{i=1}{{\left\lfloor \frac{100}{2^i}\right\rfloor}} &= {\left\lfloor \frac{100}{2^1}\right\rfloor}+{\left\lfloor \frac{N}{2^2}\right\rfloor} + {\left\lfloor \frac{100}{2^3}\right\rfloor} + \dots \\
&= 50 + 25 + 12 + 6 + 3 + 1 \\
&=  97
\end{align*}
```

となり、５の場合は

```math
\begin{align*}
\sum^{\infty}_{i=1}{{\left\lfloor \frac{100}{5^i}\right\rfloor}} &= {\left\lfloor \frac{100}{5^1}\right\rfloor} + {\left\lfloor \frac{N}{5^2}\right\rfloor} + {\left\lfloor \frac{100}{5^3}\right\rfloor} + \dots \\
&= 20 + 4 \\
&= 24
\end{align*}
```
となるため、答えは24個になる

# その他

## 括弧列
### '(' を 1，')' を -1 として上り下りを考える。   
前方から足していって、最後に総和が0になるときのみ括弧列が成立する。   
途中で０を下回ったら成立しない   

    類題
    - ABC312.D - Count Bracket Sequences

## 大小関係が与えられているときは、トポロジカル順序が役立つかも
DAGの各ノードをトポロジカル順序で並び変えたときに、あるノードがそのノードの出力辺の先のノードより前に来るように並べることを`トポロジカルソート`という。
そのときの順位並び順をトポロジカル順位という。   
大小関係が与えられているとき、それに基づいてDAGを構築しトポロジカルソートを行えば制約に反することなくソートができる。    
この時、どのタイミングでも次に選ぶ頂点(入次数が0)が一意であることが、トポロジカル順序が一意であることの必要十分条件になる。