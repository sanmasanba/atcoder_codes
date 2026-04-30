# このリポジトリについて

- このリポジトリは AtCoder Heuristic Contest (AHC) 向けの作業テンプレートです。
- 問題文は `task.html` を参照します。

---

# 基本方針（最重要）

- 目的はスコア最大化（または最小化）です。
- 1 回の作業では 1 つの仮説だけを検証します。
- 変更は小さくし、必ずベンチマークで比較します。
- 出力形式違反、panic、クラッシュは即修正対象です。
- 結果と次アクションは `notes/next_action.md` に記録します。

---

# 実装原則

- 既存の入出力形式は変更しません。
- 評価関数、近傍、枝刈りの意図をコメントで残します。
- 定数・パラメータは 1 箇所に集約します。
- デバッグ出力は切り替え可能にします。
- 大規模リファクタは明示指示がある場合のみ行います。

---

# 作業フロー

1. 問題整理（制約・スコア方向・出力形式）
2. 現状 solver 把握（構造・ボトルネック）
3. 改善仮説の設定
4. 最小変更の実装
5. 同条件ベンチマーク
6. 記録と次アクション作成

---

# テストと tools の扱い

- `tools/` はコンテスト配布物を置く場所です。原則として中身を改変しません。
- 入力ケースは `tools/in/` を使います。
- solver の出力は `tools/out/` に保存し、ビジュアライザで確認します。
- 必要なら stderr を `tools/err/` に保存して調査します。

---

# KPI（評価指標）

- 主要指標は配布 runner の Average Score です。
- 比較時は同じ入力集合・同じ実行条件を使います。
- スコアの大小どちらが良いかは `task.html` を優先します。

---

# .agents/skills 参照

- 問題分析: `.agents/skills/problem-analysis.md`
- solver 設計: `.agents/skills/solver-design.md`
- 初期解: `.agents/skills/initial-solution.md`
- 局所探索: `.agents/skills/local-search.md`
- 焼きなまし: `.agents/skills/annealing.md`
- ビームサーチ: `.agents/skills/beam-search.md`
- デバッグ: `.agents/skills/debugging.md`
- プロファイリング: `.agents/skills/profiling.md`
- ベンチマーク: `.agents/skills/benchmarking.md`
- ふりかえり: `.agents/skills/postmortem.md`
