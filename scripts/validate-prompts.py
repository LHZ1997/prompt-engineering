#!/usr/bin/env python3
"""
Prompt 格式校验脚本
校验所有 .md 文件的 frontmatter 完整性、id 唯一性、category/tag 合规性
"""

import os
import sys
import re
import yaml
from pathlib import Path
from typing import List, Dict, Tuple

# 预定义的一级分类
VALID_CATEGORIES = {
    "software-development", "writing", "data-analysis",
    "product-management", "ai-development", "business", "education",
    "analysis", "generation", "reasoning", "conversation"
}

# 必填字段
REQUIRED_FIELDS = {"id", "category", "tags", "author", "date", "version", "description"}


def extract_frontmatter(content: str) -> Tuple[Dict, str]:
    """提取 YAML frontmatter"""
    if not content.startswith("---"):
        return None, "文件缺少 YAML frontmatter"

    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        return None, "YAML frontmatter 未正确闭合"

    yaml_content = content[3:3 + end_match.start()]
    try:
        data = yaml.safe_load(yaml_content)
        if not isinstance(data, dict):
            return None, "YAML frontmatter 不是有效的字典"
        return data, None
    except yaml.YAMLError as e:
        return None, f"YAML 解析错误: {e}"


def validate_file(file_path: Path, all_ids: Dict[str, Path]) -> List[str]:
    """校验单个文件，返回错误列表"""
    errors = []
    content = file_path.read_text(encoding="utf-8")

    # 提取 frontmatter
    frontmatter, error = extract_frontmatter(content)
    if error:
        errors.append(error)
        return errors

    # 检查必填字段
    missing = REQUIRED_FIELDS - set(frontmatter.keys())
    if missing:
        errors.append(f"缺少必填字段: {', '.join(sorted(missing))}")

    # 检查 id
    file_id = frontmatter.get("id")
    if file_id:
        if not re.match(r'^[a-z0-9-]+$', str(file_id)):
            errors.append(f"id 格式非法: '{file_id}'，只能包含小写字母、数字和连字符")
        elif file_id in all_ids:
            errors.append(f"id 重复: '{file_id}' 已存在于 {all_ids[file_id]}")
        else:
            all_ids[file_id] = file_path

    # 检查 category
    category = frontmatter.get("category")
    if category and str(category) not in VALID_CATEGORIES:
        errors.append(f"非法 category: '{category}'，有效值: {', '.join(sorted(VALID_CATEGORIES))}")

    # 检查 tags
    tags = frontmatter.get("tags")
    if tags is not None:
        if not isinstance(tags, list):
            errors.append("tags 必须是数组")
        elif len(tags) == 0:
            errors.append("tags 不能为空数组")
        else:
            for tag in tags:
                if not isinstance(tag, str):
                    errors.append(f"tag 必须是字符串: {tag}")
                    break

    # 检查 version
    version = frontmatter.get("version")
    if version and not re.match(r'^\d+\.\d+\.\d+$', str(version)):
        errors.append(f"version 格式非法: '{version}'，应为 x.y.z")

    # 检查 date
    date = frontmatter.get("date")
    if date and not re.match(r'^\d{4}-\d{2}-\d{2}$', str(date)):
        errors.append(f"date 格式非法: '{date}'，应为 YYYY-MM-DD")

    return errors


def main():
    project_root = Path(__file__).parent.parent
    prompts_dir = project_root / "prompts"
    templates_dir = project_root / "templates"

    all_ids: Dict[str, Path] = {}
    total_files = 0
    total_errors = 0
    passed_files = 0

    scan_dirs = [d for d in [prompts_dir, templates_dir] if d.exists()]

    if not scan_dirs:
        print("错误: 未找到 prompts/ 或 templates/ 目录")
        sys.exit(1)

    for scan_dir in scan_dirs:
        for md_file in sorted(scan_dir.rglob("*.md")):
            total_files += 1
            rel_path = md_file.relative_to(project_root)
            errors = validate_file(md_file, all_ids)

            if errors:
                total_errors += len(errors)
                print(f"❌ {rel_path}")
                for err in errors:
                    print(f"   - {err}")
            else:
                passed_files += 1
                print(f"✅ {rel_path}")

    print(f"\n{'=' * 50}")
    print(f"总计: {total_files} 个文件")
    print(f"通过: {passed_files} 个")
    print(f"失败: {total_files - passed_files} 个")
    print(f"错误: {total_errors} 个")

    if total_errors > 0:
        sys.exit(1)
    else:
        print("\n🎉 所有文件校验通过！")
        sys.exit(0)


if __name__ == "__main__":
    main()
