#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
课程内容管理器
管理和生成详细的每日学习内容
"""

def get_day_4_content():
    """第4天：字符串处理基础"""
    return {
        "topic": "字符串处理基础",
        "duration": "1.5小时",
        "objectives": "掌握字符串的基本操作和格式化",
        "concepts": [
            {
                "name": "字符串创建方式",
                "description": "Python中有多种方式创建字符串，每种方式都有其特定的用途。",
                "details": [
                    "单引号 ('string')：最常用的方式",
                    "双引号 (\"string\")：当字符串包含单引号时使用",
                    "三引号 ('''string''' 或 \"\"\"string\"\"\")：用于多行字符串",
                    "原始字符串 (r'string')：忽略转义字符",
                    "转义字符：\\n(换行)、\\t(制表符)、\\\\(反斜杠)、\\'(单引号)"
                ]
            },
            {
                "name": "字符串索引和切片",
                "description": "字符串中的每个字符都有一个位置索引，可以通过索引访问单个字符或字符串片段。",
                "details": [
                    "正向索引：从0开始，string[0]是第一个字符",
                    "负向索引：从-1开始，string[-1]是最后一个字符",
                    "切片语法：string[start:end:step]",
                    "切片不包含结束位置的字符",
                    "省略参数的含义：[:end]从开头、[start:]到结尾、[:]复制整个字符串"
                ]
            },
            {
                "name": "字符串格式化",
                "description": "将变量值插入到字符串中的不同方法，让字符串更加动态。",
                "details": [
                    "% 格式化：'Hello %s' % name (旧式方法)",
                    ".format() 方法：'Hello {}'.format(name)",
                    "f-string：f'Hello {name}' (Python 3.6+推荐)",
                    "格式化选项：{:.2f}保留两位小数、{:>10}右对齐等"
                ]
            }
        ],
        "examples": [
            {
                "title": "字符串创建和基本操作",
                "code": "# 不同方式创建字符串\nsingle_quote = 'Hello Python'\ndouble_quote = \"It's a beautiful day\"\nmulti_line = '''这是一个\n多行字符串\n示例'''\nraw_string = r'C:\\Users\\name\\Documents'\n\nprint(single_quote)\nprint(double_quote)\nprint(multi_line)\nprint(raw_string)\n\n# 字符串拼接和重复\nfirst_name = 'Zhang'\nlast_name = 'San'\nfull_name = first_name + ' ' + last_name\nprint(full_name)  # Zhang San\n\n# 字符串重复\nrepeat = 'Python! ' * 3\nprint(repeat)  # Python! Python! Python!",
                "explanation": "展示了Python中创建字符串的各种方法和基本操作"
            },
            {
                "title": "字符串索引和切片",
                "code": "text = 'Python Programming'\nprint(f'字符串长度: {len(text)}')  # 18\n\n# 索引访问\nprint(f'第一个字符: {text[0]}')     # P\nprint(f'最后一个字符: {text[-1]}')   # g\nprint(f'第7个字符: {text[6]}')      # (空格)\n\n# 字符串切片\nprint(f'前6个字符: {text[:6]}')     # Python\nprint(f'后11个字符: {text[7:]}')     # Programming\nprint(f'中间部分: {text[7:18]}')     # Programming\nprint(f'每隔一个字符: {text[::2]}')  # Pto rgamn\nprint(f'反转字符串: {text[::-1]}')   # gnimmargorP nohtyP",
                "explanation": "字符串索引从0开始，切片可以提取字符串的任意部分"
            },
            {
                "title": "字符串格式化方法",
                "code": "name = 'Alice'\nage = 25\nscore = 88.567\n\n# % 格式化（旧式）\nold_style = 'Name: %s, Age: %d' % (name, age)\nprint(old_style)\n\n# .format() 方法\nformat_style = 'Name: {}, Age: {}'.format(name, age)\nprint(format_style)\n\n# 带位置参数\nformat_pos = 'Name: {0}, Age: {1}, Score: {2:.2f}'.format(name, age, score)\nprint(format_pos)\n\n# f-string（推荐）\nf_string = f'Name: {name}, Age: {age}, Score: {score:.2f}'\nprint(f_string)\n\n# 格式化选项\nprint(f'分数: {score:.1f}')      # 保留1位小数\nprint(f'姓名: {name:>10}')       # 右对齐，宽度10\nprint(f'年龄: {age:03d}')        # 用0填充到3位",
                "explanation": "f-string是最现代和推荐的字符串格式化方法"
            },
            {
                "title": "常用字符串方法",
                "code": "text = '  Hello Python World  '\n\n# 大小写转换\nprint(f'大写: {text.upper()}')\nprint(f'小写: {text.lower()}')\nprint(f'首字母大写: {text.capitalize()}')\nprint(f'每个单词首字母大写: {text.title()}')\n\n# 去除空白\nprint(f'去除两端空白: \"{text.strip()}\"')\nprint(f'去除左端空白: \"{text.lstrip()}\"')\nprint(f'去除右端空白: \"{text.rstrip()}\"')\n\n# 替换和查找\nprint(f'替换: {text.replace(\"Python\", \"Java\")}')\nprint(f'查找位置: {text.find(\"Python\")}')\nprint(f'是否包含: {\"Python\" in text}')\n\n# 分割和连接\nwords = text.strip().split(' ')\nprint(f'分割成列表: {words}')\njoined = '-'.join(words)\nprint(f'连接: {joined}')",
                "explanation": "字符串方法不会修改原字符串，而是返回新的字符串"
            }
        ],
        "exercises": [
            {
                "title": "姓名处理程序",
                "description": "从用户输入的全名中提取姓氏和名字（假设格式为'姓 名'）",
                "hint": "使用字符串的find()和切片功能",
                "solution": "full_name = '张 小明'\n\n# 方法1：使用find()和切片\nspace_pos = full_name.find(' ')\nlast_name = full_name[:space_pos]\nfirst_name = full_name[space_pos + 1:]\n\nprint(f'姓氏: {last_name}')\nprint(f'名字: {first_name}')\n\n# 方法2：使用split()\nparts = full_name.split(' ')\nprint(f'姓氏: {parts[0]}')\nprint(f'名字: {parts[1]}')"
            },
            {
                "title": "文本统计器",
                "description": "统计一段文本中特定字符或单词的出现次数",
                "hint": "使用字符串的count()方法",
                "solution": "text = 'Python is powerful. Python is popular. Python is easy to learn.'\n\n# 统计字符\nchar_count = text.count('o')\nprint(f'字符\"o\"出现次数: {char_count}')\n\n# 统计单词（大小写敏感）\nword_count = text.count('Python')\nprint(f'单词\"Python\"出现次数: {word_count}')\n\n# 统计单词（忽略大小写）\nlower_text = text.lower()\nword_count_lower = lower_text.count('python')\nprint(f'\"Python\"(忽略大小写)出现次数: {word_count_lower}')\n\n# 统计句子\nsentence_count = text.count('.')\nprint(f'句子数量: {sentence_count}')"
            },
            {
                "title": "密码强度检查器",
                "description": "检查密码是否同时包含大写字母、小写字母和数字",
                "hint": "使用字符串方法检查各种条件",
                "solution": "password = 'MyPassword123'\n\n# 检查是否包含大写字母\nhas_upper = any(c.isupper() for c in password)\n\n# 检查是否包含小写字母\nhas_lower = any(c.islower() for c in password)\n\n# 检查是否包含数字\nhas_digit = any(c.isdigit() for c in password)\n\n# 检查长度\nmin_length = len(password) >= 8\n\nprint(f'密码: {password}')\nprint(f'包含大写字母: {has_upper}')\nprint(f'包含小写字母: {has_lower}')\nprint(f'包含数字: {has_digit}')\nprint(f'长度至少8位: {min_length}')\n\n# 综合判断\nis_strong = has_upper and has_lower and has_digit and min_length\nprint(f'密码强度: {\"强\" if is_strong else \"弱\"}')"
            },
            {
                "title": "文本格式化器",
                "description": "创建一个程序，美化输出个人信息表格",
                "hint": "使用字符串格式化创建对齐的表格",
                "solution": "# 个人信息数据\npeople = [\n    {'name': '张三', 'age': 25, 'score': 88.5},\n    {'name': '李四', 'age': 30, 'score': 92.3},\n    {'name': '王五', 'age': 28, 'score': 85.7}\n]\n\n# 打印表格标题\nprint('=' * 40)\nprint(f'{'姓名':^8} {'年龄':^8} {'分数':^8}')\nprint('=' * 40)\n\n# 打印每个人的信息\nfor person in people:\n    name = person['name']\n    age = person['age']\n    score = person['score']\n    print(f'{name:^8} {age:^8} {score:^8.1f}')\n\nprint('=' * 40)\n\n# 使用f-string的高级格式化\nfor person in people:\n    info = f\"姓名: {person['name']:<6} | 年龄: {person['age']:>3}岁 | 分数: {person['score']:6.2f}分\"\n    print(info)"
            }
        ]
    }

def get_day_5_content():
    """第5天：用户输入与输出"""
    return {
        "topic": "用户输入与输出",
        "duration": "1.5小时",
        "objectives": "掌握程序与用户的交互方式",
        "concepts": [
            {
                "name": "input()函数详解",
                "description": "input()函数是Python中获取用户输入的标准方法。",
                "details": [
                    "input()总是返回字符串类型",
                    "可以提供提示信息作为参数",
                    "输入的内容不包含换行符",
                    "空输入返回空字符串''",
                    "用户按Enter键结束输入"
                ]
            },
            {
                "name": "数据类型转换",
                "description": "由于input()返回字符串，通常需要转换为其他数据类型。",
                "details": [
                    "int()：转换为整数",
                    "float()：转换为浮点数",
                    "bool()：转换为布尔值",
                    "转换失败会抛出ValueError异常",
                    "可以使用try-except处理转换错误"
                ]
            },
            {
                "name": "print()函数高级用法",
                "description": "print()函数有多个参数可以控制输出格式。",
                "details": [
                    "sep参数：控制多个值之间的分隔符",
                    "end参数：控制输出结尾字符（默认是换行符）",
                    "file参数：指定输出目标（默认是屏幕）",
                    "flush参数：是否立即刷新输出缓冲区"
                ]
            }
        ],
        "examples": [
            {
                "title": "基本用户输入",
                "code": "# 获取用户基本信息\nname = input('请输入您的姓名: ')\nage_str = input('请输入您的年龄: ')\n\n# 类型转换\ntry:\n    age = int(age_str)\n    print(f'您好 {name}，您今年 {age} 岁')\n    \n    # 计算出生年份\n    from datetime import datetime\n    current_year = datetime.now().year\n    birth_year = current_year - age\n    print(f'您大约出生在 {birth_year} 年')\n    \nexcept ValueError:\n    print('年龄必须是数字！')",
                "explanation": "展示了如何获取用户输入并进行类型转换，同时处理可能的错误"
            },
            {
                "title": "多种数据类型输入",
                "code": "# 获取不同类型的数据\nprint('=== 个人信息收集 ===')\n\nname = input('姓名: ')\nage = int(input('年龄: '))\nheight = float(input('身高(米): '))\nis_student = input('是否是学生(y/n): ').lower() == 'y'\nhobbies = input('兴趣爱好(用逗号分隔): ').split(',')\n\n# 清理爱好列表（去除空格）\nhobbies = [hobby.strip() for hobby in hobbies]\n\n# 输出结果\nprint('\\n=== 信息确认 ===')\nprint(f'姓名: {name}')\nprint(f'年龄: {age}岁')\nprint(f'身高: {height:.2f}米')\nprint(f'学生身份: {\"是\" if is_student else \"否\"}')\nprint(f'兴趣爱好: {\", \".join(hobbies)}')",
                "explanation": "演示如何处理多种数据类型的输入，包括列表数据的处理"
            },
            {
                "title": "print()函数高级用法",
                "code": "# sep参数：控制分隔符\nprint('Python', 'Java', 'C++', sep=' | ')\nprint('2024', '12', '25', sep='-')\n\n# end参数：控制结尾字符\nprint('加载中', end='')\nfor i in range(5):\n    print('.', end='', flush=True)\n    import time\n    time.sleep(0.5)\nprint(' 完成！')\n\n# 多个参数组合使用\nfruits = ['苹果', '香蕉', '橙子']\nprint('我喜欢的水果:', *fruits, sep=' 🍎 ', end=' 😋\\n')\n\n# 格式化输出表格\nheader = ['姓名', '年龄', '城市']\ndata = [['张三', 25, '北京'], ['李四', 30, '上海']]\n\nprint(*header, sep='\\t\\t')\nprint('-' * 30)\nfor row in data:\n    print(*row, sep='\\t\\t')",
                "explanation": "展示print()函数的高级参数用法，可以创建更灵活的输出格式"
            },
            {
                "title": "交互式菜单程序",
                "code": "# 简单的交互式菜单\ndef show_menu():\n    print('\\n=== 简单计算器 ===')\n    print('1. 加法')\n    print('2. 减法')\n    print('3. 乘法')\n    print('4. 除法')\n    print('0. 退出')\n    print('===================')\n\ndef calculator():\n    while True:\n        show_menu()\n        choice = input('请选择操作(0-4): ')\n        \n        if choice == '0':\n            print('感谢使用，再见！')\n            break\n        elif choice in ['1', '2', '3', '4']:\n            try:\n                num1 = float(input('请输入第一个数字: '))\n                num2 = float(input('请输入第二个数字: '))\n                \n                if choice == '1':\n                    result = num1 + num2\n                    op = '+'\n                elif choice == '2':\n                    result = num1 - num2\n                    op = '-'\n                elif choice == '3':\n                    result = num1 * num2\n                    op = '*'\n                elif choice == '4':\n                    if num2 != 0:\n                        result = num1 / num2\n                        op = '/'\n                    else:\n                        print('错误：除数不能为零！')\n                        continue\n                \n                print(f'结果: {num1} {op} {num2} = {result}')\n                \n            except ValueError:\n                print('错误：请输入有效的数字！')\n        else:\n            print('无效选择，请重新输入！')\n\n# 运行计算器\n# calculator()  # 取消注释运行",
                "explanation": "展示如何创建交互式程序，结合用户输入和菜单选择"
            }
        ],
        "exercises": [
            {
                "title": "温度转换器",
                "description": "制作一个温度转换程序，可以在摄氏度和华氏度之间转换",
                "hint": "摄氏度转华氏度：F = C * 9/5 + 32",
                "solution": "def temperature_converter():\n    print('=== 温度转换器 ===')\n    print('1. 摄氏度转华氏度')\n    print('2. 华氏度转摄氏度')\n    \n    choice = input('请选择转换方式(1/2): ')\n    \n    try:\n        if choice == '1':\n            celsius = float(input('请输入摄氏度: '))\n            fahrenheit = celsius * 9/5 + 32\n            print(f'{celsius}°C = {fahrenheit:.2f}°F')\n        elif choice == '2':\n            fahrenheit = float(input('请输入华氏度: '))\n            celsius = (fahrenheit - 32) * 5/9\n            print(f'{fahrenheit}°F = {celsius:.2f}°C')\n        else:\n            print('无效选择！')\n    except ValueError:\n        print('请输入有效的数字！')\n\n# temperature_converter()"
            },
            {
                "title": "BMI计算器",
                "description": "创建BMI（身体质量指数）计算器，根据身高体重计算BMI并给出健康建议",
                "hint": "BMI = 体重(kg) / 身高(m)²",
                "solution": "def bmi_calculator():\n    print('=== BMI计算器 ===')\n    \n    try:\n        weight = float(input('请输入体重(公斤): '))\n        height = float(input('请输入身高(米): '))\n        \n        # 计算BMI\n        bmi = weight / (height ** 2)\n        \n        # 判断BMI等级\n        if bmi < 18.5:\n            category = '偏瘦'\n            advice = '建议增加营养，适当增重'\n        elif bmi < 24:\n            category = '正常'\n            advice = '继续保持健康的生活方式'\n        elif bmi < 28:\n            category = '偏胖'\n            advice = '建议控制饮食，增加运动'\n        else:\n            category = '肥胖'\n            advice = '建议咨询医生，制定减重计划'\n        \n        print(f'\\n=== BMI结果 ===')\n        print(f'体重: {weight} kg')\n        print(f'身高: {height} m')\n        print(f'BMI: {bmi:.2f}')\n        print(f'分类: {category}')\n        print(f'建议: {advice}')\n        \n    except ValueError:\n        print('请输入有效的数字！')\n    except ZeroDivisionError:\n        print('身高不能为零！')\n\n# bmi_calculator()"
            },
            {
                "title": "学生成绩录入系统",
                "description": "创建一个程序录入多个学生的成绩，计算平均分，找出最高分和最低分",
                "hint": "使用循环录入多个学生信息",
                "solution": "def grade_system():\n    print('=== 学生成绩录入系统 ===')\n    \n    students = []\n    \n    while True:\n        print(f'\\n正在录入第{len(students) + 1}个学生信息')\n        name = input('学生姓名 (输入quit退出): ')\n        \n        if name.lower() == 'quit':\n            break\n        \n        try:\n            score = float(input('学生成绩: '))\n            \n            if 0 <= score <= 100:\n                students.append({'name': name, 'score': score})\n                print(f'{name}的成绩已录入！')\n            else:\n                print('成绩应在0-100之间！')\n                \n        except ValueError:\n            print('请输入有效的数字！')\n    \n    if students:\n        # 计算统计信息\n        scores = [s['score'] for s in students]\n        avg_score = sum(scores) / len(scores)\n        max_score = max(scores)\n        min_score = min(scores)\n        \n        # 找出最高分和最低分的学生\n        top_student = next(s for s in students if s['score'] == max_score)\n        bottom_student = next(s for s in students if s['score'] == min_score)\n        \n        print(f'\\n=== 成绩统计 ===')\n        print(f'学生人数: {len(students)}')\n        print(f'平均分: {avg_score:.2f}')\n        print(f'最高分: {max_score} ({top_student[\"name\"]})')\n        print(f'最低分: {min_score} ({bottom_student[\"name\"]})')\n        \n        print(f'\\n=== 所有学生成绩 ===')\n        for student in students:\n            print(f'{student[\"name\"]}: {student[\"score\"]}分')\n    else:\n        print('没有录入任何学生信息！')\n\n# grade_system()"
            }
        ]
    }

def get_day_6_content():
    """第6天：条件语句"""
    return {
        "topic": "条件语句",
        "duration": "1.5小时",
        "objectives": "掌握程序的条件控制结构",
        "concepts": [
            {
                "name": "条件语句基础",
                "description": "条件语句允许程序根据不同条件执行不同的代码分支。",
                "details": [
                    "if语句：当条件为True时执行",
                    "else语句：当if条件为False时执行",
                    "elif语句：检查多个条件",
                    "条件表达式必须返回布尔值",
                    "代码块用缩进表示（通常4个空格）"
                ]
            },
            {
                "name": "条件表达式",
                "description": "用于判断的表达式，结果为True或False。",
                "details": [
                    "比较运算符：==、!=、>、<、>=、<=",
                    "逻辑运算符：and、or、not",
                    "成员运算符：in、not in",
                    "身份运算符：is、is not",
                    "布尔值的隐式转换"
                ]
            },
            {
                "name": "嵌套条件和复杂判断",
                "description": "在条件语句内部使用其他条件语句，或组合多个条件。",
                "details": [
                    "嵌套if语句：if内部包含if",
                    "多条件组合：使用and、or连接",
                    "条件的短路求值",
                    "三元运算符：value = a if condition else b"
                ]
            }
        ],
        "examples": [
            {
                "title": "基本条件语句",
                "code": "# 基本if语句\nage = 18\n\nif age >= 18:\n    print('您已成年，可以投票')\n\n# if-else语句\nscore = 85\n\nif score >= 60:\n    print('考试通过')\nelse:\n    print('考试未通过，需要补考')\n\n# if-elif-else语句\ntemperature = 25\n\nif temperature < 0:\n    print('结冰了，很冷！')\nelif temperature < 15:\n    print('有点冷，多穿点衣服')\nelif temperature < 25:\n    print('温度适宜')\nelif temperature < 35:\n    print('有点热')\nelse:\n    print('太热了！')",
                "explanation": "展示了条件语句的基本语法和多分支判断"
            },
            {
                "title": "复杂条件判断",
                "code": "# 复杂条件组合\nusername = 'admin'\npassword = '123456'\nage = 25\nis_vip = True\n\n# 登录验证\nif username == 'admin' and password == '123456':\n    print('登录成功！')\n    \n    # 嵌套条件\n    if age >= 18:\n        print('欢迎访问成人内容')\n    else:\n        print('您是未成年用户')\n        \n    if is_vip:\n        print('VIP用户，享受特殊权限')\nelse:\n    print('用户名或密码错误！')\n\n# 成员运算符\nvalid_users = ['admin', 'user1', 'user2']\nif username in valid_users:\n    print(f'{username} 是有效用户')\n\n# 多条件判断（成绩等级）\nscore = 88\n\nif score >= 90:\n    grade = 'A'\nelif score >= 80:\n    grade = 'B'\nelif score >= 70:\n    grade = 'C'\nelif score >= 60:\n    grade = 'D'\nelse:\n    grade = 'F'\n\nprint(f'分数: {score}, 等级: {grade}')",
                "explanation": "展示了复杂条件的组合和嵌套使用"
            },
            {
                "title": "三元运算符和特殊判断",
                "code": "# 三元运算符（条件表达式）\nage = 20\nstatus = '成年人' if age >= 18 else '未成年人'\nprint(f'年龄{age}岁，身份：{status}')\n\n# 更复杂的三元运算符\nscore = 75\nresult = '优秀' if score >= 90 else '良好' if score >= 80 else '及格' if score >= 60 else '不及格'\nprint(f'成绩：{result}')\n\n# 布尔值的隐式转换\nname = input('请输入姓名: ')\nif name:  # 非空字符串为True\n    print(f'欢迎，{name}！')\nelse:\n    print('您没有输入姓名')\n\n# 数字的布尔转换\nnumber = int(input('请输入一个数字: '))\nif number:  # 非零数字为True\n    print('这是一个非零数字')\nelse:\n    print('这是零')\n\n# 列表的布尔转换\nmy_list = []\nif my_list:  # 非空列表为True\n    print('列表有内容')\nelse:\n    print('列表为空')",
                "explanation": "展示了三元运算符和Python中布尔值的隐式转换规则"
            },
            {
                "title": "实际应用：用户权限系统",
                "code": "# 用户权限系统示例\ndef check_permission(user_type, age, is_verified):\n    print(f'检查用户权限: 类型={user_type}, 年龄={age}, 已验证={is_verified}')\n    \n    # 管理员权限\n    if user_type == 'admin':\n        print('✅ 管理员：拥有所有权限')\n        return True\n    \n    # 普通用户权限检查\n    elif user_type == 'user':\n        if not is_verified:\n            print('❌ 账户未验证，权限受限')\n            return False\n        \n        if age < 13:\n            print('❌ 年龄过小，无法使用')\n            return False\n        elif age < 18:\n            print('⚠️ 未成年用户，部分功能受限')\n            return True\n        else:\n            print('✅ 成年用户，正常权限')\n            return True\n    \n    # 访客权限\n    elif user_type == 'guest':\n        print('ℹ️ 访客用户，仅基础功能')\n        return True\n    \n    else:\n        print('❌ 未知用户类型')\n        return False\n\n# 测试不同用户\nusers = [\n    ('admin', 30, True),\n    ('user', 25, True),\n    ('user', 16, True),\n    ('user', 20, False),\n    ('guest', 0, False),\n    ('unknown', 25, True)\n]\n\nfor user_type, age, is_verified in users:\n    print('\\n' + '='*40)\n    has_permission = check_permission(user_type, age, is_verified)\n    print(f'权限结果: {\"通过\" if has_permission else \"拒绝\"}')",
                "explanation": "展示了如何在实际项目中使用复杂的条件判断"
            }
        ],
        "exercises": [
            {
                "title": "成绩等级系统",
                "description": "编写程序根据分数给出等级：90-100为A，80-89为B，70-79为C，60-69为D，60以下为F",
                "hint": "使用if-elif-else结构",
                "solution": "def grade_system():\n    try:\n        score = float(input('请输入分数(0-100): '))\n        \n        if score < 0 or score > 100:\n            print('分数应该在0-100之间！')\n            return\n        \n        if score >= 90:\n            grade = 'A'\n            comment = '优秀！'\n        elif score >= 80:\n            grade = 'B'\n            comment = '良好！'\n        elif score >= 70:\n            grade = 'C'\n            comment = '中等'\n        elif score >= 60:\n            grade = 'D'\n            comment = '及格'\n        else:\n            grade = 'F'\n            comment = '不及格，需要努力！'\n        \n        print(f'分数: {score}')\n        print(f'等级: {grade}')\n        print(f'评价: {comment}')\n        \n    except ValueError:\n        print('请输入有效的数字！')\n\n# grade_system()"
            },
            {
                "title": "简单登录系统",
                "description": "创建一个登录系统，验证用户名和密码，给出相应的提示",
                "hint": "可以预设几个用户账号",
                "solution": "def login_system():\n    # 预设的用户账号\n    users = {\n        'admin': 'admin123',\n        'user1': 'password1',\n        'user2': 'password2'\n    }\n    \n    print('=== 用户登录系统 ===')\n    username = input('用户名: ')\n    password = input('密码: ')\n    \n    # 检查用户名是否存在\n    if username in users:\n        # 检查密码是否正确\n        if users[username] == password:\n            print(f'✅ 登录成功！欢迎，{username}！')\n            \n            # 根据用户类型给予不同权限\n            if username == 'admin':\n                print('🔑 您是管理员，拥有所有权限')\n            else:\n                print('👤 您是普通用户')\n        else:\n            print('❌ 密码错误！')\n    else:\n        print('❌ 用户名不存在！')\n    \n    # 显示所有可用账号（仅用于演示）\n    print('\\n提示：可用账号有:')\n    for user in users.keys():\n        print(f'  用户名: {user}')\n\n# login_system()"
            },
            {
                "title": "年龄分组程序",
                "description": "根据年龄将人员分组：0-12儿童，13-17青少年，18-59成年人，60+老年人",
                "hint": "考虑边界条件和异常情况",
                "solution": "def age_classifier():\n    try:\n        age = int(input('请输入年龄: '))\n        \n        if age < 0:\n            print('年龄不能为负数！')\n        elif age > 150:\n            print('年龄超出合理范围！')\n        elif age <= 12:\n            category = '儿童'\n            description = '纯真快乐的年纪'\n        elif age <= 17:\n            category = '青少年'\n            description = '青春活力的时期'\n        elif age <= 59:\n            category = '成年人'\n            description = '人生的黄金阶段'\n        else:\n            category = '老年人'\n            description = '智慧丰富的长者'\n        \n        if 0 <= age <= 150:\n            print(f'年龄: {age}岁')\n            print(f'分类: {category}')\n            print(f'特点: {description}')\n            \n            # 额外信息\n            if age >= 18:\n                print('✅ 已达到法定成年年龄')\n            else:\n                print('ℹ️ 未成年人，需要监护人照顾')\n            \n            if age >= 60:\n                print('🎉 可以享受老年人优惠政策')\n                \n    except ValueError:\n        print('请输入有效的整数！')\n\n# age_classifier()"
            },
            {
                "title": "数字比较游戏",
                "description": "让用户输入三个数字，找出最大值、最小值，并判断它们的关系",
                "hint": "使用嵌套条件判断三个数的大小关系",
                "solution": "def number_comparison():\n    try:\n        print('请输入三个数字：')\n        num1 = float(input('第一个数字: '))\n        num2 = float(input('第二个数字: '))\n        num3 = float(input('第三个数字: '))\n        \n        # 找出最大值和最小值\n        max_num = max(num1, num2, num3)\n        min_num = min(num1, num2, num3)\n        \n        print(f'\\n三个数字: {num1}, {num2}, {num3}')\n        print(f'最大值: {max_num}')\n        print(f'最小值: {min_num}')\n        \n        # 判断数字关系\n        if num1 == num2 == num3:\n            print('🟰 三个数字相等')\n        elif num1 == num2 or num2 == num3 or num1 == num3:\n            print('🟰 有两个数字相等')\n        else:\n            print('🔀 三个数字都不相等')\n        \n        # 排序判断\n        numbers = [num1, num2, num3]\n        sorted_asc = sorted(numbers)\n        sorted_desc = sorted(numbers, reverse=True)\n        \n        if numbers == sorted_asc:\n            print('📈 数字按升序排列')\n        elif numbers == sorted_desc:\n            print('📉 数字按降序排列')\n        else:\n            print('🔀 数字顺序是随机的')\n        \n        # 正负数判断\n        positive_count = sum(1 for num in numbers if num > 0)\n        negative_count = sum(1 for num in numbers if num < 0)\n        zero_count = sum(1 for num in numbers if num == 0)\n        \n        print(f'\\n数字特征：')\n        print(f'正数: {positive_count}个')\n        print(f'负数: {negative_count}个')\n        print(f'零: {zero_count}个')\n        \n    except ValueError:\n        print('请输入有效的数字！')\n\n# number_comparison()"
            }
        ]
    }

def get_extended_curriculum():
    """获取扩展的课程内容"""
    return {
        "4": get_day_4_content(),
        "5": get_day_5_content(),
        "6": get_day_6_content()
    }

if __name__ == "__main__":
    # 测试函数
    content = get_day_4_content()
    print(f"第4天课程: {content['topic']}")
    print(f"概念数量: {len(content['concepts'])}")
    print(f"示例数量: {len(content['examples'])}")
    print(f"练习数量: {len(content['exercises'])}") 