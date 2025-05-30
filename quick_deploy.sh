#!/bin/bash
# Python学习系统 - 快速GitHub部署脚本

echo "🚀 Python学习系统 - 快速部署到GitHub"
echo "================================================"

# 检查是否安装了git
if ! command -v git &> /dev/null; then
    echo "❌ Git未安装，请先安装Git"
    echo "📥 下载地址: https://git-scm.com/downloads"
    exit 1
fi

echo "✅ Git已安装"

# 初始化git仓库（如果未初始化）
if [ ! -d ".git" ]; then
    echo "🔧 初始化Git仓库..."
    git init
    echo "✅ Git仓库初始化完成"
else
    echo "✅ Git仓库已存在"
fi

# 设置git配置（如果未设置）
if [ -z "$(git config user.name)" ]; then
    echo "⚙️  设置Git用户信息"
    echo "请输入您的用户名:"
    read -r username
    git config user.name "$username"
fi

if [ -z "$(git config user.email)" ]; then
    echo "请输入您的邮箱:"
    read -r email
    git config user.email "$email"
fi

echo "✅ Git配置完成"

# 添加所有文件
echo "📁 添加文件到Git..."
git add .

# 检查是否有更改需要提交
if git diff --cached --quiet; then
    echo "ℹ️  没有更改需要提交"
else
    # 提交更改
    echo "💾 提交更改..."
    git commit -m "🚀 Python学习系统初始提交

    ✨ 功能特色:
    - 90天结构化Python学习计划
    - Web界面学习平台
    - 拓展阅读和官方文档链接
    - 进度跟踪和笔记记录
    - 响应式设计支持移动端
    
    🛠️ 技术栈:
    - Python 3.8+ / Flask
    - HTML5 / CSS3 / JavaScript
    - Bootstrap 5 响应式设计
    
    📚 课程内容:
    - 初级 (1-30天): Python基础语法
    - 中级 (31-60天): 面向对象和Web开发
    - 高级 (61-90天): 框架和项目实战"
    
    echo "✅ 提交完成"
fi

# 设置主分支
git branch -M main

# 询问是否设置远程仓库
echo ""
echo "📡 设置GitHub远程仓库"
echo "请先在GitHub上创建新仓库，然后输入仓库地址"
echo "格式示例:"
echo "  HTTPS: https://github.com/username/python-90-days.git"
echo "  SSH:   git@github.com:username/python-90-days.git"
echo ""
echo "请输入GitHub仓库地址 (留空跳过):"
read -r repo_url

if [ -n "$repo_url" ]; then
    # 检查是否已有远程仓库
    if git remote get-url origin &> /dev/null; then
        echo "🔄 更新远程仓库地址..."
        git remote set-url origin "$repo_url"
    else
        echo "➕ 添加远程仓库..."
        git remote add origin "$repo_url"
    fi
    
    echo "✅ 远程仓库设置完成"
    
    # 推送到GitHub
    echo "📤 推送代码到GitHub..."
    if git push -u origin main; then
        echo ""
        echo "🎉 恭喜！您的Python学习系统已成功部署到GitHub！"
        echo ""
        echo "📋 接下来您可以："
        echo "1. 🌐 在GitHub仓库页面查看代码"
        echo "2. 📄 启用GitHub Pages展示项目"
        echo "3. 👥 邀请其他人贡献代码"
        echo "4. ☁️  部署到云平台："
        echo "   • Heroku: https://heroku.com"
        echo "   • Railway: https://railway.app"
        echo "   • Vercel: https://vercel.com"
        echo "   • PythonAnywhere: https://pythonanywhere.com"
        echo ""
        echo "📖 查看 DEPLOYMENT_GUIDE.md 了解详细部署说明"
        echo ""
        echo "🔗 您的GitHub仓库: $repo_url"
    else
        echo "❌ 推送失败，请检查："
        echo "1. 网络连接是否正常"
        echo "2. 仓库地址是否正确"
        echo "3. 是否有仓库的push权限"
        echo ""
        echo "💡 您也可以稍后手动推送："
        echo "   git push -u origin main"
    fi
else
    echo "⚠️  跳过远程仓库设置"
    echo ""
    echo "📝 稍后您可以手动设置远程仓库并推送："
    echo "   git remote add origin <your-repo-url>"
    echo "   git push -u origin main"
fi

echo ""
echo "✨ 部署脚本执行完成！" 