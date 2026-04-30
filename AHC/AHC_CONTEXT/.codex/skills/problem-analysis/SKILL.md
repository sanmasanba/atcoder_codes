---
name: problem-analysis
description: Use when extracting constraints, score definition, valid-output conditions, and optimization targets from a heuristic contest problem statement before implementation.
metadata:
  short-description: Analyze the contest problem
---

# 問題分析

## 目的

- `task.html` からスコア定義と制約を正確に抽出する。
- 実装前に「何を最適化するか」を明文化する。

## 確認項目

- 入力サイズ、制約、制限時間
- 出力形式と不正解条件
- スコア式（最大化か最小化か）
- 有効解の条件

## 成果物

- 実装に渡せる要点メモ（5〜10 行）
- 失敗しやすいケースの一覧
