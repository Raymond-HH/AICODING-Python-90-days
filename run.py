#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python学习系统 - Web版本启动脚本
"""

import os
import sys
from pathlib import Path

# 添加当前目录到Python路径
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def check_dependencies():
    """检查必要的依赖"""
    try:
        import flask
        print("✓ Flask 已安装")
        return True
    except ImportError:
        print("❌ Flask 未安装，请运行: pip install -r requirements.txt")
        return False

def initialize_system():
    """初始化系统"""
    print("🚀 正在初始化Python学习系统...")
    
    # 检查并创建必要的目录
    directories = ['templates', 'static/css', 'static/js']
    for directory in directories:
        dir_path = current_dir / directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"✓ 创建目录: {directory}")
    
    # 检查进度文件
    progress_file = current_dir / "progress.json"
    if not progress_file.exists():
        import json
        from datetime import datetime
        
        initial_progress = {
            "start_date": datetime.now().strftime("%Y-%m-%d"),
            "current_day": 1,
            "completed_days": [],
            "notes": {}
        }
        
        with open(progress_file, 'w', encoding='utf-8') as f:
            json.dump(initial_progress, f, ensure_ascii=False, indent=2)
        print("✓ 创建进度文件")
    
    print("✅ 系统初始化完成!")

def main():
    """主函数"""
    print("=" * 50)
    print("🐍 Python 90天学习系统 - Web版本")
    print("=" * 50)
    
    # 检查依赖
    if not check_dependencies():
        return
    
    # 初始化系统
    initialize_system()
    
    # 启动Web应用
    try:
        from web_app import app
        print("\n🌐 启动Web服务器...")
        print("📱 访问地址: http://localhost:8080")
        print("⌨️  按 Ctrl+C 停止服务器")
        print("-" * 50)
        
        app.run(
            host='0.0.0.0',
            port=8080,
            debug=True,
            use_reloader=False  # 避免重复初始化
        )
        
    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        print("请确保所有依赖文件都存在")
    except KeyboardInterrupt:
        print("\n\n👋 感谢使用Python学习系统！")
    except Exception as e:
        print(f"\n❌ 启动失败: {e}")

if __name__ == "__main__":
    main() 