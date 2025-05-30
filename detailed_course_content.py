#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
详细的Python课程内容
包含具体的学习材料、代码示例和练习题
"""

def get_detailed_course_content():
    """获取详细的课程内容"""
    return {
        "1": {
            "topic": "Python简介与环境搭建",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "了解Python语言特点，掌握开发环境搭建",
            "concepts": [
                {
                    "name": "Python语言介绍",
                    "description": "Python是一种高级编程语言，以简洁易读著称",
                    "details": [
                        "Python是解释型语言，无需编译即可运行",
                        "具有丰富的标准库和第三方库",
                        "广泛应用于Web开发、数据分析、人工智能等领域"
                    ]
                },
                {
                    "name": "开发环境搭建",
                    "description": "安装Python解释器和代码编辑器",
                    "details": [
                        "下载并安装Python官方版本",
                        "配置环境变量PATH",
                        "选择合适的代码编辑器（VS Code、PyCharm等）"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "第一个Python程序",
                    "code": "# 这是我的第一个Python程序\nprint(\"Hello, Python!\")\nprint(\"欢迎进入Python的世界\")",
                    "explanation": "使用print()函数输出文本，这是最基本的Python语法"
                }
            ],
            "exercises": [
                {
                    "title": "环境测试",
                    "description": "验证Python环境是否正确安装",
                    "hint": "在命令行输入 python --version 检查版本",
                    "solution": "# 如果显示Python版本号，说明安装成功"
                }
            ],
            "extended_reading": {
                "title": "拓展阅读",
                "description": "深入了解Python语言和开发环境",
                "materials": [
                    {
                        "title": "Python官方教程 - 简介",
                        "url": "https://docs.python.org/zh-cn/3/tutorial/introduction.html",
                        "description": "Python官方文档的入门介绍，涵盖语言特性和基本概念",
                        "type": "official_doc"
                    },
                    {
                        "title": "Python官方教程 - 解释器",
                        "url": "https://docs.python.org/zh-cn/3/tutorial/interpreter.html",
                        "description": "详细介绍Python解释器的使用方法和交互模式",
                        "type": "official_doc"
                    },
                    {
                        "title": "Python安装指南",
                        "url": "https://docs.python.org/zh-cn/3/using/index.html",
                        "description": "各平台下Python的安装和配置详细指南",
                        "type": "official_doc"
                    },
                    {
                        "title": "Python之禅 (PEP 20)",
                        "url": "https://peps.python.org/pep-0020/",
                        "description": "Python设计哲学，理解Python的核心理念",
                        "type": "philosophy"
                    },
                    {
                        "title": "Python编码规范 (PEP 8)",
                        "url": "https://peps.python.org/pep-0008/",
                        "description": "Python代码风格指南，学习如何编写优雅的Python代码",
                        "type": "best_practice"
                    }
                ],
                "tips": [
                    "建议阅读Python之禅，理解Python的设计哲学",
                    "熟悉Python解释器的交互模式，有助于调试和学习",
                    "了解虚拟环境的概念，避免包依赖冲突"
                ]
            }
        },
        
        "2": {
            "topic": "变量与数据类型",
            "level": "初级", 
            "duration": "1-2小时",
            "objectives": "理解变量概念，掌握Python基本数据类型",
            "concepts": [
                {
                    "name": "变量的概念",
                    "description": "变量是存储数据的容器，可以随时改变其值",
                    "details": [
                        "变量名必须以字母或下划线开头",
                        "变量名区分大小写",
                        "Python是动态类型语言，无需声明变量类型"
                    ]
                },
                {
                    "name": "基本数据类型",
                    "description": "Python的基础数据类型",
                    "details": [
                        "整数（int）：如 42, -17",
                        "浮点数（float）：如 3.14, -2.5", 
                        "字符串（str）：如 'hello', \"world\"",
                        "布尔值（bool）：True 或 False"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "变量定义和使用",
                    "code": "# 整数变量\nage = 25\nprint(\"年龄:\", age)\n\n# 浮点数变量\nheight = 175.5\nprint(\"身高:\", height)\n\n# 字符串变量\nname = \"张三\"\nprint(\"姓名:\", name)\n\n# 布尔变量\nis_student = True\nprint(\"是学生:\", is_student)",
                    "explanation": "演示了四种基本数据类型的变量定义和输出"
                }
            ],
            "exercises": [
                {
                    "title": "个人信息变量",
                    "description": "创建变量存储你的个人信息：姓名、年龄、身高、是否在校学生",
                    "hint": "使用合适的数据类型",
                    "solution": "name = \"你的姓名\"\nage = 20\nheight = 170.0\nis_student = True"
                }
            ],
            "extended_reading": {
                "title": "拓展阅读",
                "description": "深入理解Python的变量和数据类型系统",
                "materials": [
                    {
                        "title": "Python官方教程 - 数据类型",
                        "url": "https://docs.python.org/zh-cn/3/tutorial/introduction.html#numbers",
                        "description": "官方文档关于数字、字符串等基本数据类型的详细说明",
                        "type": "official_doc"
                    },
                    {
                        "title": "内置类型参考",
                        "url": "https://docs.python.org/zh-cn/3/library/stdtypes.html",
                        "description": "Python所有内置数据类型的完整参考文档",
                        "type": "official_doc"
                    },
                    {
                        "title": "变量和简单数据类型",
                        "url": "https://docs.python.org/zh-cn/3/tutorial/introduction.html#using-python-as-a-calculator",
                        "description": "将Python用作计算器，了解数值运算和变量赋值",
                        "type": "official_doc"
                    },
                    {
                        "title": "动态类型系统",
                        "url": "https://docs.python.org/zh-cn/3/reference/datamodel.html#objects-values-and-types",
                        "description": "Python对象、值和类型的数据模型",
                        "type": "official_doc"
                    }
                ],
                "tips": [
                    "Python是动态类型语言，变量类型在运行时确定",
                    "使用type()函数可以查看变量的类型",
                    "Python中一切皆对象，包括数字和字符串",
                    "注意整数除法(//)和浮点除法(/)的区别"
                ]
            }
        },
        
        "3": {
            "topic": "运算符与表达式", 
            "level": "初级",
            "duration": "1-2小时", 
            "objectives": "掌握Python各种运算符的使用方法",
            "concepts": [
                {
                    "name": "算术运算符",
                    "description": "用于数学运算的操作符",
                    "details": [
                        "加法：+ （如 5 + 3 = 8）",
                        "减法：- （如 10 - 4 = 6）", 
                        "乘法：* （如 3 * 4 = 12）",
                        "除法：/ （如 15 / 3 = 5.0）",
                        "整除：// （如 17 // 5 = 3）",
                        "取余：% （如 17 % 5 = 2）",
                        "幂运算：** （如 2 ** 3 = 8）"
                    ]
                },
                {
                    "name": "比较运算符",
                    "description": "用于比较两个值的关系",
                    "details": [
                        "等于：== （如 5 == 5 返回 True）",
                        "不等于：!= （如 5 != 3 返回 True）",
                        "大于：> （如 8 > 5 返回 True）",
                        "小于：< （如 3 < 7 返回 True）",
                        "大于等于：>= （如 5 >= 5 返回 True）",
                        "小于等于：<= （如 4 <= 6 返回 True）"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "运算符示例",
                    "code": "# 算术运算\na = 10\nb = 3\nprint(f\"{a} + {b} = {a + b}\")\nprint(f\"{a} - {b} = {a - b}\")\nprint(f\"{a} * {b} = {a * b}\")\nprint(f\"{a} / {b} = {a / b}\")\nprint(f\"{a} // {b} = {a // b}\")\nprint(f\"{a} % {b} = {a % b}\")\nprint(f\"{a} ** {b} = {a ** b}\")\n\n# 比较运算\nprint(f\"{a} == {b}: {a == b}\")\nprint(f\"{a} > {b}: {a > b}\")",
                    "explanation": "展示了各种算术和比较运算符的使用"
                }
            ],
            "exercises": [
                {
                    "title": "简单计算器",
                    "description": "编写程序计算两个数的各种运算结果",
                    "hint": "使用所有学过的算术运算符",
                    "solution": "num1 = 20\nnum2 = 6\nprint(f\"加法: {num1 + num2}\")\nprint(f\"减法: {num1 - num2}\")\nprint(f\"乘法: {num1 * num2}\")\nprint(f\"除法: {num1 / num2}\")"
                }
            ],
            "extended_reading": {
                "title": "拓展阅读",
                "description": "深入了解Python的运算符和表达式系统",
                "materials": [
                    {
                        "title": "Python官方教程 - 运算符",
                        "url": "https://docs.python.org/zh-cn/3/tutorial/introduction.html#using-python-as-a-calculator",
                        "description": "官方文档中关于运算符和表达式的详细介绍",
                        "type": "official_doc"
                    },
                    {
                        "title": "表达式和运算符参考",
                        "url": "https://docs.python.org/zh-cn/3/reference/expressions.html",
                        "description": "Python语言参考中关于表达式和运算符的完整说明",
                        "type": "official_doc"
                    },
                    {
                        "title": "运算符优先级",
                        "url": "https://docs.python.org/zh-cn/3/reference/expressions.html#operator-precedence",
                        "description": "Python运算符的优先级和结合性规则",
                        "type": "official_doc"
                    },
                    {
                        "title": "数值类型运算",
                        "url": "https://docs.python.org/zh-cn/3/library/stdtypes.html#numeric-types-int-float-complex",
                        "description": "数值类型的运算方法和特殊方法",
                        "type": "official_doc"
                    }
                ],
                "tips": [
                    "注意浮点数运算可能存在精度问题",
                    "整除运算符//总是返回整数类型的结果",
                    "幂运算符**的优先级高于负号-",
                    "使用括号可以改变运算顺序",
                    "比较运算符可以链式使用，如：1 < x < 10"
                ]
            }
        },
        
        "4": {
            "topic": "字符串处理基础",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "掌握字符串的创建、操作和常用方法",
            "concepts": [
                {
                    "name": "字符串的创建",
                    "description": "在Python中创建和定义字符串",
                    "details": [
                        "使用单引号：'Hello World'",
                        "使用双引号：\"Hello World\"",
                        "使用三引号：'''多行字符串'''",
                        "字符串是不可变的数据类型"
                    ]
                },
                {
                    "name": "字符串操作",
                    "description": "字符串的基本操作方法",
                    "details": [
                        "字符串连接：使用 + 操作符",
                        "字符串重复：使用 * 操作符", 
                        "字符串索引：使用 [index] 访问字符",
                        "字符串切片：使用 [start:end] 获取子串"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "字符串基本操作",
                    "code": "# 字符串创建\nfirst_name = \"张\"\nlast_name = \"三\"\nfull_name = first_name + last_name\nprint(\"全名:\", full_name)\n\n# 字符串重复\nline = \"-\" * 20\nprint(line)\n\n# 字符串索引和切片\ntext = \"Python编程\"\nprint(\"第一个字符:\", text[0])\nprint(\"前3个字符:\", text[:3])\nprint(\"字符串长度:\", len(text))",
                    "explanation": "演示字符串的创建、连接、索引和切片操作"
                }
            ],
            "exercises": [
                {
                    "title": "姓名处理",
                    "description": "输入姓和名，输出完整姓名和姓名长度",
                    "hint": "使用字符串连接和len()函数",
                    "solution": "first = \"李\"\nlast = \"明\"\nfull = first + last\nprint(f\"姓名: {full}, 长度: {len(full)}\")"
                }
            ],
            "extended_reading": {
                "title": "拓展阅读",
                "description": "深入学习Python字符串处理技术",
                "materials": [
                    {
                        "title": "Python官方教程 - 字符串",
                        "url": "https://docs.python.org/zh-cn/3/tutorial/introduction.html#strings",
                        "description": "官方教程中关于字符串的基础知识和操作方法",
                        "type": "official_doc"
                    },
                    {
                        "title": "字符串方法参考",
                        "url": "https://docs.python.org/zh-cn/3/library/stdtypes.html#string-methods",
                        "description": "字符串对象的所有内置方法详细说明",
                        "type": "official_doc"
                    },
                    {
                        "title": "字符串格式化",
                        "url": "https://docs.python.org/zh-cn/3/tutorial/inputoutput.html#fancier-output-formatting",
                        "description": "高级字符串格式化技术和f字符串用法",
                        "type": "official_doc"
                    },
                    {
                        "title": "文本序列类型",
                        "url": "https://docs.python.org/zh-cn/3/library/stdtypes.html#text-sequence-type-str",
                        "description": "字符串作为文本序列类型的完整参考",
                        "type": "official_doc"
                    }
                ],
                "tips": [
                    "字符串是不可变对象，所有操作都返回新字符串",
                    "Python字符串默认使用UTF-8编码，支持多语言",
                    "使用原始字符串r''来避免转义字符的困扰",
                    "字符串切片支持负索引，-1表示最后一个字符",
                    "三引号字符串可以跨越多行，保留换行符"
                ]
            }
        },
        
        "5": {
            "topic": "用户输入与输出", 
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "掌握input()函数获取用户输入，学会格式化输出",
            "concepts": [
                {
                    "name": "input()函数",
                    "description": "获取用户从键盘输入的数据",
                    "details": [
                        "input()函数总是返回字符串类型",
                        "可以在input()中添加提示信息",
                        "需要类型转换来获取数字类型",
                        "input()会暂停程序等待用户输入"
                    ]
                },
                {
                    "name": "类型转换",
                    "description": "将输入的字符串转换为其他数据类型",
                    "details": [
                        "int()：转换为整数",
                        "float()：转换为浮点数", 
                        "str()：转换为字符串",
                        "bool()：转换为布尔值"
                    ]
                },
                {
                    "name": "格式化输出",
                    "description": "美化输出的显示效果",
                    "details": [
                        "使用f字符串：f\"姓名：{name}\"",
                        "使用format方法：\"姓名：{}\".format(name)",
                        "使用%格式化：\"姓名：%s\" % name",
                        "控制小数位数：f\"{num:.2f}\""
                    ]
                }
            ],
            "examples": [
                {
                    "title": "用户输入与输出示例",
                    "code": "# 获取用户基本信息\nname = input(\"请输入你的姓名: \")\nage = int(input(\"请输入你的年龄: \"))\nheight = float(input(\"请输入你的身高(cm): \"))\n\n# 格式化输出\nprint(f\"你好，{name}！\")\nprint(f\"你今年{age}岁\")\nprint(f\"身高{height:.1f}厘米\")\n\n# 计算并输出\nnext_year_age = age + 1\nprint(f\"明年你将{next_year_age}岁\")\n\n# 多种输出格式\nprint(\"姓名：{}，年龄：{}岁\".format(name, age))\nprint(\"姓名：%s，身高：%.1f厘米\" % (name, height))",
                    "explanation": "展示了如何获取用户输入、进行类型转换和格式化输出"
                }
            ],
            "exercises": [
                {
                    "title": "简单计算器",
                    "description": "编写程序让用户输入两个数字，计算并输出它们的和、差、积、商",
                    "hint": "记住input()返回的是字符串，需要转换为数字类型",
                    "solution": "# 获取用户输入\nnum1 = float(input(\"请输入第一个数字: \"))\nnum2 = float(input(\"请输入第二个数字: \"))\n\n# 计算结果\nsum_result = num1 + num2\ndiff_result = num1 - num2\nproduct_result = num1 * num2\nquotient_result = num1 / num2 if num2 != 0 else \"无法除以0\"\n\n# 输出结果\nprint(f\"{num1} + {num2} = {sum_result}\")\nprint(f\"{num1} - {num2} = {diff_result}\")\nprint(f\"{num1} × {num2} = {product_result}\")\nprint(f\"{num1} ÷ {num2} = {quotient_result}\")"
                },
                {
                    "title": "个人信息收集",
                    "description": "编写程序收集用户的姓名、年龄、爱好，并美观地显示出来",
                    "hint": "使用多个input()函数和f字符串格式化",
                    "solution": "name = input(\"姓名: \")\nage = int(input(\"年龄: \"))\nhobby = input(\"爱好: \")\n\nprint(\"\\n=== 个人信息卡 ===\")\nprint(f\"姓名: {name}\")\nprint(f\"年龄: {age}岁\")\nprint(f\"爱好: {hobby}\")\nprint(\"=================\")"
                }
            ],
            "extended_reading": {
                "title": "拓展阅读",
                "description": "深入学习Python的输入输出和类型转换",
                "materials": [
                    {
                        "title": "Python官方教程 - 输入输出",
                        "url": "https://docs.python.org/zh-cn/3/tutorial/inputoutput.html",
                        "description": "官方教程中关于输入输出的详细介绍",
                        "type": "official_doc"
                    },
                    {
                        "title": "内置函数 - input()",
                        "url": "https://docs.python.org/zh-cn/3/library/functions.html#input",
                        "description": "input()函数的官方文档",
                        "type": "official_doc"
                    },
                    {
                        "title": "字符串格式化规范",
                        "url": "https://docs.python.org/zh-cn/3/library/string.html#format-specification-mini-language",
                        "description": "字符串格式化的详细规范和语法",
                        "type": "official_doc"
                    },
                    {
                        "title": "内置函数参考",
                        "url": "https://docs.python.org/zh-cn/3/library/functions.html",
                        "description": "所有内置函数的完整参考，包括类型转换函数",
                        "type": "official_doc"
                    }
                ],
                "tips": [
                    "input()总是返回字符串，需要手动转换类型",
                    "使用try-except处理类型转换可能的错误",
                    "f字符串是Python 3.6+推荐的格式化方式",
                    "print()函数支持多个参数和分隔符设置"
                ]
            }
        },
        
        "6": {
            "topic": "条件语句",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "掌握if、elif、else条件语句的使用",
            "concepts": [
                {
                    "name": "if语句",
                    "description": "根据条件执行不同的代码块",
                    "details": [
                        "if语句的基本语法：if 条件:",
                        "缩进表示代码块的范围",
                        "条件可以是任何返回布尔值的表达式",
                        "可以使用逻辑运算符：and、or、not"
                    ]
                },
                {
                    "name": "elif和else",
                    "description": "处理多个条件分支",
                    "details": [
                        "elif用于检查多个条件",
                        "else处理所有条件都不满足的情况",
                        "条件按顺序检查，第一个为真的执行",
                        "只能有一个else，但可以有多个elif"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "条件语句示例",
                    "code": "# 成绩等级判断\nscore = int(input(\"请输入成绩: \"))\n\nif score >= 90:\n    grade = \"A\"\n    print(\"优秀！\")\nelif score >= 80:\n    grade = \"B\"\n    print(\"良好！\")\nelif score >= 70:\n    grade = \"C\"\n    print(\"中等！\")\nelif score >= 60:\n    grade = \"D\"\n    print(\"及格！\")\nelse:\n    grade = \"F\"\n    print(\"不及格！\")\n\nprint(f\"你的成绩是{score}分，等级为{grade}\")",
                    "explanation": "演示了多条件判断的完整流程"
                }
            ],
            "exercises": [
                {
                    "title": "年龄分组",
                    "description": "根据用户输入的年龄，判断属于哪个年龄组",
                    "hint": "使用if-elif-else结构",
                    "solution": "age = int(input(\"请输入年龄: \"))\n\nif age < 13:\n    print(\"儿童\")\nelif age < 20:\n    print(\"青少年\")\nelif age < 60:\n    print(\"成年人\")\nelse:\n    print(\"老年人\")"
                }
            ]
        },
        
        "7": {
            "topic": "第一周复习与项目",
            "level": "初级",
            "duration": "2-3小时",
            "objectives": "巩固第一周知识，完成综合项目",
            "concepts": [
                {
                    "name": "知识回顾",
                    "description": "复习第一周学过的所有内容",
                    "details": [
                        "Python基础语法和环境",
                        "变量、数据类型和运算符",
                        "字符串处理和格式化",
                        "用户输入输出和条件语句"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "个人资料管理器",
                    "code": "# 个人资料管理器\nprint(\"=== 个人资料管理器 ===\")\n\n# 收集信息\nname = input(\"姓名: \")\nage = int(input(\"年龄: \"))\nheight = float(input(\"身高(cm): \"))\nweight = float(input(\"体重(kg): \"))\n\n# 计算BMI\nbmi = weight / ((height / 100) ** 2)\n\n# 判断BMI分类\nif bmi < 18.5:\n    bmi_category = \"偏瘦\"\nelif bmi < 24:\n    bmi_category = \"正常\"\nelif bmi < 28:\n    bmi_category = \"偏胖\"\nelse:\n    bmi_category = \"肥胖\"\n\n# 输出结果\nprint(\"\\n=== 个人资料 ===\")\nprint(f\"姓名: {name}\")\nprint(f\"年龄: {age}岁\")\nprint(f\"身高: {height}cm\")\nprint(f\"体重: {weight}kg\")\nprint(f\"BMI: {bmi:.2f} ({bmi_category})\")",
                    "explanation": "综合运用了输入输出、计算、条件判断等知识"
                }
            ],
            "exercises": [
                {
                    "title": "猜数字游戏",
                    "description": "创建一个简单的猜数字游戏",
                    "hint": "使用条件语句判断大小",
                    "solution": "import random\n\nnumber = random.randint(1, 100)\nguess = int(input(\"猜一个1-100的数字: \"))\n\nif guess == number:\n    print(\"恭喜！猜对了！\")\nelif guess < number:\n    print(\"太小了！\")\nelse:\n    print(\"太大了！\")"
                }
            ]
        },
        
        "8": {
            "topic": "列表基础",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "掌握列表的创建、访问和基本操作",
            "concepts": [
                {
                    "name": "列表的创建",
                    "description": "Python中最常用的数据结构之一",
                    "details": [
                        "使用方括号[]创建列表",
                        "列表可以包含不同类型的数据",
                        "列表是可变的（mutable）",
                        "列表元素按顺序排列，有索引"
                    ]
                },
                {
                    "name": "列表操作",
                    "description": "访问、修改和操作列表元素",
                    "details": [
                        "索引访问：list[0]获取第一个元素",
                        "负索引：list[-1]获取最后一个元素",
                        "切片操作：list[1:3]获取子列表",
                        "len()函数获取列表长度"
                    ]
                },
                {
                    "name": "列表方法",
                    "description": "常用的列表内置方法",
                    "details": [
                        "append()：在末尾添加元素",
                        "insert()：在指定位置插入元素",
                        "remove()：删除指定值的元素",
                        "pop()：删除并返回指定位置的元素"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "列表基本操作",
                    "code": "# 创建列表\nfruits = [\"苹果\", \"香蕉\", \"橙子\", \"葡萄\"]\nnumbers = [1, 2, 3, 4, 5]\nmixed = [\"张三\", 25, 175.5, True]\n\n# 访问元素\nprint(\"第一个水果:\", fruits[0])\nprint(\"最后一个数字:\", numbers[-1])\nprint(\"前三个水果:\", fruits[:3])\n\n# 修改元素\nfruits[1] = \"草莓\"\nprint(\"修改后的水果:\", fruits)\n\n# 添加元素\nfruits.append(\"芒果\")\nprint(\"添加后的水果:\", fruits)\n\n# 删除元素\nfruits.remove(\"橙子\")\nprint(\"删除后的水果:\", fruits)\n\n# 列表长度\nprint(\"水果数量:\", len(fruits))",
                    "explanation": "展示了列表的创建、访问、修改和基本方法的使用"
                }
            ],
            "exercises": [
                {
                    "title": "学生成绩管理",
                    "description": "创建一个学生成绩列表，实现查看、添加、删除成绩功能",
                    "hint": "使用列表存储成绩，用方法进行操作",
                    "solution": "# 学生成绩管理\nscores = [85, 92, 78, 96, 88]\n\nprint(\"当前成绩:\", scores)\nprint(\"平均分:\", sum(scores) / len(scores))\nprint(\"最高分:\", max(scores))\nprint(\"最低分:\", min(scores))\n\n# 添加新成绩\nnew_score = int(input(\"输入新成绩: \"))\nscores.append(new_score)\nprint(\"添加后的成绩:\", scores)"
                }
            ]
        },
        
        "9": {
            "topic": "for循环",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "掌握for循环的使用，学会遍历序列",
            "concepts": [
                {
                    "name": "for循环基础",
                    "description": "用于遍历序列（如列表、字符串）的循环结构",
                    "details": [
                        "基本语法：for 变量 in 序列:",
                        "循环变量会依次取序列中的每个值",
                        "循环体需要缩进",
                        "可以遍历列表、字符串、元组等"
                    ]
                },
                {
                    "name": "range()函数",
                    "description": "生成数字序列的函数",
                    "details": [
                        "range(n)：生成0到n-1的数字",
                        "range(start, stop)：生成start到stop-1的数字",
                        "range(start, stop, step)：指定步长",
                        "常与for循环配合使用"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "for循环示例",
                    "code": "# 遍历列表\nfruits = [\"苹果\", \"香蕉\", \"橙子\"]\nfor fruit in fruits:\n    print(f\"我喜欢吃{fruit}\")\n\n# 遍历字符串\nword = \"Python\"\nfor char in word:\n    print(f\"字母: {char}\")\n\n# 使用range()\nprint(\"\\n数字1到5:\")\nfor i in range(1, 6):\n    print(f\"数字: {i}\")\n\n# 计算1到10的和\ntotal = 0\nfor i in range(1, 11):\n    total += i\nprint(f\"\\n1到10的和: {total}\")\n\n# 遍历列表和索引\nscores = [85, 92, 78, 96]\nfor i, score in enumerate(scores):\n    print(f\"第{i+1}个成绩: {score}分\")",
                    "explanation": "演示了for循环的各种用法：遍历列表、字符串、使用range()和enumerate()"
                }
            ],
            "exercises": [
                {
                    "title": "九九乘法表",
                    "description": "使用for循环打印九九乘法表",
                    "hint": "使用嵌套的for循环",
                    "solution": "# 九九乘法表\nfor i in range(1, 10):\n    for j in range(1, i + 1):\n        print(f\"{j}×{i}={i*j}\", end=\"\\t\")\n    print()  # 换行"
                }
            ]
        },
        
        "10": {
            "topic": "while循环",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "掌握while循环的使用，理解循环控制",
            "concepts": [
                {
                    "name": "while循环基础",
                    "description": "基于条件的循环结构",
                    "details": [
                        "基本语法：while 条件:",
                        "只要条件为真就继续执行",
                        "需要在循环体内改变条件，避免无限循环",
                        "适用于不知道循环次数的情况"
                    ]
                },
                {
                    "name": "循环控制",
                    "description": "控制循环执行的语句",
                    "details": [
                        "break：立即退出循环",
                        "continue：跳过本次循环，继续下一次",
                        "else子句：循环正常结束时执行",
                        "避免无限循环的注意事项"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "while循环示例",
                    "code": "# 基本while循环\ncount = 1\nwhile count <= 5:\n    print(f\"计数: {count}\")\n    count += 1\n\n# 用户输入验证\nwhile True:\n    password = input(\"请输入密码: \")\n    if password == \"123456\":\n        print(\"密码正确！\")\n        break\n    else:\n        print(\"密码错误，请重试\")\n\n# 猜数字游戏\nimport random\nsecret = random.randint(1, 100)\nguess_count = 0\n\nwhile True:\n    guess = int(input(\"猜一个1-100的数字: \"))\n    guess_count += 1\n    \n    if guess == secret:\n        print(f\"恭喜！你用了{guess_count}次猜对了！\")\n        break\n    elif guess < secret:\n        print(\"太小了！\")\n    else:\n        print(\"太大了！\")",
                    "explanation": "展示了while循环的基本用法、用户输入验证和游戏逻辑"
                }
            ],
            "exercises": [
                {
                    "title": "计算阶乘",
                    "description": "使用while循环计算一个数的阶乘",
                    "hint": "n! = n × (n-1) × (n-2) × ... × 1",
                    "solution": "n = int(input(\"请输入一个正整数: \"))\nfactorial = 1\ni = 1\n\nwhile i <= n:\n    factorial *= i\n    i += 1\n\nprint(f\"{n}的阶乘是: {factorial}\")"
                }
            ]
        },
        
        "11": {
            "topic": "循环控制语句",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "掌握break、continue等循环控制语句",
            "concepts": [
                {
                    "name": "break语句",
                    "description": "立即退出循环",
                    "details": [
                        "break会终止最近的for或while循环",
                        "常用于满足特定条件时退出循环",
                        "在嵌套循环中只退出当前层循环",
                        "break后的代码不会执行"
                    ]
                },
                {
                    "name": "continue语句",
                    "description": "跳过当前循环的剩余代码",
                    "details": [
                        "continue跳过本次循环的剩余语句",
                        "直接进入下一次循环的判断",
                        "常用于跳过特定条件的处理",
                        "只影响当前循环层"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "循环控制示例",
                    "code": "# break示例：找到第一个偶数就退出\nnumbers = [1, 3, 5, 8, 9, 12]\nfor num in numbers:\n    if num % 2 == 0:\n        print(f\"找到第一个偶数: {num}\")\n        break\n    print(f\"奇数: {num}\")\n\n# continue示例：只打印偶数\nprint(\"\\n所有偶数:\")\nfor i in range(1, 11):\n    if i % 2 != 0:\n        continue\n    print(f\"偶数: {i}\")\n\n# 综合示例：密码验证\nmax_attempts = 3\nattempts = 0\n\nwhile attempts < max_attempts:\n    password = input(\"请输入密码: \")\n    attempts += 1\n    \n    if password == \"python123\":\n        print(\"登录成功！\")\n        break\n    elif attempts < max_attempts:\n        print(f\"密码错误，还有{max_attempts - attempts}次机会\")\n        continue\n    else:\n        print(\"登录失败，账号被锁定\")",
                    "explanation": "演示了break和continue在不同场景下的使用"
                }
            ],
            "exercises": [
                {
                    "title": "素数判断",
                    "description": "判断一个数是否为素数，使用break优化",
                    "hint": "如果找到因数就可以提前退出",
                    "solution": "num = int(input(\"请输入一个数: \"))\nis_prime = True\n\nif num < 2:\n    is_prime = False\nelse:\n    for i in range(2, int(num ** 0.5) + 1):\n        if num % i == 0:\n            is_prime = False\n            break\n\nif is_prime:\n    print(f\"{num} 是素数\")\nelse:\n    print(f\"{num} 不是素数\")"
                }
            ]
        },
        
        "12": {
            "topic": "嵌套循环",
            "level": "初级", 
            "duration": "1-2小时",
            "objectives": "掌握嵌套循环的使用和应用场景",
            "concepts": [
                {
                    "name": "嵌套循环概念",
                    "description": "循环内部包含另一个循环",
                    "details": [
                        "外层循环每执行一次，内层循环完整执行一轮",
                        "常用于处理二维数据结构",
                        "时间复杂度是各层循环的乘积",
                        "需要注意性能问题"
                    ]
                },
                {
                    "name": "应用场景",
                    "description": "嵌套循环的常见用途",
                    "details": [
                        "打印图案和表格",
                        "遍历二维列表",
                        "组合和排列问题",
                        "矩阵运算"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "嵌套循环示例",
                    "code": "# 打印星形图案\nrows = 5\nfor i in range(1, rows + 1):\n    for j in range(i):\n        print(\"*\", end=\"\")\n    print()  # 换行\n\n# 乘法表\nprint(\"\\n乘法表:\")\nfor i in range(1, 4):\n    for j in range(1, 4):\n        result = i * j\n        print(f\"{i}×{j}={result}\", end=\"\\t\")\n    print()\n\n# 遍历二维列表\nmatrix = [\n    [1, 2, 3],\n    [4, 5, 6],\n    [7, 8, 9]\n]\n\nprint(\"\\n矩阵元素:\")\nfor row in matrix:\n    for element in row:\n        print(element, end=\" \")\n    print()\n\n# 查找最大值\nmax_value = matrix[0][0]\nfor i in range(len(matrix)):\n    for j in range(len(matrix[i])):\n        if matrix[i][j] > max_value:\n            max_value = matrix[i][j]\n\nprint(f\"\\n矩阵中的最大值: {max_value}\")",
                    "explanation": "展示了嵌套循环在图案打印、表格和二维数据处理中的应用"
                }
            ],
            "exercises": [
                {
                    "title": "数字金字塔",
                    "description": "打印数字金字塔图案",
                    "hint": "外层控制行数，内层打印数字",
                    "solution": "rows = 5\nfor i in range(1, rows + 1):\n    # 打印空格\n    for j in range(rows - i):\n        print(\" \", end=\"\")\n    # 打印数字\n    for k in range(1, i + 1):\n        print(k, end=\"\")\n    print()"
                }
            ]
        },
        
        "13": {
            "topic": "列表推导式",
            "level": "初级",
            "duration": "1-2小时", 
            "objectives": "掌握列表推导式的语法和应用",
            "concepts": [
                {
                    "name": "列表推导式语法",
                    "description": "用简洁的方式创建列表",
                    "details": [
                        "基本语法：[表达式 for 变量 in 序列]",
                        "条件筛选：[表达式 for 变量 in 序列 if 条件]",
                        "比传统循环更简洁高效",
                        "返回一个新的列表"
                    ]
                },
                {
                    "name": "高级用法",
                    "description": "嵌套和条件表达式",
                    "details": [
                        "嵌套推导式处理二维数据",
                        "条件表达式：[表达式1 if 条件 else 表达式2 for 变量 in 序列]",
                        "多重循环：[表达式 for 变量1 in 序列1 for 变量2 in 序列2]",
                        "注意可读性和性能"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "列表推导式示例",
                    "code": "# 基本列表推导式\nnumbers = [1, 2, 3, 4, 5]\nsquares = [x**2 for x in numbers]\nprint(\"平方数:\", squares)\n\n# 条件筛选\nevens = [x for x in range(1, 11) if x % 2 == 0]\nprint(\"偶数:\", evens)\n\n# 字符串处理\nwords = ['hello', 'world', 'python']\nuppercase = [word.upper() for word in words]\nprint(\"大写:\", uppercase)\n\n# 条件表达式\nresult = ['偶数' if x % 2 == 0 else '奇数' for x in range(1, 6)]\nprint(\"奇偶判断:\", result)\n\n# 嵌套列表推导式\nmatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\nflattened = [num for row in matrix for num in row]\nprint(\"扁平化:\", flattened)\n\n# 实用示例：过滤和转换\nscores = [85, 92, 78, 96, 88, 75]\npassed = [score for score in scores if score >= 80]\nprint(\"及格分数:\", passed)\n\n# 多条件\nhigh_scores = [f\"{score}分(优秀)\" if score >= 90 else f\"{score}分(良好)\" \n               for score in scores if score >= 80]\nprint(\"高分评价:\", high_scores)",
                    "explanation": "展示了列表推导式的各种用法，从基础到高级应用"
                }
            ],
            "exercises": [
                {
                    "title": "温度转换",
                    "description": "将摄氏度列表转换为华氏度",
                    "hint": "华氏度 = 摄氏度 * 9/5 + 32",
                    "solution": "celsius = [0, 10, 20, 30, 40]\nfahrenheit = [c * 9/5 + 32 for c in celsius]\nprint(\"华氏度:\", fahrenheit)"
                }
            ]
        },
        
        "14": {
            "topic": "第二周复习与项目",
            "level": "初级",
            "duration": "2-3小时",
            "objectives": "巩固循环和列表知识，完成综合项目",
            "concepts": [
                {
                    "name": "知识总结",
                    "description": "回顾第二周学习内容",
                    "details": [
                        "列表的创建和操作",
                        "for循环和while循环",
                        "循环控制语句",
                        "嵌套循环和列表推导式"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "学生成绩分析系统",
                    "code": "# 学生成绩分析系统\nprint(\"=== 学生成绩分析系统 ===\")\n\n# 输入成绩\nscores = []\nwhile True:\n    score_input = input(\"请输入成绩(输入q退出): \")\n    if score_input.lower() == 'q':\n        break\n    try:\n        score = float(score_input)\n        if 0 <= score <= 100:\n            scores.append(score)\n        else:\n            print(\"成绩应在0-100之间\")\n    except ValueError:\n        print(\"请输入有效数字\")\n\nif scores:\n    # 统计分析\n    total = sum(scores)\n    average = total / len(scores)\n    highest = max(scores)\n    lowest = min(scores)\n    \n    # 等级分布\n    excellent = [s for s in scores if s >= 90]\n    good = [s for s in scores if 80 <= s < 90]\n    fair = [s for s in scores if 70 <= s < 80]\n    poor = [s for s in scores if s < 70]\n    \n    # 输出报告\n    print(\"\\n=== 成绩分析报告 ===\")\n    print(f\"总人数: {len(scores)}\")\n    print(f\"平均分: {average:.2f}\")\n    print(f\"最高分: {highest}\")\n    print(f\"最低分: {lowest}\")\n    print(f\"优秀(>=90): {len(excellent)}人\")\n    print(f\"良好(80-89): {len(good)}人\")\n    print(f\"中等(70-79): {len(fair)}人\")\n    print(f\"不及格(<70): {len(poor)}人\")\nelse:\n    print(\"没有输入任何成绩\")",
                    "explanation": "综合运用了列表、循环、条件语句和列表推导式"
                }
            ],
            "exercises": [
                {
                    "title": "购物清单管理",
                    "description": "创建一个购物清单管理程序",
                    "hint": "使用列表存储商品，循环实现菜单",
                    "solution": "shopping_list = []\n\nwhile True:\n    print(\"\\n购物清单管理\")\n    print(\"1. 添加商品\")\n    print(\"2. 删除商品\")\n    print(\"3. 查看清单\")\n    print(\"4. 退出\")\n    \n    choice = input(\"请选择操作: \")\n    \n    if choice == '1':\n        item = input(\"请输入商品名称: \")\n        shopping_list.append(item)\n        print(f\"已添加: {item}\")\n    elif choice == '2':\n        if shopping_list:\n            print(\"当前商品:\", shopping_list)\n            item = input(\"请输入要删除的商品: \")\n            if item in shopping_list:\n                shopping_list.remove(item)\n                print(f\"已删除: {item}\")\n            else:\n                print(\"商品不存在\")\n        else:\n            print(\"清单为空\")\n    elif choice == '3':\n        if shopping_list:\n            print(\"购物清单:\")\n            for i, item in enumerate(shopping_list, 1):\n                print(f\"{i}. {item}\")\n        else:\n            print(\"清单为空\")\n    elif choice == '4':\n        print(\"再见！\")\n        break\n    else:\n        print(\"无效选择\")"
                }
            ]
        },
        
        "15": {
            "topic": "元组与集合",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "掌握元组和集合的特点与使用方法",
            "concepts": [
                {
                    "name": "元组(Tuple)",
                    "description": "有序且不可变的数据集合",
                    "details": [
                        "使用圆括号()创建：(1, 2, 3)",
                        "元组是不可变的(immutable)",
                        "支持索引和切片操作",
                        "可以包含不同类型的数据"
                    ]
                },
                {
                    "name": "集合(Set)",
                    "description": "无序且元素唯一的数据集合",
                    "details": [
                        "使用花括号{}创建：{1, 2, 3}",
                        "自动去除重复元素",
                        "不支持索引，但支持成员测试",
                        "支持数学集合运算"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "元组和集合示例",
                    "code": "# 元组示例\npoint = (3, 4)\nprint(f\"坐标点: {point}\")\nprint(f\"x坐标: {point[0]}, y坐标: {point[1]}\")\n\n# 元组拆包\nx, y = point\nprint(f\"拆包后: x={x}, y={y}\")\n\n# 多个返回值\ndef get_name_age():\n    return \"张三\", 25\n\nname, age = get_name_age()\nprint(f\"姓名: {name}, 年龄: {age}\")\n\n# 集合示例\nnumbers = {1, 2, 3, 4, 5}\nprint(f\"数字集合: {numbers}\")\n\n# 去除重复\nduplicates = [1, 2, 2, 3, 3, 4]\nunique = set(duplicates)\nprint(f\"去重后: {unique}\")\n\n# 集合运算\nset1 = {1, 2, 3, 4}\nset2 = {3, 4, 5, 6}\n\nprint(f\"并集: {set1 | set2}\")\nprint(f\"交集: {set1 & set2}\")\nprint(f\"差集: {set1 - set2}\")\nprint(f\"对称差集: {set1 ^ set2}\")\n\n# 成员测试\nif 3 in set1:\n    print(\"3在set1中\")\n\n# 集合方法\nfruits = {'苹果', '香蕉'}\nfruits.add('橙子')\nprint(f\"添加后: {fruits}\")\nfruits.remove('香蕉')\nprint(f\"删除后: {fruits}\")",
                    "explanation": "展示了元组的不可变性和拆包，以及集合的去重和运算功能"
                }
            ],
            "exercises": [
                {
                    "title": "统计重复单词",
                    "description": "统计文本中不重复的单词数量",
                    "hint": "使用集合的去重特性",
                    "solution": "text = \"hello world hello python world\"\nwords = text.split()\nunique_words = set(words)\nprint(f\"总单词数: {len(words)}\")\nprint(f\"不重复单词数: {len(unique_words)}\")\nprint(f\"不重复单词: {unique_words}\")"
                }
            ]
        },
        
        "16": {
            "topic": "字典基础",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "掌握字典的创建、访问和基本操作",
            "concepts": [
                {
                    "name": "字典概念",
                    "description": "键值对(key-value)的数据结构",
                    "details": [
                        "使用花括号{}创建：{'key': 'value'}",
                        "键必须是不可变类型(字符串、数字、元组)",
                        "值可以是任意类型",
                        "字典是可变的且无序的(Python 3.7+保持插入顺序)"
                    ]
                },
                {
                    "name": "字典操作",
                    "description": "访问、修改和操作字典",
                    "details": [
                        "使用键访问值：dict[key]",
                        "添加/修改：dict[key] = value",
                        "删除：del dict[key] 或 dict.pop(key)",
                        "检查键是否存在：key in dict"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "字典基础操作",
                    "code": "# 创建字典\nstudent = {\n    'name': '张三',\n    'age': 20,\n    'grade': 85,\n    'courses': ['数学', '英语', '计算机']\n}\n\nprint(f\"学生信息: {student}\")\nprint(f\"姓名: {student['name']}\")\nprint(f\"年龄: {student['age']}\")\n\n# 修改和添加\nstudent['age'] = 21\nstudent['phone'] = '12345678901'\nprint(f\"更新后: {student}\")\n\n# 安全访问\nphone = student.get('phone', '未设置')\nprint(f\"电话: {phone}\")\n\n# 遍历字典\nprint(\"\\n所有信息:\")\nfor key, value in student.items():\n    print(f\"{key}: {value}\")\n\n# 只遍历键或值\nprint(\"\\n所有键:\", list(student.keys()))\nprint(\"所有值:\", list(student.values()))\n\n# 字典合并\ncontact = {'email': 'zhangsan@email.com', 'address': '北京'}\nstudent.update(contact)\nprint(f\"\\n合并后: {student}\")\n\n# 删除元素\nif 'phone' in student:\n    del student['phone']\n    print(\"已删除电话信息\")\n\nprint(f\"最终信息: {student}\")",
                    "explanation": "演示了字典的创建、访问、修改、遍历和删除操作"
                }
            ],
            "exercises": [
                {
                    "title": "单词计数器",
                    "description": "统计文本中每个单词出现的次数",
                    "hint": "使用字典，键为单词，值为计数",
                    "solution": "text = \"python is great python is easy python is powerful\"\nwords = text.split()\nword_count = {}\n\nfor word in words:\n    if word in word_count:\n        word_count[word] += 1\n    else:\n        word_count[word] = 1\n\nprint(\"单词计数:\")\nfor word, count in word_count.items():\n    print(f\"{word}: {count}\")"
                }
            ]
        },
        
        "17": {
            "topic": "字典操作与方法",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "掌握字典的高级操作和常用方法",
            "concepts": [
                {
                    "name": "字典方法",
                    "description": "字典的内置方法",
                    "details": [
                        "get(key, default): 安全获取值",
                        "pop(key): 删除并返回值",
                        "update(dict): 更新字典",
                        "clear(): 清空字典"
                    ]
                },
                {
                    "name": "字典推导式",
                    "description": "用推导式创建字典",
                    "details": [
                        "语法：{key_expr: value_expr for item in iterable}",
                        "条件筛选：{k: v for k, v in dict.items() if condition}",
                        "键值转换和过滤",
                        "提高代码简洁性"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "字典高级操作",
                    "code": "# 字典方法示例\nscores = {'数学': 95, '英语': 87, '物理': 92, '化学': 89}\n\n# get方法\nmath_score = scores.get('数学', 0)\nhistory_score = scores.get('历史', 0)  # 不存在的键\nprint(f\"数学: {math_score}, 历史: {history_score}\")\n\n# setdefault方法\nscores.setdefault('历史', 85)\nprint(f\"添加历史成绩后: {scores}\")\n\n# pop方法\nremoved_score = scores.pop('化学')\nprint(f\"删除的化学成绩: {removed_score}\")\nprint(f\"删除后: {scores}\")\n\n# 字典推导式\noriginal = {'a': 1, 'b': 2, 'c': 3, 'd': 4}\n\n# 值翻倍\ndoubled = {k: v * 2 for k, v in original.items()}\nprint(f\"值翻倍: {doubled}\")\n\n# 过滤\nfiltered = {k: v for k, v in original.items() if v % 2 == 0}\nprint(f\"偶数值: {filtered}\")\n\n# 键值互换\nswapped = {v: k for k, v in original.items()}\nprint(f\"键值互换: {swapped}\")\n\n# 嵌套字典\nstudents = {\n    '张三': {'数学': 95, '英语': 87},\n    '李四': {'数学': 88, '英语': 92},\n    '王五': {'数学': 91, '英语': 89}\n}\n\n# 计算平均分\nfor name, subjects in students.items():\n    avg = sum(subjects.values()) / len(subjects)\n    print(f\"{name}的平均分: {avg:.1f}\")\n\n# 统计各科总分\nsubject_totals = {}\nfor student_scores in students.values():\n    for subject, score in student_scores.items():\n        subject_totals[subject] = subject_totals.get(subject, 0) + score\n\nprint(f\"\\n各科总分: {subject_totals}\")",
                    "explanation": "展示了字典的高级方法、推导式和嵌套字典的应用"
                }
            ],
            "exercises": [
                {
                    "title": "学生信息管理",
                    "description": "创建学生信息管理系统",
                    "hint": "使用嵌套字典存储学生的多项信息",
                    "solution": "students = {}\n\ndef add_student(name, age, grade):\n    students[name] = {'age': age, 'grade': grade, 'subjects': {}}\n\ndef add_score(name, subject, score):\n    if name in students:\n        students[name]['subjects'][subject] = score\n    else:\n        print(f\"学生{name}不存在\")\n\n# 添加学生\nadd_student('张三', 20, '大二')\nadd_student('李四', 19, '大一')\n\n# 添加成绩\nadd_score('张三', '数学', 95)\nadd_score('张三', '英语', 87)\nadd_score('李四', '数学', 88)\n\n# 显示信息\nfor name, info in students.items():\n    print(f\"{name}: {info}\")"
                }
            ]
        },
        
        "18": {
            "topic": "数据结构综合应用",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "综合运用列表、元组、字典、集合解决实际问题",
            "concepts": [
                {
                    "name": "数据结构选择",
                    "description": "根据需求选择合适的数据结构",
                    "details": [
                        "列表：有序、可变、允许重复",
                        "元组：有序、不可变、允许重复",
                        "字典：键值对、可变、键唯一",
                        "集合：无序、可变、元素唯一"
                    ]
                },
                {
                    "name": "组合使用",
                    "description": "多种数据结构的组合应用",
                    "details": [
                        "列表包含字典：存储多个对象",
                        "字典包含列表：一对多关系",
                        "集合操作：去重、交并差",
                        "元组作为字典键：坐标、复合键"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "图书管理系统",
                    "code": "# 图书管理系统\nlibrary = {\n    'books': [\n        {'id': 1, 'title': 'Python编程', 'author': '张三', 'category': '计算机', 'available': True},\n        {'id': 2, 'title': '数据结构', 'author': '李四', 'category': '计算机', 'available': False},\n        {'id': 3, 'title': '文学作品', 'author': '王五', 'category': '文学', 'available': True}\n    ],\n    'members': {\n        'user1': {'name': '小明', 'borrowed': [2]},\n        'user2': {'name': '小红', 'borrowed': []}\n    },\n    'categories': {'计算机', '文学', '科学', '历史'}\n}\n\n# 查找可借阅的书籍\navailable_books = [book for book in library['books'] if book['available']]\nprint(\"可借阅书籍:\")\nfor book in available_books:\n    print(f\"- {book['title']} ({book['author']})\")\n\n# 按分类统计\ncategory_count = {}\nfor book in library['books']:\n    category = book['category']\n    category_count[category] = category_count.get(category, 0) + 1\n\nprint(f\"\\n分类统计: {category_count}\")\n\n# 查找用户借阅的书籍\nuser_id = 'user1'\nuser = library['members'][user_id]\nborrowed_titles = []\nfor book_id in user['borrowed']:\n    for book in library['books']:\n        if book['id'] == book_id:\n            borrowed_titles.append(book['title'])\n            break\n\nprint(f\"\\n{user['name']}借阅的书籍: {borrowed_titles}\")\n\n# 添加新书\nnew_book = {\n    'id': len(library['books']) + 1,\n    'title': '新书名',\n    'author': '新作者',\n    'category': '计算机',\n    'available': True\n}\nlibrary['books'].append(new_book)\nlibrary['categories'].add(new_book['category'])\n\nprint(f\"\\n图书总数: {len(library['books'])}\")\nprint(f\"分类总数: {len(library['categories'])}\")",
                    "explanation": "综合运用了列表、字典、集合来构建完整的数据管理系统"
                }
            ],
            "exercises": [
                {
                    "title": "销售数据分析",
                    "description": "分析销售数据，统计各种指标",
                    "hint": "使用多种数据结构存储和分析数据",
                    "solution": "sales_data = [\n    {'date': '2024-01-01', 'product': 'A', 'amount': 100, 'region': '北京'},\n    {'date': '2024-01-01', 'product': 'B', 'amount': 150, 'region': '上海'},\n    {'date': '2024-01-02', 'product': 'A', 'amount': 120, 'region': '北京'},\n    {'date': '2024-01-02', 'product': 'C', 'amount': 200, 'region': '广州'}\n]\n\n# 按产品统计销量\nproduct_sales = {}\nfor sale in sales_data:\n    product = sale['product']\n    product_sales[product] = product_sales.get(product, 0) + sale['amount']\n\nprint(\"产品销量:\", product_sales)\n\n# 按地区统计\nregion_sales = {}\nfor sale in sales_data:\n    region = sale['region']\n    region_sales[region] = region_sales.get(region, 0) + sale['amount']\n\nprint(\"地区销量:\", region_sales)"
                }
            ]
        }
    } 