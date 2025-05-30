# 🚀 GitHub部署指南

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
