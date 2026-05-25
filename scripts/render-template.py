#!/usr/bin/env python3
"""
模板渲染脚本
读取模板文件，将 {{variable}} 占位符替换为变量值，输出渲染后的 prompt
"""

import argparse
import json
import re
import sys
from pathlib import Path


def load_variables(vars_path: Path) -> dict:
    """从 JSON 文件加载变量"""
    content = vars_path.read_text(encoding="utf-8")
    return json.loads(content)


def render_template(template_path: Path, variables: dict) -> str:
    """渲染模板，替换 {{variable}} 占位符"""
    content = template_path.read_text(encoding="utf-8")

    # 简单替换 {{var_name}}
    def replace_var(match):
        var_name = match.group(1).strip()
        if var_name in variables:
            return str(variables[var_name])
        else:
            # 如果变量未提供，保留占位符并打印警告
            print(f"⚠️  警告: 变量 '{var_name}' 未提供", file=sys.stderr)
            return match.group(0)

    rendered = re.sub(r'\{\{(\s*[\w_-]+\s*)\}\}', replace_var, content)
    return rendered


def extract_variables(template_path: Path) -> list:
    """从模板中提取所有变量名"""
    content = template_path.read_text(encoding="utf-8")
    vars_found = set(re.findall(r'\{\{(\s*[\w_-]+\s*)\}\}', content))
    return sorted([v.strip() for v in vars_found])


def main():
    parser = argparse.ArgumentParser(description="渲染 Prompt 模板")
    parser.add_argument("template", type=Path, help="模板文件路径")
    parser.add_argument("--vars", type=Path, help="变量 JSON 文件路径")
    parser.add_argument("--output", "-o", type=Path, help="输出文件路径（默认 stdout）")
    parser.add_argument("--list-vars", action="store_true", help="列出模板所需变量并退出")
    parser.add_argument("--set", action="append", default=[], help="直接设置变量，格式: name=value")

    args = parser.parse_args()

    if not args.template.exists():
        print(f"错误: 模板文件不存在: {args.template}", file=sys.stderr)
        sys.exit(1)

    if args.list_vars:
        variables = extract_variables(args.template)
        print("模板所需变量:")
        for var in variables:
            print(f"  - {var}")
        sys.exit(0)

    # 加载变量
    variables = {}
    if args.vars:
        if not args.vars.exists():
            print(f"错误: 变量文件不存在: {args.vars}", file=sys.stderr)
            sys.exit(1)
        variables = load_variables(args.vars)

    # 解析命令行变量
    for item in args.set:
        if "=" not in item:
            print(f"错误: --set 参数格式错误: {item}（应为 name=value）", file=sys.stderr)
            sys.exit(1)
        name, value = item.split("=", 1)
        variables[name.strip()] = value.strip()

    # 渲染
    rendered = render_template(args.template, variables)

    # 输出
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
        print(f"✅ 已渲染到: {args.output}")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
