"""Validate the public, spoiler-free problem index and explanation templates."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INDEX = DOCS / "problems" / "index.md"
REQUIRED_HEADINGS = (
    "## 問題リンク",
    "## キーワード",
    "## 何に着目するか",
    "## 解法方針",
    "## tips",
    "## 典型・関連問題",
)
SPOILER_WORDS = ("二分探索", "DP", "動的計画法", "グラフ", "累積和", "UnionFind")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    index = INDEX.read_text(encoding="utf-8")
    for word in SPOILER_WORDS:
        if word in index:
            fail(f"問題一覧に典型ヒントが含まれています: {word}")

    rows = re.findall(
        r"\|\s*(\d{3})\s*\|\s*\[[^]]+\]\((https://atcoder\.jp/contests/abc\d+/tasks/abc\d+_[cdef])\)\s*\|\s*\[解説\]\((\d{3}\.md)\)\s*\|",
        index,
    )
    if not rows:
        fail("問題一覧の行を見つけられません")

    numbers = []
    for number, _url, filename in rows:
        numbers.append(number)
        if filename != f"{number}.md":
            fail(f"{number}: 解説ファイル名が通し番号と一致しません")
        page = DOCS / "problems" / filename
        if not page.is_file():
            fail(f"{number}: 解説ページがありません")
        text = page.read_text(encoding="utf-8")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                fail(f"{number}: 必須見出しがありません: {heading}")
        related_section = re.search(
            r"^## 典型・関連問題\s*$(.*?)(?=^## |\Z)",
            text,
            re.MULTILINE | re.DOTALL,
        )
        related_links = (
            re.findall(r"\[[^]]+\]\([^)]+\)", related_section.group(1))
            if related_section
            else []
        )
        if len(related_links) < 3:
            fail(f"{number}: 典型・関連問題を最低3つ列挙してください")
        if re.search(r"\]\((?:\./|\.\./)?\d{3}\.md\)", related_section.group(1)):
            fail(f"{number}: 関連問題にproblems内のMarkdownリンクは使用できません")

    expected = [f"{i:03}" for i in range(1, len(rows) + 1)]
    if numbers != expected:
        fail("問題番号は001から連番にしてください")
    print(f"validated {len(rows)} problems")


if __name__ == "__main__":
    main()
