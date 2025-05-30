#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python学习系统启动脚本
"""

import sys
import subprocess
from pathlib import Path

def check_dependencies():
    """检查依赖包"""
    try:
        import flask
        print("✓ Flask 已安装")
        return True
    except ImportError:
        print("❌ Flask 未安装")
        print("正在安装 Flask...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
            print("✓ Flask 安装成功")
            return True
        except subprocess.CalledProcessError:
            print("❌ Flask 安装失败")
            return False

def main():
    print("=" * 50)
    print("🐍 Python 90天学习系统 - Web版本")
    print("=" * 50)
    
    # 检查依赖
    if not check_dependencies():
        print("❌ 依赖检查失败，无法启动")
        return
    
    print("🚀 正在初始化Python学习系统...")
    
    # 确保必要的目录存在
    base_path = Path(__file__).parent
    directories = ['templates', 'static/css', 'static/js', 'static/images']
    for dir_path in directories:
        (base_path / dir_path).mkdir(parents=True, exist_ok=True)
    
    print("✅ 系统初始化完成!")
    print()
    print("🌐 启动Web服务器...")
    print("📱 访问地址: http://localhost:8080")
    print("⌨️  按 Ctrl+C 停止服务器")
    print("-" * 50)
    
    try:
        # 启动web应用
        import web_app
        web_app.app.run(debug=True, host='0.0.0.0', port=8080)
    except KeyboardInterrupt:
        print("\n👋 感谢使用Python学习系统！")
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        print("请检查是否有其他程序占用8080端口")

if __name__ == "__main__":
    main() 