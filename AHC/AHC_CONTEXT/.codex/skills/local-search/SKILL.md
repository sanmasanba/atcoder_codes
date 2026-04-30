---
name: local-search
description: Use when improving an existing feasible solution with local search, neighborhood design, delta evaluation, acceptance rules, or restart strategies.
metadata:
  short-description: Local search improvement
---

# 局所探索

## 向いている状況

- 有効な初期解が作れる。
- 小さな変更でスコア改善が見込める。

## 設計チェック

- 近傍定義（1 手で何を変えるか）
- 差分評価
- 受理条件
- 多様化（再スタート、近傍混合）

## 計測

- 1 秒あたり改善量
- 受理率
- 反復回数
