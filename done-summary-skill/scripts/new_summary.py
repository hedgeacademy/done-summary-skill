#!/usr/bin/env python3
"""Create a blank Done Summary from a bundled language template."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
TEMPLATE_DIR = SKILL_DIR / "assets" / "templates"

LANGUAGE_ALIASES = {
    "zh": "zh",
    "cn": "zh",
    "chinese": "zh",
    "中文": "zh",
    "en": "en",
    "english": "en",
    "ar": "ar-sa",
    "ar-sa": "ar-sa",
    "arabic": "ar-sa",
    "saudi": "ar-sa",
    "ko": "ko",
    "kr": "ko",
    "korean": "ko",
    "한국어": "ko",
    "ja": "ja",
    "jp": "ja",
    "japanese": "ja",
    "日本語": "ja",
    "th": "th",
    "thai": "th",
    "ภาษาไทย": "th",
}


def normalize_language(value: str) -> str:
    key = value.strip().lower()
    if key not in LANGUAGE_ALIASES:
        supported = ", ".join(sorted(set(LANGUAGE_ALIASES.values())))
        raise SystemExit(f"Unsupported language '{value}'. Supported: {supported}")
    return LANGUAGE_ALIASES[key]


def template_path(language: str) -> Path:
    return TEMPLATE_DIR / f"done-summary.{language}.md"


def read_template(language: str) -> str:
    path = template_path(language)
    if not path.exists():
        raise SystemExit(f"Template not found: {path}")
    return path.read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a blank Done Summary from a bundled language template."
    )
    parser.add_argument(
        "--lang",
        default="en",
        help="Template language: en, zh, ar-sa, ko, ja, th. Aliases like chinese, arabic, korean, japanese, thai also work.",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Optional output Markdown path. If omitted, the template is printed to stdout.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List supported canonical language codes and exit.",
    )
    args = parser.parse_args()

    if args.list:
        print("en\nzh\nar-sa\nko\nja\nth")
        return 0

    language = normalize_language(args.lang)
    content = read_template(language)

    if args.output:
        output_path = Path(args.output).expanduser()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
        print(f"Wrote {output_path}")
    else:
        sys.stdout.write(content)
        if not content.endswith("\n"):
            sys.stdout.write("\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
