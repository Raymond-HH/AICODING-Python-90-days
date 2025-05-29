#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的课程内容数据
为前几天提供基本的学习内容
"""

def get_simple_course_content():
    """获取简单的课程内容"""
    return {
        "1": {
            "topic": "Python入门与环境搭建",
            "duration": "1-2小时",
            "objectives": "了解Python基础知识，搭建开发环境",
            "concepts": [
                {
                    "name": "什么是Python",
                    "description": "Python是一种高级编程语言，以其简洁和可读性著称",
                    "details": [
                        "1991年由Guido van Rossum创建",
                        "面向对象的动态语言",
                        "广泛应用于Web开发、数据科学、人工智能等领域"
                    ]
                },
                {
                    "name": "Python的特点",
                    "description": "了解Python的主要特色和优势",
                    "details": [
                        "语法简洁清晰",
                        "跨平台支持",
                        "丰富的第三方库",
                        "活跃的社区支持"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "第一个Python程序",
                    "code": "print(\"Hello, Python!\")\nprint(\"欢迎来到Python世界！\")",
                    "explanation": "这是最基础的Python程序，使用print()函数输出文本到控制台"
                }
            ],
            "exercises": [
                {
                    "title": "练习：打印个人信息",
                    "description": "编写一个程序，打印你的姓名、年龄和爱好",
                    "hint": "使用多个print()语句",
                    "solution": "print(\"姓名：张三\")\nprint(\"年龄：25\")\nprint(\"爱好：编程\")"
                }
            ]
        },
        "2": {
            "topic": "Python基础语法 - 变量与数据类型",
            "duration": "1-2小时",
            "objectives": "掌握Python变量声明和基本数据类型",
            "concepts": [
                {
                    "name": "变量",
                    "description": "变量是存储数据的容器",
                    "details": [
                        "不需要声明类型",
                        "遵循命名规则",
                        "区分大小写"
                    ]
                },
                {
                    "name": "基本数据类型",
                    "description": "Python的核心数据类型",
                    "details": [
                        "整数 (int)",
                        "浮点数 (float)",
                        "字符串 (str)",
                        "布尔值 (bool)"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "变量和数据类型示例",
                    "code": "# 整数\nage = 25\n\n# 浮点数\nheight = 1.75\n\n# 字符串\nname = \"小明\"\n\n# 布尔值\nis_student = True\n\nprint(f\"姓名：{name}\")\nprint(f\"年龄：{age}\")\nprint(f\"身高：{height}m\")\nprint(f\"是学生：{is_student}\")",
                    "explanation": "演示了Python四种基本数据类型的使用方法"
                }
            ],
            "exercises": [
                {
                    "title": "练习：计算圆的面积",
                    "description": "定义半径变量，计算并打印圆的面积（π ≈ 3.14159）",
                    "hint": "面积 = π × 半径²",
                    "solution": "pi = 3.14159\nradius = 5\narea = pi * radius * radius\nprint(f\"半径为 {radius} 的圆的面积是：{area}\")"
                }
            ]
        },
        "3": {
            "topic": "Python运算符",
            "duration": "1-2小时",
            "objectives": "掌握Python中的各种运算符",
            "concepts": [
                {
                    "name": "算术运算符",
                    "description": "用于数学计算的运算符",
                    "details": [
                        "+ 加法",
                        "- 减法", 
                        "* 乘法",
                        "/ 除法",
                        "// 整除",
                        "% 取余",
                        "** 幂运算"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "算术运算示例",
                    "code": "a = 10\nb = 3\n\nprint(f\"加法：{a} + {b} = {a + b}\")\nprint(f\"减法：{a} - {b} = {a - b}\")\nprint(f\"乘法：{a} * {b} = {a * b}\")\nprint(f\"除法：{a} / {b} = {a / b}\")\nprint(f\"整除：{a} // {b} = {a // b}\")\nprint(f\"取余：{a} % {b} = {a % b}\")\nprint(f\"幂运算：{a} ** {b} = {a ** b}\")",
                    "explanation": "展示了Python中所有算术运算符的使用"
                }
            ],
            "exercises": [
                {
                    "title": "练习：简单计算器",
                    "description": "编写程序计算两个数的加、减、乘、除运算",
                    "hint": "定义两个变量，然后进行四则运算",
                    "solution": "num1 = 15\nnum2 = 4\n\nprint(f\"{num1} + {num2} = {num1 + num2}\")\nprint(f\"{num1} - {num2} = {num1 - num2}\")\nprint(f\"{num1} * {num2} = {num1 * num2}\")\nprint(f\"{num1} / {num2} = {num1 / num2}\")"
                }
            ]
        }
    } 