#!/bin/bash

# 🚀 GitHub上传脚本
# Python 90天学习系统

echo "🚀 准备上传Python学习系统到GitHub..."
echo "========================================"

# 检查是否已经有远程仓库
if git remote get-url origin 2>/dev/null; then
    echo "✅ 远程仓库已存在"
    echo "当前远程仓库: $(git remote get-url origin)"
else
    echo "❌ 还未设置远程仓库"
    echo ""
    echo "📝 请按照以下步骤操作："
    echo ""
    echo "1. 访问 https://github.com"
    echo "2. 点击右上角 '+' 号，选择 'New repository'"
    echo "3. 填写仓库信息："
    echo "   - Repository name: python-90-days-learning-system"
    echo "   - Description: 90天Python系统化学习平台 - Web版本"
    echo "   - 选择 Public 或 Private"
    echo "   - 不要勾选任何初始化选项"
    echo "4. 点击 'Create repository'"
    echo ""
    echo "5. 创建后，复制仓库URL并运行："
    echo "   git remote add origin YOUR_REPOSITORY_URL"
    echo "   例如: git remote add origin https://github.com/ruihu/python-90-days-learning-system.git"
    echo ""
    echo "6. 然后运行："
    echo "   git push -u origin main"
    echo ""
    exit 1
fi

# 显示当前状态
echo ""
echo "📊 当前Git状态："
git status --porcelain

echo ""
echo "📝 最新提交："
git log --oneline -n 1

echo ""
echo "🔗 远程仓库："
git remote -v

echo ""
echo "🚀 准备推送到GitHub..."
echo "如果这是第一次推送，可能需要输入GitHub凭据"

# 推送到GitHub
if git push -u origin main; then
    echo ""
    echo "🎉 成功上传到GitHub！"
    echo "========================================"
    echo "📱 仓库地址: $(git remote get-url origin)"
    echo "🌐 可以在浏览器中访问查看您的项目"
    echo ""
    echo "📋 后续更新步骤："
    echo "1. 修改代码后运行: git add ."
    echo "2. 创建提交: git commit -m '描述您的更改'"
    echo "3. 推送更新: git push origin main"
else
    echo ""
    echo "❌ 上传失败！"
    echo "可能的原因："
    echo "1. 网络连接问题"
    echo "2. 认证失败 - 需要设置Personal Access Token"
    echo "3. 远程仓库地址错误"
    echo ""
    echo "💡 如果认证失败，请："
    echo "1. 访问 GitHub > Settings > Developer settings > Personal access tokens"
    echo "2. 生成新的token，选择 repo 权限"
    echo "3. 推送时使用token作为密码"
fi 