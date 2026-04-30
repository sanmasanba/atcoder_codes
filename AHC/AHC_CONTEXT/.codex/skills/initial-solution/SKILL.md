---
name: initial-solution
description: Use when building the first valid baseline solver for a heuristic contest problem before iterative score improvement.
metadata:
  short-description: Build a baseline solver
---

# 初期解

## 目的

- まず常に有効解を返すベースラインを作る。

## 手順

1. 入出力を実装する。
2. 単純な構築法で有効解を生成する。
3. 小ケースで妥当性確認する。
4. ベースラインのスコアと時間を記録する。

## 完了条件

- 全テストで形式違反がない。
- panic やクラッシュがない。
- 比較用ベースラインが残っている。
