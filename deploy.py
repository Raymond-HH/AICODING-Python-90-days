#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub自动化部署脚本
用于将Python学习系统部署到GitHub
"""

import os
import subprocess
import sys
from pathlib import Path
import json

def run_command(command, description=""):
    """执行命令并显示结果"""
    print(f"🔧 {description}")
    print(f"执行: {command}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ 成功: {description}")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"❌ 失败: {description}")
            print(f"错误: {result.stderr}")
            return False
        return True
    except Exception as e:
        print(f"❌ 执行失败: {e}")
        return False

def check_git_installed():
    """检查Git是否已安装"""
    return run_command("git --version", "检查Git版本")

def initialize_git():
    """初始化Git仓库"""
    if not os.path.exists('.git'):
        return run_command("git init", "初始化Git仓库")
    else:
        print("✅ Git仓库已存在")
        return True

def setup_gitignore():
    """设置.gitignore文件"""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs
*.log
logs/

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Flask
instance/
.webassets-cache

# User data
progress.json
backup/
notes/user_notes.json

# Temporary files
temp/
tmp/
"""
    
    with open('.gitignore', 'w', encoding='utf-8') as f:
        f.write(gitignore_content)
    print("✅ .gitignore文件已更新")

def create_readme():
    """创建或更新README.md"""
    readme_content = """# 🐍 Python 90天学习系统

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/python-90-days.svg)](https://github.com/yourusername/python-90-days/stargazers)

一个专为Python零基础学员设计的完整学习系统，通过90天的结构化学习，帮助你从小白成长为能够独立开发项目的Python程序员。

## ✨ 主要特色

- 📚 **科学的课程设计**: 90天结构化学习计划，分为初级、中级、高级三个阶段
- 🎯 **实用导向**: 每天都有具体的代码示例和练习题
- 🛠️ **Web界面**: 现代化的Web学习平台，支持进度跟踪和笔记记录
- 📖 **拓展阅读**: 每课都提供官方Python文档链接和深度学习资源
- 🎮 **互动体验**: 完成打卡、笔记记录、项目展示等功能

## 🚀 快速开始

### 在线体验
访问 [在线演示](https://your-demo-site.com) 立即开始学习！

### 本地运行

1. **克隆项目**
```bash
git clone https://github.com/yourusername/python-90-days.git
cd python-90-days
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **启动系统**
```bash
python run.py
```

4. **访问系统**
打开浏览器访问 `http://localhost:8080`

## 📚 课程内容

### 🌱 初级阶段 (第1-30天)
- Python环境搭建和基础语法
- 变量、数据类型、运算符
- 条件语句和循环结构
- 列表、字典、元组等数据结构
- 函数定义和文件操作

### 🚀 中级阶段 (第31-60天)
- 面向对象编程
- 模块和包管理
- Web开发基础
- 数据库操作
- API开发

### 🎓 高级阶段 (第61-90天)
- 框架深入学习
- 项目架构设计
- 性能优化
- 部署和运维
- 综合项目实战

## 🛠️ 技术栈

- **后端**: Python 3.8+, Flask
- **前端**: HTML5, CSS3, JavaScript, Bootstrap
- **数据存储**: JSON文件
- **部署**: 支持多种部署方式

## 📱 功能特色

- ✅ **进度跟踪**: 可视化学习进度
- 📝 **笔记系统**: 记录学习心得
- 🎯 **每日打卡**: 培养学习习惯
- 📖 **拓展阅读**: 深度学习资源
- 🎮 **项目实战**: 13个实战项目
- 📊 **学习统计**: 详细的学习数据

## 🤝 贡献指南

欢迎贡献代码、报告问题或提出建议！

1. Fork 这个项目
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- 感谢 [Python官方文档](https://docs.python.org/zh-cn/3/) 提供的优质学习资源
- 感谢所有为Python社区做出贡献的开发者们
- 感谢使用本系统的每一位学习者

## 📞 联系我们

- 📧 Email: your-email@example.com
- 💬 讨论群: [加入我们的学习群](https://your-chat-link.com)
- 🐛 问题反馈: [GitHub Issues](https://github.com/yourusername/python-90-days/issues)

---

⭐ 如果这个项目对你有帮助，请给个Star支持一下！
"""
    
    # 只有当README.md不存在或者用户确认时才更新
    if not os.path.exists('README.md'):
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print("✅ README.md文件已创建")
    else:
        print("ℹ️  README.md文件已存在，跳过更新")

def create_license():
    """创建MIT许可证文件"""
    license_content = """MIT License

Copyright (c) 2024 Python 90天学习系统

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    
    if not os.path.exists('LICENSE'):
        with open('LICENSE', 'w', encoding='utf-8') as f:
            f.write(license_content)
        print("✅ LICENSE文件已创建")

def create_github_workflows():
    """创建GitHub Actions工作流"""
    os.makedirs('.github/workflows', exist_ok=True)
    
    # CI/CD 工作流
    workflow_content = """name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10', '3.11']

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov flake8
    
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    
    - name: Test with pytest
      run: |
        pytest tests/ --cov=. --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./static
