#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
课程大纲生成器
生成90天Python学习计划的详细内容
"""

import json
from pathlib import Path

def generate_curriculum():
    """生成完整的90天Python学习课程大纲"""
    
    curriculum = {
        "metadata": {
            "title": "Python 90天学习计划",
            "description": "从零基础到能够独立开发项目的完整学习路径",
            "duration": "90天",
            "daily_time": "1-2小时",
            "levels": ["初级(1-30天)", "中级(31-60天)", "高级(61-90天)"]
        },
        "beginner": {
            "title": "初级阶段 (第1-30天)",
            "description": "掌握Python基础语法和核心概念",
            "goals": [
                "理解Python基本语法",
                "掌握数据类型和控制结构",
                "能够编写简单的程序",
                "具备基础的调试能力"
            ],
            "days": generate_beginner_days()
        },
        "intermediate": {
            "title": "中级阶段 (第31-60天)",
            "description": "深入学习面向对象编程和常用库",
            "goals": [
                "掌握面向对象编程",
                "熟练使用常用第三方库",
                "能够处理文件和网络操作",
                "具备基础的项目开发能力"
            ],
            "days": generate_intermediate_days()
        },
        "advanced": {
            "title": "高级阶段 (第61-90天)",
            "description": "学习高级特性和实际项目开发",
            "goals": [
                "掌握高级编程技巧",
                "能够开发完整的应用程序",
                "了解性能优化和部署",
                "具备解决复杂问题的能力"
            ],
            "days": generate_advanced_days()
        }
    }
    
    # 保存课程大纲
    output_file = Path(__file__).parent / "curriculum.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(curriculum, f, ensure_ascii=False, indent=2)
    
    print(f"课程大纲已生成: {output_file}")
    return curriculum

def generate_beginner_days():
    """生成初级阶段的每日学习内容"""
    days = {}
    
    # 第1周: Python基础入门
    days["1"] = {
        "topic": "Python简介与环境搭建",
        "duration": "1-1.5小时",
        "objectives": "了解Python语言特点，完成开发环境搭建",
        "content": [
            "Python语言简介和应用领域",
            "安装Python解释器和IDE",
            "第一个Python程序：Hello World",
            "Python交互式环境的使用"
        ],
        "examples": [
            "print('Hello, World!')",
            "在IDLE中执行简单计算",
            "使用help()函数获取帮助"
        ],
        "exercises": [
            "输出你的姓名和年龄",
            "计算圆形面积（半径为5）",
            "尝试不同的print()参数"
        ]
    }
    
    days["2"] = {
        "topic": "变量与数据类型",
        "duration": "1.5小时",
        "objectives": "掌握Python基本数据类型和变量使用",
        "content": [
            "变量的定义和命名规则",
            "数字类型：int, float, complex",
            "字符串类型：str",
            "布尔类型：bool",
            "type()函数的使用"
        ],
        "examples": [
            "name = 'Alice'",
            "age = 25",
            "height = 1.75",
            "is_student = True"
        ],
        "exercises": [
            "创建不同类型的变量",
            "使用type()检查变量类型",
            "尝试类型转换函数"
        ]
    }
    
    # 继续添加更多天的内容...
    # 为了节省空间，这里只展示前几天的详细内容
    # 实际系统中会包含完整的90天内容
    
    # 第7天：复习日
    days["7"] = {
        "topic": "第一周复习与小测试",
        "duration": "1.5小时",
        "objectives": "巩固第一周学习内容，查漏补缺",
        "content": [
            "回顾Python基础语法",
            "练习变量和数据类型",
            "解决常见错误",
            "完成综合练习"
        ],
        "examples": [
            "综合使用所学知识编写小程序",
            "调试常见语法错误"
        ],
        "exercises": [
            "编写个人信息管理小程序",
            "完成10道基础语法题目",
            "总结学习笔记"
        ]
    }
    
    # 为简化展示，这里返回部分内容
    # 实际实现中会包含完整的30天内容
    return days

def generate_intermediate_days():
    """生成中级阶段的每日学习内容"""
    days = {}
    
    days["31"] = {
        "topic": "面向对象编程基础",
        "duration": "2小时",
        "objectives": "理解类和对象的概念，学会定义简单的类",
        "content": [
            "面向对象编程概念",
            "类的定义和实例化",
            "属性和方法",
            "self关键字的使用"
        ],
        "examples": [
            "class Person:",
            "    def __init__(self, name):",
            "        self.name = name"
        ],
        "exercises": [
            "创建学生类",
            "添加方法显示学生信息",
            "创建多个学生对象"
        ]
    }
    
    # 更多中级内容...
    return days

def generate_advanced_days():
    """生成高级阶段的每日学习内容"""
    days = {}
    
    days["61"] = {
        "topic": "设计模式入门",
        "duration": "2小时",
        "objectives": "了解常用设计模式，提高代码质量",
        "content": [
            "设计模式概述",
            "单例模式",
            "工厂模式",
            "观察者模式"
        ],
        "examples": [
            "实现单例模式",
            "创建简单工厂"
        ],
        "exercises": [
            "实现配置管理单例",
            "设计日志记录器",
            "创建事件监听系统"
        ]
    }
    
    # 更多高级内容...
    return days

if __name__ == "__main__":
    generate_curriculum() 