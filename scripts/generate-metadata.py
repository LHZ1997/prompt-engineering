#!/usr/bin/env python3
"""
全局索引生成脚本
扫描 prompts/ 和 templates/ 目录，提取所有 .md 文件的 frontmatter，生成 metadata.json
"""

import json
import re
import yaml
from pathlib import Path
from datetime import datetime, date


def extract_frontmatter(content: str) -> dict:
    """提取 YAML frontmatter"""
    if not content.startswith("---"):
        return None

    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        return None

    yaml_content = content[3:3 + end_match.start()]
    try:
        return yaml.safe_load(yaml_content)
    except yaml.YAMLError:
        return None


def scan_directory(directory: Path, base_path: Path) -> list:
    """扫描目录下的所有 .md 文件，提取元数据"""
    entries = []
    for md_file in sorted(directory.rglob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        frontmatter = extract_frontmatter(content)

        if frontmatter and isinstance(frontmatter, dict):
            rel_path = str(md_file.relative_to(base_path))
            raw_date = frontmatter.get("date")
            if isinstance(raw_date, date):
                raw_date = raw_date.isoformat()

            entry = {
                "id": frontmatter.get("id"),
                "path": rel_path,
                "category": frontmatter.get("category"),
                "tags": frontmatter.get("tags", []),
                "author": frontmatter.get("author"),
                "date": raw_date,
                "version": frontmatter.get("version"),
                "model_compatibility": frontmatter.get("model_compatibility", []),
                "description": frontmatter.get("description"),
            }
            entries.append(entry)

    return entries


def main():
    project_root = Path(__file__).parent.parent
    prompts_dir = project_root / "prompts"
    templates_dir = project_root / "templates"
    output_file = project_root / "metadata.json"

    metadata = {
        "generated_at": datetime.now().isoformat(),
        "version": "1.0.0",
        "prompts": [],
        "templates": [],
    }

    if prompts_dir.exists():
        metadata["prompts"] = scan_directory(prompts_dir, project_root)
        print(f"扫描 prompts/: 发现 {len(metadata['prompts'])} 个 prompt")

    if templates_dir.exists():
        metadata["templates"] = scan_directory(templates_dir, project_root)
        print(f"扫描 templates/: 发现 {len(metadata['templates'])} 个 template")

    # 写入文件
    output_file.write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    total = len(metadata["prompts"]) + len(metadata["templates"])
    print(f"✅ 已生成 metadata.json，共 {total} 条记录")


if __name__ == "__main__":
    main()
