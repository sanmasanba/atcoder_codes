---
name: solver-design
description: Use when structuring a heuristic contest solver into baseline generation, improvement phases, time control, and fallback behavior so it remains easy to iterate on.
metadata:
  short-description: Design solver structure
---

# solver 設計

## 目的

- 解法の全体構成を決め、改善可能な形で実装する。

## 設計項目

- 状態表現
- 初期解生成
- 改善フェーズ（探索手法）
- 時間管理
- 失敗時フォールバック

## 記録

- その設計を採用した理由
- 捨てた代替案と理由
