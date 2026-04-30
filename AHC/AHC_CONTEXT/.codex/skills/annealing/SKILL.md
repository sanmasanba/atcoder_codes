---
name: annealing
description: Use when tuning or implementing simulated annealing for heuristic contest solvers, including temperature schedule, acceptance behavior, neighborhood mix, and runtime allocation.
metadata:
  short-description: Simulated annealing tuning
---

# 焼きなまし

## 主要パラメータ

- 初期温度
- 終了温度
- 冷却スケジュール
- 反復配分

## 調整順序

1. 温度スケール
2. 冷却率
3. 近傍の比率
4. ペナルティ係数

## ログ

- 温度推移
- 受理率
- ベスト更新時刻
