#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python学习系统 - 生产环境入口文件
适用于云平台部署 (Heroku, Railway, Vercel等)
"""

import os
from web_app import app

# 设置生产环境配置
if __name__ == '__main__':
    # 从环境变量获取端口号，默认为8080
    port = int(os.environ.get('PORT', 8080))
    
    # 从环境变量获取主机地址，默认为本地
    host = os.environ.get('HOST', '0.0.0.0')
    
    # 从环境变量判断是否为调试模式
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    print(f"🚀 启动Python学习系统...")
    print(f"📱 监听地址: {host}:{port}")
    print(f"🐛 调试模式: {debug}")
    
    # 启动应用
    app.run(
        host=host,
        port=port,
        debug=debug
    ) 