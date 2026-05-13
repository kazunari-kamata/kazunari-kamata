#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

SKIP_DIRS = {
    ".git",
    ".venv",
    "node_modules",
    "dist",
    "build",
    "__pycache__",
}

# 個人名や固有文字列を直接書かず、一般的なローカル絶対パスを検出する
POSIX_HOME_ROOTS = ("/" + "Users", "/" + "home")
MACOS_PRIVATE_VAR_ROOT = "/" + "private" + "/" + "var"
PATTERNS = [
    re.compile(rf"{root}/[A-Za-z0-9._-]+(?:/[^\s\)\"'`<>]*)?")
    for root in POSIX_HOME_ROOTS
] + [
    re.compile(rf"{MACOS_PRIVATE_VAR_ROOT}/[^\s\)\"'`<>]+"),
    re.compile(r"[A-Za-z]:\\\\Users\\\\[A-Za-z0-9._-]+(?:\\\\[^\s\)\"'`<>]*)?"),
]

TARGET_SUFFIXES = {
    ".md",
    ".txt",
    ".yml",
    ".yaml",
    ".json",
    ".toml",
    ".py",
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".html",
    ".css",
}

def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)

def is_target(path: Path) -> bool:
    return path.suffix.lower() in TARGET_SUFFIXES or path.name in {
        "AGENTS.md",
        "README.md",
    }

def main() -> int:
    found = False

    for path in Path(".").rglob("*"):
        if should_skip(path) or not path.is_file() or not is_target(path):
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for lineno, line in enumerate(text.splitlines(), start=1):
            for pattern in PATTERNS:
                if pattern.search(line):
                    print(f"{path}:{lineno}: local absolute path detected")
                    found = True

    if found:
        print("Local absolute paths were detected. Use repository-relative paths instead.")
        return 1

    print("OK: no local absolute paths detected.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
