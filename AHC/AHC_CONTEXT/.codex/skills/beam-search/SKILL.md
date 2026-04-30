---
name: beam-search
description: Use when designing or improving beam search for heuristic contest solvers, especially for state design, beam width tuning, pruning, duplicate removal, and sequential decision problems.
metadata:
  short-description: Beam search design
---

# ビームサーチ

## 向いている状況

- 意思決定が逐次的で順序依存が強い。
- 状態をキー化して重複排除できる。

## 主要パラメータ

- ビーム幅
- 展開数
- 枝刈り条件
- 同点時の優先規則

## 注意点

- 状態爆発の監視
- 重複状態の圧縮
- 幅を増やしたときの時間悪化
