#!/usr/bin/env python3
"""Generate doc/SCOPE_ISSUE.md from template + metadata (for GitHub issue regeneration)."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
META_PATH = REPO_ROOT / "doc" / "scope-issue.meta.yaml"
TEMPLATE_PATH = REPO_ROOT / "doc" / "templates" / "scope-issue.en.md"
OUT_PATH = REPO_ROOT / "doc" / "SCOPE_ISSUE.md"


def load_meta() -> dict:
    meta: dict = {"labels": ["enhancement"]}
    in_labels = False
    label_list: list[str] = []
    for line in META_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("issue_number:"):
            meta["issue_number"] = int(line.split(":", 1)[1].strip())
            in_labels = False
        elif line.startswith("upstream_repo:"):
            meta["upstream_repo"] = line.split(":", 1)[1].strip()
            in_labels = False
        elif line.startswith("title:"):
            raw = line.split(":", 1)[1].strip()
            meta["title"] = raw.strip('"').strip("'")
            in_labels = False
        elif line.startswith("labels:"):
            in_labels = True
            label_list = []
        elif in_labels and line.startswith("- "):
            label_list.append(line[2:].strip())
    if label_list:
        meta["labels"] = label_list
    return meta


def issue_url(meta: dict) -> str:
    repo = meta.get("upstream_repo", "dannerph/homeassistant-eon-energiemonitor")
    num = meta.get("issue_number")
    if num:
        return f"https://github.com/{repo}/issues/{num}"
    return f"https://github.com/{repo}/issues/new"


def main() -> None:
    meta = load_meta()
    title = meta.get("title", "Feature: Multiple EON regions via optional `scope` list")
    body = TEMPLATE_PATH.read_text(encoding="utf-8").strip()
    url = issue_url(meta)
    repo = meta.get("upstream_repo", "dannerph/homeassistant-eon-energiemonitor")
    issue_no = meta.get("issue_number", "?")
    labels = meta.get("labels") or ["enhancement"]
    label_str = ", ".join(f"`{l}`" for l in labels)

    header = f"""# GitHub issue (upstream)

| | |
|---|---|
| **Title** | {title} |
| **Repository** | `{repo}` |
| **Issue** | [#{issue_no}]({url}) |
| **Labels** | {label_str} |
| **Spec** | [SCOPE_SPEC.md](SCOPE_SPEC.md) |
| **Regenerate** | `python3 scripts/generate-scope-issue.py` |

> Auto-generated from `doc/scope-issue.meta.yaml` and `doc/templates/scope-issue.en.md`.  
> Edit those sources, then run the script. Use **Issue body** below for GitHub (or use `--body-file doc/templates/scope-issue.en.md`).

---

## Issue body (copy from here)

"""
    footer = f"""
---

## Recreate or update on GitHub

```bash
gh issue view {issue_no} --repo {repo}

# New issue:
gh issue create --repo {repo} \\
  --title '{title}' \\
  --body-file doc/templates/scope-issue.en.md \\
  --label enhancement

# Update existing issue #{issue_no}:
gh issue edit {issue_no} --repo {repo} \\
  --title '{title}' \\
  --body-file doc/templates/scope-issue.en.md
```

After creating a new issue, set `issue_number` in `doc/scope-issue.meta.yaml` and re-run this script.
"""

    OUT_PATH.write_text(header + body + footer, encoding="utf-8")
    print(f"Wrote {OUT_PATH}")
    print(f"Upstream issue: {url}")


if __name__ == "__main__":
    main()
