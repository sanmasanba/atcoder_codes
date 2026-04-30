---
name: debugging
description: Use when investigating invalid outputs, panics, crashes, major score drops, or runtime regressions in heuristic contest solvers.
metadata:
  short-description: Debug solver failures
---

# デバッグ

## 優先順位

1. 出力形式違反
2. panic / クラッシュ
3. 大幅スコア悪化
4. 実行時間悪化

## 手順

1. 再現入力を固定する。
2. 最小再現ケースに縮小する。
3. 診断ログを限定的に追加する。
4. 修正後にバッチ再検証する。
