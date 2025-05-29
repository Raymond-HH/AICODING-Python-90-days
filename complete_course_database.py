#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完整课程内容数据库
包含90天课程的详细学习内容
"""

def get_complete_course_database():
    """获取完整的课程数据库"""
    return {
        # 第1周：Python基础入门
        "1": {
            "topic": "Python简介与环境搭建",
            "duration": "1-1.5小时",
            "objectives": "了解Python语言特点，完成开发环境搭建",
            "concepts": [
                {
                    "name": "Python语言简介",
                    "description": "Python是一种高级、解释型、动态类型的编程语言。",
                    "details": [
                        "由Guido van Rossum于1989年发明，1991年首次发布",
                        "设计哲学强调代码的可读性和简洁性",
                        "语法简洁，学习曲线平缓，适合初学者",
                        "应用广泛：Web开发、数据科学、人工智能、自动化等"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "第一个Python程序",
                    "code": "print('Hello, World!')\nprint('欢迎来到Python的世界！')",
                    "explanation": "print()是Python的内置函数，用于输出文本到屏幕"
                }
            ],
            "exercises": [
                {
                    "title": "个人介绍程序",
                    "description": "编写程序输出你的个人信息",
                    "hint": "使用多个print()语句",
                    "solution": "print('姓名：张三')\nprint('年龄：20岁')\nprint('爱好：编程、读书')"
                }
            ]
        },
        
        "2": {
            "topic": "变量与数据类型",
            "duration": "1.5小时",
            "objectives": "掌握Python基本数据类型和变量使用",
            "concepts": [
                {
                    "name": "变量概念",
                    "description": "变量是存储数据的容器，像一个贴着标签的盒子。",
                    "details": [
                        "变量名是标签，变量值是盒子里的内容",
                        "Python中变量不需要声明类型",
                        "变量名只能包含字母、数字和下划线",
                        "不能以数字开头，区分大小写"
                    ]
                },
                {
                    "name": "基本数据类型",
                    "description": "Python内置的几种基本数据类型。",
                    "details": [
                        "int：整数，如 42, -17, 0",
                        "float：浮点数，如 3.14, -0.5, 2.0",
                        "str：字符串，如 'Hello', \"Python\"",
                        "bool：布尔值，只有 True 和 False"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "创建和使用变量",
                    "code": "# 创建变量\nname = 'Alice'\nage = 25\nheight = 1.68\nis_student = True\n\n# 输出变量\nprint('姓名:', name)\nprint('年龄:', age)\nprint('身高:', height)\nprint('是否学生:', is_student)",
                    "explanation": "展示了如何创建不同类型的变量并输出它们的值"
                },
                {
                    "title": "类型检查和转换",
                    "code": "# 检查变量类型\nprint(type(name))    # <class 'str'>\nprint(type(age))     # <class 'int'>\n\n# 类型转换\nage_str = str(age)   # 数字转字符串\nprint('我今年' + age_str + '岁')\n\n# 字符串转数字\nscore = '85'\nscore_num = int(score)\nprint('分数:', score_num)",
                    "explanation": "演示了如何检查变量类型和进行类型转换"
                }
            ],
            "exercises": [
                {
                    "title": "个人信息管理",
                    "description": "创建变量存储你的个人信息，并输出格式化的信息",
                    "hint": "包括姓名、年龄、身高、是否学生等信息",
                    "solution": "name = '李明'\nage = 22\nheight = 1.75\nis_student = True\ncity = '北京'\n\nprint('=== 个人信息 ===')\nprint(f'姓名: {name}')\nprint(f'年龄: {age}岁')\nprint(f'身高: {height}米')\nprint(f'学生: {\"是\" if is_student else \"否\"}')\nprint(f'城市: {city}')"
                }
            ]
        },
        
        "3": {
            "topic": "运算符与表达式",
            "duration": "1.5小时",
            "objectives": "掌握Python中各种运算符的使用",
            "concepts": [
                {
                    "name": "算术运算符",
                    "description": "用于数学计算的运算符。",
                    "details": [
                        "+ 加法：5 + 3 = 8",
                        "- 减法：5 - 3 = 2", 
                        "* 乘法：5 * 3 = 15",
                        "/ 除法：5 / 3 = 1.666... (结果为浮点数)",
                        "// 整除：5 // 3 = 1 (只保留整数部分)",
                        "% 取余：5 % 3 = 2 (余数)",
                        "** 幂运算：5 ** 3 = 125 (5的3次方)"
                    ]
                },
                {
                    "name": "比较运算符",
                    "description": "用于比较两个值，返回布尔值。",
                    "details": [
                        "== 等于：5 == 5 为 True",
                        "!= 不等于：5 != 3 为 True",
                        "> 大于：5 > 3 为 True",
                        "< 小于：5 < 3 为 False",
                        ">= 大于等于：5 >= 5 为 True",
                        "<= 小于等于：3 <= 5 为 True"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "算术运算实例",
                    "code": "a = 10\nb = 3\n\nprint(f'{a} + {b} = {a + b}')    # 13\nprint(f'{a} - {b} = {a - b}')    # 7\nprint(f'{a} * {b} = {a * b}')    # 30\nprint(f'{a} / {b} = {a / b:.2f}') # 3.33\nprint(f'{a} // {b} = {a // b}')  # 3\nprint(f'{a} % {b} = {a % b}')    # 1\nprint(f'{a} ** {b} = {a ** b}')  # 1000",
                    "explanation": "展示了所有算术运算符的使用方法和结果"
                }
            ],
            "exercises": [
                {
                    "title": "几何计算器",
                    "description": "计算圆形的面积和周长",
                    "hint": "面积 = π × r²，周长 = 2 × π × r",
                    "solution": "import math\n\nradius = 5\npi = math.pi\n\narea = pi * radius ** 2\ncircumference = 2 * pi * radius\n\nprint(f'半径: {radius}')\nprint(f'面积: {area:.2f}')\nprint(f'周长: {circumference:.2f}')"
                }
            ]
        },
        
        "4": {
            "topic": "字符串处理基础",
            "duration": "1.5小时",
            "objectives": "掌握字符串的基本操作和格式化",
            "concepts": [
                {
                    "name": "字符串创建",
                    "description": "Python中创建字符串的不同方式。",
                    "details": [
                        "单引号: 'Hello'",
                        "双引号: \"Hello\"",
                        "三引号: '''多行字符串'''",
                        "原始字符串: r'C:\\Users'",
                        "转义字符: \\n(换行), \\t(制表符)"
                    ]
                },
                {
                    "name": "字符串操作",
                    "description": "对字符串进行各种操作的方法。",
                    "details": [
                        "拼接: 'Hello' + ' World'",
                        "重复: 'Ha' * 3 = 'HaHaHa'",
                        "索引: text[0] 获取第一个字符",
                        "切片: text[1:4] 获取子字符串",
                        "长度: len(text) 获取字符串长度"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "字符串基本操作",
                    "code": "text = 'Python Programming'\n\n# 字符串信息\nprint(f'字符串: {text}')\nprint(f'长度: {len(text)}')\nprint(f'第一个字符: {text[0]}')\nprint(f'最后一个字符: {text[-1]}')\n\n# 字符串切片\nprint(f'前6个字符: {text[:6]}')\nprint(f'后11个字符: {text[7:]}')\nprint(f'反转: {text[::-1]}')",
                    "explanation": "展示了字符串的索引、切片和基本信息获取"
                },
                {
                    "title": "字符串格式化",
                    "code": "name = 'Alice'\nage = 25\nscore = 88.5\n\n# f-string格式化（推荐）\nprint(f'姓名: {name}')\nprint(f'年龄: {age}岁')\nprint(f'分数: {score:.1f}分')\n\n# format方法\nprint('{}今年{}岁'.format(name, age))\n\n# 旧式%格式化\nprint('%s的分数是%.2f' % (name, score))",
                    "explanation": "展示了Python中三种主要的字符串格式化方法"
                }
            ],
            "exercises": [
                {
                    "title": "姓名处理器",
                    "description": "从全名中分离姓氏和名字",
                    "hint": "假设姓名格式为'姓 名'，使用空格分割",
                    "solution": "full_name = '张 小明'\n\n# 方法1: 使用find和切片\nspace_pos = full_name.find(' ')\nfamily_name = full_name[:space_pos]\ngiven_name = full_name[space_pos+1:]\n\nprint(f'姓氏: {family_name}')\nprint(f'名字: {given_name}')\n\n# 方法2: 使用split\nparts = full_name.split(' ')\nprint(f'姓氏: {parts[0]}')\nprint(f'名字: {parts[1]}')"
                }
            ]
        },
        
        "5": {
            "topic": "用户输入与输出",
            "duration": "1.5小时", 
            "objectives": "掌握程序与用户的交互方式",
            "concepts": [
                {
                    "name": "input()函数",
                    "description": "获取用户输入的函数。",
                    "details": [
                        "input()总是返回字符串类型",
                        "可以提供提示信息：input('请输入姓名: ')",
                        "需要类型转换：int(input('年龄: '))",
                        "空输入返回空字符串",
                        "输入错误需要处理异常"
                    ]
                },
                {
                    "name": "print()函数高级用法",
                    "description": "输出函数的高级参数。",
                    "details": [
                        "sep参数: print('a', 'b', sep='-')",
                        "end参数: print('Hello', end=' ')",
                        "file参数: 指定输出位置",
                        "flush参数: 立即刷新输出缓冲区"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "用户信息收集",
                    "code": "print('=== 用户信息收集 ===')\n\n# 获取用户输入\nname = input('请输入姓名: ')\nage_str = input('请输入年龄: ')\n\ntry:\n    age = int(age_str)\n    print(f'\\n你好 {name}，你今年 {age} 岁')\n    \n    # 判断年龄段\n    if age < 18:\n        print('你还是未成年人')\n    else:\n        print('你已经成年了')\n        \nexcept ValueError:\n    print('年龄必须是数字！')",
                    "explanation": "展示了如何安全地获取和处理用户输入"
                }
            ],
            "exercises": [
                {
                    "title": "简单计算器",
                    "description": "创建一个计算器，让用户输入两个数字和运算符",
                    "hint": "处理除零错误和无效输入",
                    "solution": "print('=== 简单计算器 ===')\n\ntry:\n    num1 = float(input('第一个数字: '))\n    operator = input('运算符(+,-,*,/): ')\n    num2 = float(input('第二个数字: '))\n    \n    if operator == '+':\n        result = num1 + num2\n    elif operator == '-':\n        result = num1 - num2\n    elif operator == '*':\n        result = num1 * num2\n    elif operator == '/':\n        if num2 != 0:\n            result = num1 / num2\n        else:\n            print('错误：除数不能为零')\n            exit()\n    else:\n        print('无效的运算符')\n        exit()\n    \n    print(f'{num1} {operator} {num2} = {result}')\n    \nexcept ValueError:\n    print('请输入有效的数字')"
                }
            ]
        },
        
        "6": {
            "topic": "条件语句",
            "duration": "1.5小时",
            "objectives": "掌握程序的条件控制结构",
            "concepts": [
                {
                    "name": "if语句",
                    "description": "根据条件执行不同的代码块。",
                    "details": [
                        "if condition: 当条件为True时执行",
                        "else: 当if条件为False时执行",
                        "elif: 检查多个条件",
                        "条件可以是比较、逻辑运算等",
                        "代码块用缩进表示（建议4个空格）"
                    ]
                },
                {
                    "name": "复合条件",
                    "description": "使用逻辑运算符组合多个条件。",
                    "details": [
                        "and: 所有条件都为True",
                        "or: 至少一个条件为True", 
                        "not: 取反，True变False",
                        "括号可以改变优先级",
                        "短路求值：and遇False停止，or遇True停止"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "成绩等级判断",
                    "code": "score = 85\n\nif score >= 90:\n    grade = 'A'\n    comment = '优秀！'\nelif score >= 80:\n    grade = 'B' \n    comment = '良好！'\nelif score >= 70:\n    grade = 'C'\n    comment = '中等'\nelif score >= 60:\n    grade = 'D'\n    comment = '及格'\nelse:\n    grade = 'F'\n    comment = '不及格'\n\nprint(f'分数: {score}')\nprint(f'等级: {grade}')\nprint(f'评价: {comment}')",
                    "explanation": "展示了多分支条件判断的使用方法"
                }
            ],
            "exercises": [
                {
                    "title": "登录验证系统",
                    "description": "创建简单的用户名密码验证",
                    "hint": "预设正确的用户名和密码",
                    "solution": "# 预设的正确账号\ncorrect_username = 'admin'\ncorrect_password = '123456'\n\nprint('=== 登录系统 ===')\nusername = input('用户名: ')\npassword = input('密码: ')\n\nif username == correct_username and password == correct_password:\n    print('✅ 登录成功！欢迎使用系统')\nelif username == correct_username:\n    print('❌ 密码错误！')\nelif password == correct_password:\n    print('❌ 用户名错误！')\nelse:\n    print('❌ 用户名和密码都错误！')"
                }
            ]
        },
        
        "7": {
            "topic": "第一周复习与项目",
            "duration": "2小时",
            "objectives": "巩固第一周学习内容，完成计算器项目",
            "concepts": [
                {
                    "name": "知识点回顾",
                    "description": "回顾第一周学习的核心概念。",
                    "details": [
                        "变量和数据类型的使用",
                        "运算符的优先级和使用场景",
                        "字符串处理的常用方法",
                        "用户输入输出的最佳实践",
                        "条件语句的嵌套和组合"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "综合应用示例",
                    "code": "# 用户信息管理综合示例\nprint('=== 用户信息管理系统 ===')\n\n# 获取用户输入\nname = input('姓名: ')\nage = int(input('年龄: '))\nemail = input('邮箱: ')\n\n# 数据验证和处理\nif '@' in email and '.' in email:\n    email_valid = True\nelse:\n    email_valid = False\n    \n# 年龄分类\nif age < 18:\n    category = '未成年人'\nelif age < 60:\n    category = '成年人'\nelse:\n    category = '老年人'\n\n# 输出格式化信息\nprint('\\n=== 用户信息确认 ===')\nprint(f'姓名: {name.title()}')\nprint(f'年龄: {age}岁 ({category})')\nprint(f'邮箱: {email} ({\"有效\" if email_valid else \"无效\"})')",
                    "explanation": "综合运用了第一周学习的所有知识点"
                }
            ],
            "exercises": [
                {
                    "title": "完整计算器项目",
                    "description": "创建一个功能完整的计算器程序",
                    "hint": "包含错误处理、菜单选择、循环功能",
                    "solution": "def calculator():\n    print('🧮 欢迎使用计算器！')\n    \n    while True:\n        print('\\n=== 操作菜单 ===')\n        print('1. 加法')\n        print('2. 减法')\n        print('3. 乘法')\n        print('4. 除法')\n        print('0. 退出')\n        \n        choice = input('请选择操作(0-4): ')\n        \n        if choice == '0':\n            print('感谢使用！')\n            break\n            \n        if choice in ['1', '2', '3', '4']:\n            try:\n                num1 = float(input('第一个数: '))\n                num2 = float(input('第二个数: '))\n                \n                if choice == '1':\n                    result = num1 + num2\n                    op = '+'\n                elif choice == '2':\n                    result = num1 - num2\n                    op = '-'\n                elif choice == '3':\n                    result = num1 * num2\n                    op = '*'\n                elif choice == '4':\n                    if num2 != 0:\n                        result = num1 / num2\n                        op = '/'\n                    else:\n                        print('错误：除数不能为零！')\n                        continue\n                \n                print(f'结果: {num1} {op} {num2} = {result}')\n                \n            except ValueError:\n                print('错误：请输入有效数字！')\n        else:\n            print('无效选择！')\n\n# calculator()  # 取消注释运行"
                }
            ]
        }
    }

if __name__ == "__main__":
    # 测试数据库
    database = get_complete_course_database()
    print(f"课程数据库包含 {len(database)} 天的内容")
    for day, content in database.items():
        print(f"第{day}天: {content['topic']}") 