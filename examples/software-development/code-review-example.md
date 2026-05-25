# 代码审查示例

## 使用的 Prompt

[prompts/software-development/code-review.md](../../prompts/software-development/code-review.md)

## 输入

### 变量

| 变量 | 值 |
|------|-----|
| `language` | `python` |
| `code` | 见下方 |
| `context` | `Flask Web 应用中的用户注册接口` |

### 代码

```python
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    cursor.execute(query)
    conn.commit()
    conn.close()
    
    return jsonify({"message": "User created"})
```

## 输出

### 总体评价

代码存在 **Critical** 级别的安全漏洞（SQL 注入、明文存储密码），且缺少输入校验和错误处理，不适合生产环境使用。

### 问题列表

| 行号 | 严重级别 | 类别 | 问题描述 | 改进建议 |
|------|----------|------|----------|----------|
| 4-5 | Critical | 安全性 | 直接访问字典键，可能触发 KeyError | 使用 `.get()` 并校验必填字段 |
| 5 | Critical | 安全性 | 密码明文存储，存在严重安全隐患 | 使用 bcrypt/argon2 哈希后存储 |
| 8 | Critical | 安全性 | SQL 字符串拼接，存在 SQL 注入 | 使用参数化查询 |
| 3 | Major | 健壮性 | 未校验 Content-Type 和请求体格式 | 增加 `force=True` 或校验逻辑 |
| 4-5 | Major | 健壮性 | 未校验 username/password 长度和格式 | 增加正则校验和长度限制 |
| 10 | Major | 健壮性 | 未处理数据库操作异常 | 添加 try/finally 或上下文管理器 |
| 6-10 | Minor | 性能 | 每次请求新建数据库连接 | 考虑使用连接池 |
| 13 | Minor | 规范 | 返回 200 但实际可能是错误场景 | 根据结果返回合适状态码 |

### 改进后的代码

```python
import re
import bcrypt
import sqlite3
from flask import request, jsonify
from contextlib import closing

@app.route('/register', methods=['POST'])
def register():
    # 1. 获取并校验输入
    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON body"}), 400
    
    username = data.get('username', '').strip()
    password = data.get('password', '')
    
    if not username or not password:
        return jsonify({"error": "username and password are required"}), 400
    
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', username):
        return jsonify({"error": "username must be 3-20 alphanumeric characters"}), 400
    
    if len(password) < 8:
        return jsonify({"error": "password must be at least 8 characters"}), 400
    
    # 2. 密码哈希
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    # 3. 安全的数据库操作
    try:
        with closing(sqlite3.connect('app.db')) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash)
            )
            conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 409
    except sqlite3.Error as e:
        return jsonify({"error": "Database error"}), 500
    
    return jsonify({"message": "User created successfully"}), 201
```

### 学习要点

1. **永远不要信任用户输入**：对所有外部输入进行类型、格式和长度校验
2. **密码必须哈希存储**：使用 bcrypt、argon2 等专门算法，不要自创加密方案
3. **参数化查询是防 SQL 注入的唯一正确方式**：字符串格式化/拼接都不安全
