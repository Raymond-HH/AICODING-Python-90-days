#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python学习系统初始化脚本
用于首次运行时生成所有必要文件和目录
"""

import os
import sys
from pathlib import Path
from detailed_curriculum import generate_complete_curriculum
from project_generator import generate_all_projects

def setup_learning_system():
    """初始化Python学习系统"""
    print("🚀 正在初始化Python学习系统...")
    
    # 创建基础目录结构
    base_path = Path(__file__).parent
    directories = [
        "backup",
        "projects", 
        "notes",
        "resources",
        "docs"
    ]
    
    for directory in directories:
        dir_path = base_path / directory
        dir_path.mkdir(exist_ok=True)
        print(f"✅ 创建目录: {directory}")
    
    # 生成课程大纲
    print("📚 生成课程大纲...")
    try:
        generate_complete_curriculum()
        print("✅ 课程大纲生成完成")
    except Exception as e:
        print(f"❌ 课程大纲生成失败: {e}")
        return False
    
    # 生成项目模板
    print("🎯 生成项目模板...")
    try:
        generate_all_projects()
        print("✅ 项目模板生成完成")
    except Exception as e:
        print(f"❌ 项目模板生成失败: {e}")
        return False
    
    # 创建学习资源文档
    create_learning_resources()
    
    # 创建快速开始指南
    create_quick_start_guide()
    
    print("\n🎉 Python学习系统初始化完成！")
    print("📖 运行 python main.py 开始学习")
    return True

def create_learning_resources():
    """创建学习资源文档"""
    resources_path = Path(__file__).parent / "docs"
    
    # Python学习资源
    python_resources = """# Python学习资源汇总

