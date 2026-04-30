---
name: profiling
description: Use when measuring case-by-case runtime, identifying hot paths, and validating performance improvements in a heuristic contest solver.
metadata:
  short-description: Profile performance bottlenecks
---

# プロファイリング

## 目的

- 体感ではなく計測でボトルネックを特定する。

## 手順

1. ケース別実行時間を計測する。
2. ホットパスを特定する。
3. メモリ配置・割り当て・再計算を見直す。
4. 同条件で再計測し差分を確認する。
