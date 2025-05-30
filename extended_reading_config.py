#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
拓展阅读配置文件
为每天的课程提供官方Python文档和额外学习资源
"""

def get_extended_reading_config():
    """获取所有课程的拓展阅读配置"""
    return {
        "5": {
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
        },
        
        "6": {
            "title": "拓展阅读",
            "description": "深入理解Python的条件语句和控制流",
            "materials": [
                {
                    "title": "Python官方教程 - 控制流",
                    "url": "https://docs.python.org/zh-cn/3/tutorial/controlflow.html",
                    "description": "官方教程中关于if语句和控制流的详细说明",
                    "type": "official_doc"
                },
                {
                    "title": "复合语句参考",
                    "url": "https://docs.python.org/zh-cn/3/reference/compound_stmts.html#the-if-statement",
                    "description": "if语句的语法和语义完整参考",
                    "type": "official_doc"
                },
                {
                    "title": "布尔运算",
                    "url": "https://docs.python.org/zh-cn/3/library/stdtypes.html#boolean-operations-and-or-not",
                    "description": "布尔运算符and、or、not的详细说明",
                    "type": "official_doc"
                },
                {
                    "title": "真值测试",
                    "url": "https://docs.python.org/zh-cn/3/library/stdtypes.html#truth-value-testing",
                    "description": "Python中什么值被认为是False或True",
                    "type": "official_doc"
                }
            ],
            "tips": [
                "Python使用缩进来表示代码块，注意保持一致",
                "可以使用elif避免过多的嵌套if语句",
                "布尔运算符有短路求值特性",
                "空列表、空字符串、0等都被认为是False"
            ]
        },
        
        "7": {
            "title": "拓展阅读",
            "description": "第一周知识总结和编程最佳实践",
            "materials": [
                {
                    "title": "Python编程常见问题",
                    "url": "https://docs.python.org/zh-cn/3/faq/programming.html",
                    "description": "Python编程中的常见问题和解决方案",
                    "type": "official_doc"
                },
                {
                    "title": "代码风格指南 PEP 8",
                    "url": "https://peps.python.org/pep-0008/",
                    "description": "Python代码风格的官方指南",
                    "type": "best_practice"
                },
                {
                    "title": "Python术语表",
                    "url": "https://docs.python.org/zh-cn/3/glossary.html",
                    "description": "Python中重要术语的定义和解释",
                    "type": "official_doc"
                },
                {
                    "title": "Python HOWTOs",
                    "url": "https://docs.python.org/zh-cn/3/howto/index.html",
                    "description": "Python实用主题的详细指南",
                    "type": "official_doc"
                }
            ],
            "tips": [
                "多练习是掌握编程的关键",
                "阅读他人的代码可以学到很多技巧",
                "遵循PEP 8代码风格让代码更易读",
                "善用Python内置函数和标准库"
            ]
        },
        
        "8": {
            "title": "拓展阅读",
            "description": "深入学习Python列表和序列类型",
            "materials": [
                {
                    "title": "Python官方教程 - 列表",
                    "url": "https://docs.python.org/zh-cn/3/tutorial/introduction.html#lists",
                    "description": "官方教程中关于列表的基础介绍",
                    "type": "official_doc"
                },
                {
                    "title": "序列类型参考",
                    "url": "https://docs.python.org/zh-cn/3/library/stdtypes.html#sequence-types-list-tuple-range",
                    "description": "列表、元组、range等序列类型的完整参考",
                    "type": "official_doc"
                },
                {
                    "title": "列表方法详解",
                    "url": "https://docs.python.org/zh-cn/3/tutorial/datastructures.html#more-on-lists",
                    "description": "列表的各种方法和用法的详细说明",
                    "type": "official_doc"
                },
                {
                    "title": "序列和其他类型的比较",
                    "url": "https://docs.python.org/zh-cn/3/tutorial/datastructures.html#comparing-sequences-and-other-types",
                    "description": "序列类型之间的比较和转换",
                    "type": "official_doc"
                }
            ],
            "tips": [
                "列表是可变的，可以修改其内容",
                "负索引从列表末尾开始计数",
                "切片操作返回新列表，不修改原列表",
                "list()函数可以将其他序列转换为列表"
            ]
        },
        
        "9": {
            "title": "拓展阅读",
            "description": "深入理解Python的for循环和迭代",
            "materials": [
                {
                    "title": "Python官方教程 - for语句",
                    "url": "https://docs.python.org/zh-cn/3/tutorial/controlflow.html#for-statements",
                    "description": "官方教程中关于for循环的详细说明",
                    "type": "official_doc"
                },
                {
                    "title": "range()函数参考",
                    "url": "https://docs.python.org/zh-cn/3/library/functions.html#func-range",
                    "description": "range()函数的官方文档和用法",
                    "type": "official_doc"
                },
                {
                    "title": "迭代器和生成器",
                    "url": "https://docs.python.org/zh-cn/3/tutorial/classes.html#iterators",
                    "description": "Python迭代协议的深入介绍",
                    "type": "official_doc"
                },
                {
                    "title": "enumerate()函数",
                    "url": "https://docs.python.org/zh-cn/3/library/functions.html#enumerate",
                    "description": "enumerate()函数的用法和示例",
                    "type": "official_doc"
                }
            ],
            "tips": [
                "for循环比while循环更适合遍历序列",
                "range()返回的是一个迭代器，不是列表",
                "enumerate()可以同时获取索引和值",
                "zip()函数可以并行遍历多个序列"
            ]
        },
        
        "10": {
            "title": "拓展阅读",
            "description": "深入学习while循环和循环控制",
            "materials": [
                {
                    "title": "Python官方教程 - while语句",
                    "url": "https://docs.python.org/zh-cn/3/tutorial/controlflow.html#while-statements",
                    "description": "官方教程中关于while循环的详细介绍",
                    "type": "official_doc"
                },
                {
                    "title": "循环控制语句",
                    "url": "https://docs.python.org/zh-cn/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops",
                    "description": "break、continue语句和循环的else子句",
                    "type": "official_doc"
                },
                {
                    "title": "复合语句 - while",
                    "url": "https://docs.python.org/zh-cn/3/reference/compound_stmts.html#the-while-statement",
                    "description": "while语句的语法和语义参考",
                    "type": "official_doc"
                }
            ],
            "tips": [
                "while循环适用于不确定循环次数的情况",
                "注意避免无限循环，确保循环条件会改变",
                "else子句在循环正常结束时执行",
                "使用break和continue控制循环流程"
            ]
        },
        
        "15": {
            "title": "拓展阅读",
            "description": "深入理解Python的元组和集合数据结构",
            "materials": [
                {
                    "title": "Python官方教程 - 元组和序列",
                    "url": "https://docs.python.org/zh-cn/3/tutorial/datastructures.html#tuples-and-sequences",
                    "description": "官方教程中关于元组和序列的详细说明",
                    "type": "official_doc"
                },
                {
                    "title": "集合类型参考",
                    "url": "https://docs.python.org/zh-cn/3/library/stdtypes.html#set-types-set-frozenset",
                    "description": "集合和不可变集合的完整参考文档",
                    "type": "official_doc"
                },
                {
                    "title": "数据结构详解",
                    "url": "https://docs.python.org/zh-cn/3/tutorial/datastructures.html",
                    "description": "Python数据结构的完整教程",
                    "type": "official_doc"
                }
            ],
            "tips": [
                "元组是不可变的，适合存储不需要修改的数据",
                "集合自动去重，适合去除重复元素",
                "使用元组拆包可以优雅地交换变量",
                "集合支持数学运算：并集、交集、差集"
            ]
        },
        
        "20": {
            "title": "拓展阅读",
            "description": "深入学习正则表达式和文本处理",
            "materials": [
                {
                    "title": "正则表达式HOWTO",
                    "url": "https://docs.python.org/zh-cn/3/howto/regex.html",
                    "description": "Python正则表达式的详细指南和教程",
                    "type": "official_doc"
                },
                {
                    "title": "re模块参考",
                    "url": "https://docs.python.org/zh-cn/3/library/re.html",
                    "description": "re模块的完整API参考文档",
                    "type": "official_doc"
                },
                {
                    "title": "字符串服务",
                    "url": "https://docs.python.org/zh-cn/3/library/string.html",
                    "description": "Python字符串处理服务的完整参考",
                    "type": "official_doc"
                }
            ],
            "tips": [
                "正则表达式是强大的文本处理工具",
                "使用原始字符串r''编写正则表达式",
                "先用简单模式测试，再构建复杂表达式",
                "注意正则表达式的性能，避免过度复杂"
            ]
        },
        
        "22": {
            "title": "拓展阅读", 
            "description": "深入理解Python函数的设计和使用",
            "materials": [
                {
                    "title": "Python官方教程 - 函数",
                    "url": "https://docs.python.org/zh-cn/3/tutorial/controlflow.html#defining-functions",
                    "description": "官方教程中关于函数定义和使用的详细说明",
                    "type": "official_doc"
                },
                {
                    "title": "函数式编程HOWTO",
                    "url": "https://docs.python.org/zh-cn/3/howto/functional.html",
                    "description": "Python函数式编程的概念和技巧",
                    "type": "official_doc"
                },
                {
                    "title": "函数调用表达式",
                    "url": "https://docs.python.org/zh-cn/3/reference/expressions.html#calls",
                    "description": "函数调用的语法和语义参考",
                    "type": "official_doc"
                },
                {
                    "title": "代码风格 - 函数设计",
                    "url": "https://peps.python.org/pep-0008/#function-and-variable-names",
                    "description": "PEP 8中关于函数命名和设计的建议",
                    "type": "best_practice"
                }
            ],
            "tips": [
                "函数名应该清楚地描述函数的功能",
                "保持函数简短，专注于单一职责",
                "使用文档字符串描述函数的用途",
                "考虑使用类型提示提高代码可读性"
            ]
        },
        
        "25": {
            "title": "拓展阅读",
            "description": "深入理解递归算法和函数式编程",
            "materials": [
                {
                    "title": "递归算法思想",
                    "url": "https://docs.python.org/zh-cn/3/tutorial/controlflow.html#defining-functions",
                    "description": "理解递归的数学基础和编程应用",
                    "type": "official_doc"
                },
                {
                    "title": "函数式编程特性",
                    "url": "https://docs.python.org/zh-cn/3/howto/functional.html",
                    "description": "Python中的函数式编程概念和工具",
                    "type": "official_doc"
                },
                {
                    "title": "算法与数据结构",
                    "url": "https://docs.python.org/zh-cn/3/tutorial/datastructures.html",
                    "description": "Python数据结构和算法的基础知识",
                    "type": "official_doc"
                }
            ],
            "tips": [
                "递归必须有明确的基准条件避免无限递归",
                "考虑递归的时间和空间复杂度",
                "有些递归问题可以用迭代解决",
                "理解尾递归优化的概念"
            ]
        },
        
        "30": {
            "title": "拓展阅读", 
            "description": "Python学习路径和进阶方向",
            "materials": [
                {
                    "title": "Python开发者指南",
                    "url": "https://devguide.python.org/",
                    "description": "Python开发的完整指南和最佳实践",
                    "type": "official_doc"
                },
                {
                    "title": "Python增强提案(PEPs)",
                    "url": "https://peps.python.org/",
                    "description": "了解Python语言的发展和设计决策",
                    "type": "official_doc"
                },
                {
                    "title": "Python包索引(PyPI)",
                    "url": "https://pypi.org/",
                    "description": "探索Python生态系统中的第三方库",
                    "type": "official_doc"
                },
                {
                    "title": "Python进阶主题",
                    "url": "https://docs.python.org/zh-cn/3/howto/index.html",
                    "description": "各种Python进阶主题的详细指南",
                    "type": "official_doc"
                }
            ],
            "tips": [
                "持续学习是程序员的重要品质",
                "参与开源项目提升编程技能",
                "选择专业方向深入学习",
                "建立个人项目展示技能",
                "加入Python社区与他人交流"
            ]
        }
    } 