"""
    
    with open('.github/workflows/ci.yml', 'w', encoding='utf-8') as f:
        f.write(workflow_content)
    print("✅ GitHub Actions工作流已创建")

def setup_github_remote():
    """设置GitHub远程仓库"""
    print("\n📡 设置GitHub远程仓库")
    print("请按以下步骤操作：")
    print("1. 在GitHub上创建新仓库 (建议名称: python-90-days)")
    print("2. 复制仓库的HTTPS或SSH地址")
    
    repo_url = input("请输入GitHub仓库地址: ").strip()
    
    if repo_url:
        # 检查是否已有远程仓库
        result = subprocess.run("git remote get-url origin", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            # 更新现有的远程仓库
            return run_command(f"git remote set-url origin {repo_url}", "更新远程仓库地址")
        else:
            # 添加新的远程仓库
            return run_command(f"git remote add origin {repo_url}", "添加远程仓库")
    else:
        print("⚠️  跳过远程仓库设置")
        return True

def commit_and_push():
    """提交并推送代码"""
    print("\n📤 提交并推送代码到GitHub")
    
    # 添加所有文件
    if not run_command("git add .", "添加所有文件到暂存区"):
        return False
    
    # 检查是否有更改
    result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    if not result.stdout.strip():
        print("ℹ️  没有需要提交的更改")
        return True
    
    # 提交更改
    commit_message = "🚀 Initial commit: Python 90天学习系统"
    if not run_command(f'git commit -m "{commit_message}"', "提交更改"):
        return False
    
    # 设置主分支名称
    run_command("git branch -M main", "设置主分支为main")
    
    # 推送到GitHub
    return run_command("git push -u origin main", "推送代码到GitHub")

def create_deployment_guide():
    """创建部署指南"""
    guide_content = """# 🚀 GitHub部署指南

本指南将帮助您将Python学习系统部署到GitHub，并可选择性地部署到各种云平台。

## 📋 部署清单

### ✅ 已完成的配置
- [x] Git仓库初始化
- [x] .gitignore文件配置
- [x] requirements.txt依赖列表
- [x] README.md项目说明
- [x] LICENSE许可证文件
- [x] GitHub Actions CI/CD
- [x] 代码推送到GitHub

## 🌐 部署选项

### 1. GitHub Pages (静态站点)
适用于展示项目文档和前端页面。

### 2. Heroku (免费额度)
```bash
# 安装Heroku CLI后执行
heroku create your-app-name
git push heroku main
```

### 3. Railway
```bash
# 连接到Railway
railway login
railway init
railway up
```

### 4. Vercel
```bash
# 安装Vercel CLI
npm i -g vercel
vercel
```

### 5. PythonAnywhere
1. 上传代码到PythonAnywhere
2. 在Web选项卡中配置Flask应用
3. 设置静态文件路径

## 🔧 环境变量配置

在生产环境中，请设置以下环境变量：

```bash
export FLASK_ENV=production
export SECRET_KEY=your-secret-key-here
```

## 📱 移动端适配

项目已经包含响应式设计，在移动设备上也能良好显示。

## 🔄 持续部署

每次推送到main分支时，GitHub Actions会自动：
1. 运行代码检查
2. 执行测试
3. 部署到生产环境（如果配置）

## 🐛 常见问题

### Q: 如何更新部署？
A: 直接推送代码到GitHub，自动部署会处理更新。

### Q: 如何查看部署日志？
A: 在GitHub仓库的Actions选项卡中查看。

### Q: 如何回滚版本？
A: 在GitHub中切换到之前的提交，然后重新部署。

## 📞 获取帮助

如果在部署过程中遇到问题，请：
1. 检查GitHub Actions的日志
2. 查看Issues页面寻找解决方案
3. 创建新的Issue描述问题

---
祝您部署成功！🎉
"""
    
    with open('DEPLOYMENT_GUIDE.md', 'w', encoding='utf-8') as f:
        f.write(guide_content)
    print("✅ DEPLOYMENT_GUIDE.md部署指南已创建")

def main():
    """主函数"""
    print("🚀 Python学习系统 - GitHub部署工具")
    print("=" * 50)
    
    # 检查Git是否安装
    if not check_git_installed():
        print("❌ 请先安装Git: https://git-scm.com/downloads")
        return
    
    # 初始化Git仓库
    if not initialize_git():
        return
    
    # 设置项目文件
    setup_gitignore()
    create_readme()
    create_license()
    create_github_workflows()
    create_deployment_guide()
    
    # 设置GitHub远程仓库
    if not setup_github_remote():
        print("⚠️  远程仓库设置失败，请手动设置")
    
    # 提交并推送代码
    print("\n🤔 是否现在提交并推送代码到GitHub？")
    choice = input("输入 y 继续，其他键跳过: ").strip().lower()
    
    if choice == 'y':
        if commit_and_push():
            print("\n🎉 恭喜！您的Python学习系统已成功部署到GitHub！")
            print("\n📋 接下来您可以：")
            print("1. 在GitHub仓库页面查看代码")
            print("2. 启用GitHub Pages展示项目")
            print("3. 邀请其他人贡献代码")
            print("4. 部署到云平台 (Heroku, Railway, Vercel等)")
            print("\n📖 查看 DEPLOYMENT_GUIDE.md 了解更多部署选项")
        else:
            print("❌ 推送失败，请检查网络连接和仓库权限")
    else:
        print("\n📝 文件已准备就绪，您可以稍后手动推送：")
        print("git add .")
        print('git commit -m "Initial commit"')
        print("git push -u origin main")
    
    print("\n✨ 部署配置完成！")

if __name__ == "__main__":
    main() 