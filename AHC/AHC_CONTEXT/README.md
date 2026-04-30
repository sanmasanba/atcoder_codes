# AHC Context Template

AHC の問題を効率よく解くためのテンプレート集です。

## 構成

- `AGENT.md`: 実装・評価の基本方針
- `.agents/skills/`: 作業フェーズ別の実践ガイド
- `templates/`: 依頼文・記録文の雛形
- `notes/`: 次アクションと学びの蓄積
- `tools/`: コンテスト配布の tester / visualizer / 入力データ置き場

※ このリポジトリ内の `.agents/skills/` は運用ドキュメントです。Codex の `/skills` 一覧は、セッションが読み込んだ別のスキル登録先を表示する場合があります。

## tools の前提

- テストケースは `tools/in/` を使用します。
- solver 出力は `tools/out/` に保存します。
- `tools/out/` の出力をビジュアライザで可視化します。