## 📚 官方文档和教程
- [Python官方文档](https://docs.python.org/zh-cn/3/)
- [Python官方教程](https://docs.python.org/zh-cn/3/tutorial/)
- [Python标准库参考](https://docs.python.org/zh-cn/3/library/)

## 📖 推荐书籍
### 初学者
- 《Python编程：从入门到实践》- Eric Matthes
- 《笨办法学Python》- Zed Shaw
- 《Python核心编程》- Wesley Chun

### 进阶
- 《流畅的Python》- Luciano Ramalho
- 《Effective Python》- Brett Slatkin
- 《Python高级编程》- Tarek Ziadé

## 🌐 在线学习平台
- [菜鸟教程 - Python](https://www.runoob.com/python3/python3-tutorial.html)
- [廖雪峰Python教程](https://www.liaoxuefeng.com/wiki/1016959663602400)
- [Python之禅](https://pythonzentips.com/)

## 🛠️ 开发工具
### IDE推荐
- **PyCharm** - 功能强大的Python IDE
- **VSCode** - 轻量级但功能丰富
- **Sublime Text** - 快速响应的文本编辑器
- **Vim/Neovim** - 高效的命令行编辑器

### 有用的包管理工具
- **pip** - Python包管理器
- **conda** - 科学计算包管理
- **pipenv** - 虚拟环境管理
- **poetry** - 现代依赖管理

## 🔧 实用工具和库
### 数据处理
- **pandas** - 数据分析
- **numpy** - 数值计算
- **matplotlib** - 数据可视化
- **seaborn** - 统计数据可视化

### Web开发
- **Flask** - 轻量级Web框架
- **Django** - 全功能Web框架
- **FastAPI** - 现代高性能API框架
- **requests** - HTTP库

### 测试
- **pytest** - 测试框架
- **unittest** - 标准测试库
- **coverage** - 代码覆盖率

## 📱 移动应用
- **Kivy** - 跨平台应用开发
- **BeeWare** - 原生应用开发套件

## 🤖 人工智能/机器学习
- **scikit-learn** - 机器学习库
- **TensorFlow** - 深度学习框架
- **PyTorch** - 深度学习框架
- **OpenCV** - 计算机视觉

## 🎮 游戏开发
- **Pygame** - 2D游戏开发
- **Panda3D** - 3D游戏引擎

## 💡 学习建议
1. **循序渐进**: 不要急于求成，按计划逐步学习
2. **多动手**: 编程是实践性很强的技能，要多写代码
3. **读优秀代码**: 学习开源项目的代码风格和设计
4. **参与社区**: 加入Python社区，与其他开发者交流
5. **坚持练习**: 每天保持一定的编程练习

## 🆘 遇到问题时的求助渠道
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)
- [Python官方论坛](https://discuss.python.org/)
- [Reddit - r/Python](https://www.reddit.com/r/Python/)
- [知乎Python话题](https://www.zhihu.com/topic/19552832)
- [CSDN Python社区](https://blog.csdn.net/nav/python)

## 📊 Python应用领域
- **Web开发**: 网站、API服务
- **数据科学**: 数据分析、机器学习、人工智能
- **自动化**: 脚本编写、任务自动化、测试自动化
- **科学计算**: 数学建模、科学研究
- **游戏开发**: 2D/3D游戏、游戏脚本
- **网络编程**: 网络工具、服务器开发
- **桌面应用**: GUI应用程序开发
"""

    with open(resources_path / "learning_resources.md", 'w', encoding='utf-8') as f:
        f.write(python_resources)
    
    print("✅ 学习资源文档已创建")

def create_quick_start_guide():
    """创建快速开始指南"""
    docs_path = Path(__file__).parent / "docs"
    
    quick_start = """# 🚀 Python学习系统快速开始指南

## 系统介绍
这是一个为期90天的Python学习系统，专为零基础学员设计。系统包含：
- 📚 详细的每日学习计划
- 🎯 每周实践项目
- 📊 学习进度跟踪
- 📝 笔记记录功能

## 使用方法

### 1. 启动系统
```bash
python main.py
```

### 2. 主要功能
- **今日学习内容**: 查看当天的学习材料和任务
- **学习计划**: 浏览完整的90天课程大纲
- **完成学习**: 标记今日学习为完成状态
- **进度统计**: 查看学习进度和统计数据
- **学习笔记**: 记录学习心得和重点
- **每周项目**: 查看和完成实践项目

### 3. 学习建议
1. **每天坚持**: 建议每天学习1-2小时
2. **按序学习**: 严格按照课程顺序进行
3. **动手实践**: 每个示例都要亲自敲一遍
4. **完成练习**: 认真完成每天的练习任务
5. **记录笔记**: 及时记录学习要点和疑问
6. **周项目**: 认真完成每周的项目练习

### 4. 目录结构
```
Python_learning/
├── main.py              # 主程序入口
├── curriculum.json      # 课程大纲数据
├── progress.json        # 学习进度数据
├── projects/            # 每周项目目录
│   ├── week_1/         # 第1周项目
│   ├── week_2/         # 第2周项目
│   └── ...
├── docs/               # 文档目录
├── backup/             # 备份目录
└── notes/              # 笔记目录
```

### 5. 学习路径
- **第1-30天 (初级)**: Python基础语法和核心概念
- **第31-60天 (中级)**: 面向对象编程和常用库
- **第61-90天 (高级)**: 高级特性和项目开发

### 6. 每周项目概览
1. **第1周**: 计算器程序 - 基础语法练习
2. **第2周**: 猜数字游戏 - 条件语句和循环
3. **第3周**: 学生成绩管理 - 数据结构应用
4. **第4周**: 文本文件处理器 - 文件操作
5. **第5周**: 网页数据抓取 - 网络编程
6. **第6周**: 数据分析小工具 - 数据处理
7. **第7周**: 简单Web应用 - Web开发
8. **第8周**: 数据库应用 - 数据库操作
9. **第9周**: API服务开发 - 接口设计
10. **第10周**: 多线程应用 - 并发编程
11. **第11周**: 机器学习入门 - AI基础
12. **第12周**: 项目部署 - 运维技能
13. **第13周**: 综合项目 - 技能整合

### 7. 学习目标
- **1个月后**: 能够上手简单项目
- **2个月后**: 具备中级开发能力
- **3个月后**: 能够在AI辅助下看懂大部分项目代码

### 8. 常见问题
**Q: 如果某天的内容太难怎么办？**
A: 可以多花一些时间，或者先继续下一天的内容，稍后回头复习。

**Q: 可以跳过某些内容吗？**
A: 不建议跳过，每天的内容都是精心设计的，有连贯性。

**Q: 如何重置学习进度？**
A: 在系统设置中选择"重置学习进度"。

**Q: 项目太难完成不了怎么办？**
A: 项目有基础版和进阶版，可以先完成基础版。

### 9. 技术支持
如遇到问题，可以：
1. 查看docs目录下的学习资源
2. 在线搜索相关问题
3. 参考提供的学习资源链接

## 开始学习
准备好了吗？运行 `python main.py` 开始你的Python学习之旅！

祝你学习愉快！🎉
"""

    with open(docs_path / "quick_start.md", 'w', encoding='utf-8') as f:
        f.write(quick_start)
    
    print("✅ 快速开始指南已创建")

if __name__ == "__main__":
    success = setup_learning_system()
    if success:
        print("\n" + "="*50)
        print("🎓 欢迎使用Python 90天学习系统！")
        print("📖 运行以下命令开始学习:")
        print("   python main.py")
        print("="*50)
    else:
        print("❌ 系统初始化失败，请检查错误信息")
        sys.exit(1) 