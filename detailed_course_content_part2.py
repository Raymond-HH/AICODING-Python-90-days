#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
详细的Python课程内容 - 第二部分
包含第19-30天的具体学习材料、代码示例和练习题
"""

def get_detailed_course_content_part2():
    """获取第19-30天的详细课程内容"""
    return {
        "19": {
            "topic": "字符串高级操作",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "掌握字符串的高级方法和处理技巧",
            "concepts": [
                {
                    "name": "字符串方法",
                    "description": "字符串的常用内置方法",
                    "details": [
                        "strip()：去除首尾空白字符",
                        "split()：分割字符串为列表",
                        "join()：用分隔符连接列表元素",
                        "replace()：替换字符串中的内容"
                    ]
                },
                {
                    "name": "字符串检查",
                    "description": "检查字符串的状态和内容",
                    "details": [
                        "startswith()、endswith()：检查开头和结尾",
                        "isdigit()、isalpha()：检查字符类型",
                        "find()、index()：查找子字符串位置",
                        "count()：统计子字符串出现次数"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "字符串高级操作示例",
                    "code": "# 字符串清理\ntext = \"  Hello, World!  \"\nprint(f\"原始: '{text}'\")\nprint(f\"去空格: '{text.strip()}'\")\nprint(f\"小写: '{text.strip().lower()}'\")\nprint(f\"大写: '{text.strip().upper()}'\")\n\n# 字符串分割和连接\nsentence = \"Python is awesome and powerful\"\nwords = sentence.split()\nprint(f\"分割成单词: {words}\")\n\n# 用不同分隔符连接\njoined = \"-\".join(words)\nprint(f\"用-连接: {joined}\")\n\n# 字符串替换\noriginal = \"I love Java programming\"\nreplaced = original.replace(\"Java\", \"Python\")\nprint(f\"替换后: {replaced}\")\n\n# 字符串检查\nemail = \"user@example.com\"\nprint(f\"是否以user开头: {email.startswith('user')}\")\nprint(f\"是否以.com结尾: {email.endswith('.com')}\")\nprint(f\"@的位置: {email.find('@')}\")\n\n# 字符串格式化\nname = \"张三\"\nage = 25\nscore = 89.5\n\n# 多种格式化方式\nprint(f\"f字符串: {name}今年{age}岁，成绩{score:.1f}分\")\nprint(\"format方法: {}今年{}岁，成绩{:.1f}分\".format(name, age, score))\nprint(\"百分号格式: %s今年%d岁，成绩%.1f分\" % (name, age, score))\n\n# 文本处理实例\ndata = \"apple,banana,orange,grape\"\nfruits = [fruit.strip().title() for fruit in data.split(',')]\nprint(f\"处理后的水果: {fruits}\")",
                    "explanation": "展示了字符串的清理、分割、连接、替换、检查和格式化等高级操作"
                }
            ],
            "exercises": [
                {
                    "title": "文本清理器",
                    "description": "编写程序清理和格式化文本数据",
                    "hint": "使用strip()、replace()、title()等方法",
                    "solution": "text = \"  hello, WORLD! this is PYTHON programming.  \"\n# 清理文本\nclean_text = text.strip().lower().replace('!', '').replace(',', '')\nwords = clean_text.split()\ncapitalized = [word.capitalize() for word in words]\nresult = ' '.join(capitalized)\nprint(f\"清理后: {result}\")"
                }
            ]
        },
        
        "20": {
            "topic": "正则表达式入门",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "了解正则表达式的基本概念和简单应用",
            "concepts": [
                {
                    "name": "正则表达式基础",
                    "description": "用于匹配文本模式的强大工具",
                    "details": [
                        "导入re模块：import re",
                        "基本匹配：re.search()、re.match()、re.findall()",
                        "常用元字符：. * + ? [] ^ $ |",
                        "转义字符：使用\\来匹配特殊字符"
                    ]
                },
                {
                    "name": "常用模式",
                    "description": "实用的正则表达式模式",
                    "details": [
                        "\\d：匹配数字",
                        "\\w：匹配字母、数字、下划线",
                        "\\s：匹配空白字符",
                        "[a-z]：匹配小写字母范围"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "正则表达式基础示例",
                    "code": "import re\n\n# 基本匹配\ntext = \"我的电话是13812345678，邮箱是user@example.com\"\n\n# 查找电话号码\nphone_pattern = r'\\d{11}'\nphone = re.search(phone_pattern, text)\nif phone:\n    print(f\"找到电话: {phone.group()}\")\n\n# 查找邮箱\nemail_pattern = r'\\w+@\\w+\\.\\w+'\nemail = re.search(email_pattern, text)\nif email:\n    print(f\"找到邮箱: {email.group()}\")\n\n# 查找所有数字\nnumbers = re.findall(r'\\d+', \"价格：99元，折扣：85%，库存：100件\")\nprint(f\"所有数字: {numbers}\")\n\n# 字符串替换\noriginal = \"今天是2024年5月30日\"\n# 将日期格式改为 2024-05-30\ndate_pattern = r'(\\d{4})年(\\d+)月(\\d+)日'\nreplaced = re.sub(date_pattern, r'\\1-\\2-\\3', original)\nprint(f\"替换后: {replaced}\")\n\n# 验证格式\ndef validate_phone(phone):\n    pattern = r'^1[3-9]\\d{9}$'\n    return bool(re.match(pattern, phone))\n\ntest_phones = ['13812345678', '12345678901', '1381234567']\nfor phone in test_phones:\n    valid = validate_phone(phone)\n    print(f\"{phone}: {'有效' if valid else '无效'}\")\n\n# 分割文本\nsentence = \"苹果，香蕉；橙子：葡萄\"\nfruits = re.split(r'[，；：]', sentence)\nprint(f\"分割结果: {fruits}\")",
                    "explanation": "展示了正则表达式的查找、替换、验证和分割功能"
                }
            ],
            "exercises": [
                {
                    "title": "信息提取器",
                    "description": "从文本中提取电话号码、邮箱和日期",
                    "hint": "使用re.findall()查找所有匹配项",
                    "solution": "import re\n\ntext = '''\n联系人：张三，电话：13812345678，邮箱：zhangsan@email.com\n日期：2024年5月30日，备用电话：13987654321\n'''\n\n# 提取电话\nphones = re.findall(r'1[3-9]\\d{9}', text)\nprint(f\"电话号码: {phones}\")\n\n# 提取邮箱\nemails = re.findall(r'\\w+@\\w+\\.\\w+', text)\nprint(f\"邮箱地址: {emails}\")\n\n# 提取日期\ndates = re.findall(r'\\d{4}年\\d+月\\d+日', text)\nprint(f\"日期: {dates}\")"
                }
            ]
        },
        
        "21": {
            "topic": "第三周复习与项目",
            "level": "初级",
            "duration": "2-3小时",
            "objectives": "巩固数据结构和字符串处理知识，完成综合项目",
            "concepts": [
                {
                    "name": "知识整合",
                    "description": "回顾第三周学习内容",
                    "details": [
                        "元组、集合、字典的使用",
                        "数据结构的选择和组合",
                        "字符串的高级处理",
                        "正则表达式的基本应用"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "通讯录管理系统",
                    "code": "import re\n\nclass ContactManager:\n    def __init__(self):\n        self.contacts = {}\n    \n    def add_contact(self, name, phone, email):\n        # 验证电话格式\n        if not re.match(r'^1[3-9]\\d{9}$', phone):\n            return False, \"电话号码格式不正确\"\n        \n        # 验证邮箱格式\n        if not re.match(r'^\\w+@\\w+\\.\\w+$', email):\n            return False, \"邮箱格式不正确\"\n        \n        self.contacts[name] = {\n            'phone': phone,\n            'email': email,\n            'tags': set()\n        }\n        return True, \"联系人添加成功\"\n    \n    def search_contact(self, keyword):\n        results = []\n        for name, info in self.contacts.items():\n            if (keyword.lower() in name.lower() or \n                keyword in info['phone'] or \n                keyword.lower() in info['email'].lower()):\n                results.append((name, info))\n        return results\n    \n    def add_tag(self, name, tag):\n        if name in self.contacts:\n            self.contacts[name]['tags'].add(tag)\n            return True\n        return False\n    \n    def get_contacts_by_tag(self, tag):\n        return [(name, info) for name, info in self.contacts.items() \n                if tag in info['tags']]\n    \n    def export_data(self):\n        result = []\n        for name, info in self.contacts.items():\n            tags = ', '.join(info['tags']) if info['tags'] else '无'\n            result.append(f\"{name},{info['phone']},{info['email']},{tags}\")\n        return '\\n'.join(result)\n\n# 使用示例\nmanager = ContactManager()\n\n# 添加联系人\ncontacts_data = [\n    ('张三', '13812345678', 'zhangsan@email.com'),\n    ('李四', '13987654321', 'lisi@email.com'),\n    ('王五', '13756789012', 'wangwu@email.com')\n]\n\nfor name, phone, email in contacts_data:\n    success, message = manager.add_contact(name, phone, email)\n    print(f\"添加{name}: {message}\")\n\n# 添加标签\nmanager.add_tag('张三', '同事')\nmanager.add_tag('张三', '朋友')\nmanager.add_tag('李四', '同学')\n\n# 搜索联系人\nprint(\"\\n搜索结果（关键词：张）:\")\nresults = manager.search_contact('张')\nfor name, info in results:\n    print(f\"{name}: {info['phone']}, {info['email']}\")\n\n# 按标签查找\nprint(\"\\n同事标签的联系人:\")\ncolleagues = manager.get_contacts_by_tag('同事')\nfor name, info in colleagues:\n    print(f\"{name}: {info['phone']}\")\n\n# 导出数据\nprint(\"\\n导出数据:\")\nprint(manager.export_data())",
                    "explanation": "综合运用了字典、集合、正则表达式和类的概念构建完整的通讯录系统"
                }
            ],
            "exercises": [
                {
                    "title": "文本分析器",
                    "description": "分析文本的各种统计信息",
                    "hint": "使用字典统计、集合去重、正则匹配",
                    "solution": "import re\n\ndef analyze_text(text):\n    # 字符统计\n    char_count = len(text)\n    \n    # 单词统计\n    words = re.findall(r'\\b\\w+\\b', text.lower())\n    word_count = len(words)\n    unique_words = len(set(words))\n    \n    # 词频统计\n    word_freq = {}\n    for word in words:\n        word_freq[word] = word_freq.get(word, 0) + 1\n    \n    # 最高频词汇\n    most_common = max(word_freq.items(), key=lambda x: x[1]) if word_freq else ('', 0)\n    \n    return {\n        '字符数': char_count,\n        '单词数': word_count,\n        '不重复单词数': unique_words,\n        '最高频词汇': most_common,\n        '词频表': word_freq\n    }\n\ntext = 'Python is great. Python is easy. Python is powerful.'\nresult = analyze_text(text)\nfor key, value in result.items():\n    print(f'{key}: {value}')"
                }
            ]
        },
        
        "22": {
            "topic": "函数定义与调用",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "掌握函数的定义、调用和基本使用",
            "concepts": [
                {
                    "name": "函数基础",
                    "description": "函数是可重用的代码块",
                    "details": [
                        "使用def关键字定义函数",
                        "函数名遵循变量命名规则",
                        "使用return返回值",
                        "函数调用时使用函数名加括号"
                    ]
                },
                {
                    "name": "函数的优势",
                    "description": "使用函数的好处",
                    "details": [
                        "代码重用：避免重复代码",
                        "模块化：将复杂问题分解",
                        "易于测试和调试",
                        "提高代码可读性"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "函数定义与调用示例",
                    "code": "# 简单函数定义\ndef greet():\n    print(\"Hello, World!\")\n\n# 调用函数\ngreet()\n\n# 带参数的函数\ndef greet_person(name):\n    print(f\"Hello, {name}!\")\n\ngreet_person(\"张三\")\ngreet_person(\"李四\")\n\n# 带返回值的函数\ndef add_numbers(a, b):\n    result = a + b\n    return result\n\n# 使用返回值\nsum1 = add_numbers(5, 3)\nsum2 = add_numbers(10, 20)\nprint(f\"5 + 3 = {sum1}\")\nprint(f\"10 + 20 = {sum2}\")\n\n# 多个参数的函数\ndef calculate_rectangle_area(length, width):\n    area = length * width\n    return area\n\n# 计算面积\narea1 = calculate_rectangle_area(5, 3)\narea2 = calculate_rectangle_area(10, 8)\nprint(f\"矩形面积: {area1}, {area2}\")\n\n# 函数文档字符串\ndef calculate_bmi(weight, height):\n    \"\"\"\n    计算BMI指数\n    \n    参数:\n    weight: 体重(kg)\n    height: 身高(m)\n    \n    返回:\n    BMI指数\n    \"\"\"\n    bmi = weight / (height ** 2)\n    return bmi\n\n# 使用带文档的函数\nbmi = calculate_bmi(70, 1.75)\nprint(f\"BMI: {bmi:.2f}\")\n\n# 查看函数文档\nprint(calculate_bmi.__doc__)\n\n# 条件返回\ndef check_grade(score):\n    if score >= 90:\n        return \"优秀\"\n    elif score >= 80:\n        return \"良好\"\n    elif score >= 70:\n        return \"中等\"\n    elif score >= 60:\n        return \"及格\"\n    else:\n        return \"不及格\"\n\n# 测试成绩评定\nscores = [95, 85, 75, 65, 55]\nfor score in scores:\n    grade = check_grade(score)\n    print(f\"分数{score}: {grade}\")",
                    "explanation": "展示了函数的定义、参数传递、返回值、文档字符串等基本概念"
                }
            ],
            "exercises": [
                {
                    "title": "温度转换器",
                    "description": "编写函数实现摄氏度和华氏度的相互转换",
                    "hint": "华氏度 = 摄氏度 * 9/5 + 32",
                    "solution": "def celsius_to_fahrenheit(celsius):\n    \"\"\"摄氏度转华氏度\"\"\"\n    return celsius * 9/5 + 32\n\ndef fahrenheit_to_celsius(fahrenheit):\n    \"\"\"华氏度转摄氏度\"\"\"\n    return (fahrenheit - 32) * 5/9\n\n# 测试\nprint(f\"0°C = {celsius_to_fahrenheit(0)}°F\")\nprint(f\"100°C = {celsius_to_fahrenheit(100)}°F\")\nprint(f\"32°F = {fahrenheit_to_celsius(32)}°C\")\nprint(f\"212°F = {fahrenheit_to_celsius(212)}°C\")"
                }
            ]
        },
        
        "23": {
            "topic": "函数参数与返回值",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "掌握函数参数的各种形式和返回值的使用",
            "concepts": [
                {
                    "name": "参数类型",
                    "description": "函数参数的不同形式",
                    "details": [
                        "位置参数：按顺序传递",
                        "关键字参数：指定参数名",
                        "默认参数：设置默认值",
                        "*args：可变位置参数",
                        "**kwargs：可变关键字参数"
                    ]
                },
                {
                    "name": "返回值",
                    "description": "函数返回值的使用",
                    "details": [
                        "单个返回值",
                        "多个返回值（元组）",
                        "None返回值",
                        "早期返回"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "函数参数与返回值示例",
                    "code": "# 默认参数\ndef greet(name, greeting=\"你好\"):\n    return f\"{greeting}, {name}!\"\n\nprint(greet(\"张三\"))  # 使用默认值\nprint(greet(\"李四\", \"欢迎\"))  # 指定参数值\n\n# 关键字参数\ndef create_profile(name, age, city=\"未知\", job=\"未知\"):\n    return f\"姓名：{name}，年龄：{age}，城市：{city}，职业：{job}\"\n\n# 不同的调用方式\nprint(create_profile(\"张三\", 25))\nprint(create_profile(\"李四\", 30, job=\"程序员\"))\nprint(create_profile(name=\"王五\", age=28, city=\"北京\", job=\"教师\"))\n\n# 可变参数 *args\ndef calculate_sum(*numbers):\n    total = 0\n    for num in numbers:\n        total += num\n    return total\n\nprint(f\"求和: {calculate_sum(1, 2, 3, 4, 5)}\")\nprint(f\"求和: {calculate_sum(10, 20)}\")\n\n# 可变关键字参数 **kwargs\ndef print_info(**info):\n    for key, value in info.items():\n        print(f\"{key}: {value}\")\n\nprint(\"个人信息:\")\nprint_info(name=\"张三\", age=25, city=\"北京\", hobby=\"编程\")\n\n# 组合使用\ndef flexible_function(required, *args, **kwargs):\n    print(f\"必需参数: {required}\")\n    print(f\"位置参数: {args}\")\n    print(f\"关键字参数: {kwargs}\")\n\nflexible_function(\"必须的\", 1, 2, 3, name=\"张三\", age=25)\n\n# 多个返回值\ndef get_statistics(numbers):\n    if not numbers:\n        return None, None, None\n    \n    total = sum(numbers)\n    average = total / len(numbers)\n    max_val = max(numbers)\n    min_val = min(numbers)\n    \n    return total, average, max_val, min_val\n\n# 接收多个返回值\ndata = [10, 20, 30, 40, 50]\ntotal, avg, max_num, min_num = get_statistics(data)\nprint(f\"总和: {total}, 平均: {avg:.2f}, 最大: {max_num}, 最小: {min_num}\")\n\n# 函数作为参数\ndef apply_operation(numbers, operation):\n    return [operation(num) for num in numbers]\n\ndef square(x):\n    return x ** 2\n\ndef double(x):\n    return x * 2\n\nnumbers = [1, 2, 3, 4, 5]\nsquared = apply_operation(numbers, square)\ndoubled = apply_operation(numbers, double)\n\nprint(f\"原数列: {numbers}\")\nprint(f\"平方: {squared}\")\nprint(f\"翻倍: {doubled}\")",
                    "explanation": "展示了各种参数类型、多返回值和函数作为参数的高级用法"
                }
            ],
            "exercises": [
                {
                    "title": "计算器函数",
                    "description": "编写一个支持多种运算的计算器函数",
                    "hint": "使用默认参数和可变参数",
                    "solution": "def calculator(operation, *numbers, precision=2):\n    \"\"\"\n    计算器函数\n    operation: 运算类型 ('add', 'subtract', 'multiply', 'divide')\n    numbers: 可变数量的数字\n    precision: 结果精度，默认2位小数\n    \"\"\"\n    if not numbers:\n        return \"错误：需要至少一个数字\"\n    \n    if operation == 'add':\n        result = sum(numbers)\n    elif operation == 'multiply':\n        result = 1\n        for num in numbers:\n            result *= num\n    elif operation == 'subtract':\n        result = numbers[0]\n        for num in numbers[1:]:\n            result -= num\n    elif operation == 'divide':\n        result = numbers[0]\n        for num in numbers[1:]:\n            if num == 0:\n                return \"错误：除零\"\n            result /= num\n    else:\n        return \"错误：不支持的运算\"\n    \n    return round(result, precision)\n\n# 测试\nprint(calculator('add', 1, 2, 3, 4, 5))\nprint(calculator('multiply', 2, 3, 4))\nprint(calculator('divide', 100, 2, 5, precision=1))"
                }
            ]
        },
        
        "24": {
            "topic": "作用域与局部变量",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "理解变量作用域和生命周期",
            "concepts": [
                {
                    "name": "作用域概念",
                    "description": "变量的可访问范围",
                    "details": [
                        "全局作用域：在整个程序中可访问",
                        "局部作用域：只在函数内部可访问",
                        "global关键字：在函数内修改全局变量",
                        "nonlocal关键字：访问外层函数变量"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "作用域示例",
                    "code": "# 全局变量\ncounter = 0\n\ndef increment():\n    global counter\n    counter += 1\n    print(f\"计数器: {counter}\")\n\n# 局部变量\ndef calculate_area(radius):\n    pi = 3.14159  # 局部变量\n    area = pi * radius ** 2\n    return area\n\nincrement()\nincrement()\nprint(f\"面积: {calculate_area(5)}\")",
                    "explanation": "展示了全局变量和局部变量的使用"
                }
            ],
            "exercises": [
                {
                    "title": "计数器函数",
                    "description": "创建一个计数器函数，每次调用增加计数",
                    "hint": "使用global关键字",
                    "solution": "count = 0\n\ndef increment_counter():\n    global count\n    count += 1\n    return count\n\nprint(increment_counter())\nprint(increment_counter())"
                }
            ]
        },
        
        "25": {
            "topic": "递归函数",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "理解递归的概念和应用",
            "concepts": [
                {
                    "name": "递归基础",
                    "description": "函数调用自身的编程技巧",
                    "details": [
                        "递归条件：函数调用自身",
                        "基准条件：停止递归的条件",
                        "递归深度：避免无限递归",
                        "递归与循环的选择"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "递归示例",
                    "code": "# 阶乘函数\ndef factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\n\n# 斐波那契数列\ndef fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)\n\nprint(f\"5的阶乘: {factorial(5)}\")\nprint(f\"斐波那契第7项: {fibonacci(7)}\")",
                    "explanation": "展示了经典的递归算法"
                }
            ],
            "exercises": [
                {
                    "title": "递归求和",
                    "description": "使用递归计算1到n的和",
                    "hint": "n + sum(n-1)",
                    "solution": "def recursive_sum(n):\n    if n <= 1:\n        return n\n    return n + recursive_sum(n - 1)\n\nprint(recursive_sum(10))"
                }
            ]
        },
        
        "26": {
            "topic": "Lambda函数",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "掌握匿名函数的使用",
            "concepts": [
                {
                    "name": "Lambda表达式",
                    "description": "简短的匿名函数",
                    "details": [
                        "语法：lambda 参数: 表达式",
                        "只能包含一个表达式",
                        "常与map、filter、sort配合使用",
                        "适用于简单的函数逻辑"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "Lambda函数示例",
                    "code": "# 基本lambda\nsquare = lambda x: x ** 2\nprint(f\"平方: {square(5)}\")\n\n# 与map配合\nnumbers = [1, 2, 3, 4, 5]\nsquared = list(map(lambda x: x ** 2, numbers))\nprint(f\"平方数列: {squared}\")\n\n# 与filter配合\nevens = list(filter(lambda x: x % 2 == 0, numbers))\nprint(f\"偶数: {evens}\")\n\n# 排序\nstudents = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]\nstudents.sort(key=lambda x: x[1])\nprint(f\"按分数排序: {students}\")",
                    "explanation": "展示了lambda函数的各种应用场景"
                }
            ],
            "exercises": [
                {
                    "title": "数据处理",
                    "description": "使用lambda处理数据列表",
                    "hint": "结合map和filter使用",
                    "solution": "data = [1, 2, 3, 4, 5, 6]\nprocessed = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, data)))\nprint(processed)"
                }
            ]
        },
        
        "27": {
            "topic": "内置函数详解",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "掌握Python常用内置函数",
            "concepts": [
                {
                    "name": "数值函数",
                    "description": "处理数值的内置函数",
                    "details": [
                        "abs()：绝对值",
                        "max()、min()：最大最小值",
                        "sum()：求和",
                        "round()：四舍五入"
                    ]
                },
                {
                    "name": "序列函数",
                    "description": "处理序列的内置函数",
                    "details": [
                        "len()：长度",
                        "range()：生成数字序列",
                        "enumerate()：枚举",
                        "zip()：打包"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "内置函数示例",
                    "code": "# 数值函数\nnumbers = [-5, 3, 8, -2, 10]\nprint(f\"绝对值: {[abs(x) for x in numbers]}\")\nprint(f\"最大值: {max(numbers)}\")\nprint(f\"最小值: {min(numbers)}\")\nprint(f\"总和: {sum(numbers)}\")\n\n# 序列函数\nnames = ['Alice', 'Bob', 'Charlie']\nages = [25, 30, 35]\n\n# enumerate获取索引和值\nfor i, name in enumerate(names):\n    print(f\"{i}: {name}\")\n\n# zip打包多个序列\nfor name, age in zip(names, ages):\n    print(f\"{name}今年{age}岁\")\n\n# 类型转换函数\nprint(f\"字符串转整数: {int('123')}\")\nprint(f\"数字转字符串: {str(456)}\")\nprint(f\"转列表: {list(range(5))}\")",
                    "explanation": "展示了常用内置函数的使用方法"
                }
            ],
            "exercises": [
                {
                    "title": "数据统计",
                    "description": "使用内置函数进行数据统计",
                    "hint": "综合使用多个内置函数",
                    "solution": "scores = [85, 92, 78, 96, 88]\nprint(f\"最高分: {max(scores)}\")\nprint(f\"最低分: {min(scores)}\")\nprint(f\"平均分: {sum(scores) / len(scores):.1f}\")\nprint(f\"总分: {sum(scores)}\")"
                }
            ]
        },
        
        "28": {
            "topic": "第四周复习与项目",
            "level": "初级",
            "duration": "2-3小时",
            "objectives": "巩固函数知识，完成函数相关项目",
            "concepts": [
                {
                    "name": "函数设计原则",
                    "description": "编写高质量函数的原则",
                    "details": [
                        "单一职责：一个函数只做一件事",
                        "函数名要清晰描述功能",
                        "参数数量要合理",
                        "添加适当的文档字符串"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "学生成绩管理系统（函数版）",
                    "code": "def add_student(students, name, *scores):\n    \"\"\"添加学生及其成绩\"\"\"\n    students[name] = list(scores)\n    return f\"学生{name}添加成功\"\n\ndef calculate_average(scores):\n    \"\"\"计算平均分\"\"\"\n    return sum(scores) / len(scores) if scores else 0\n\ndef get_grade(score):\n    \"\"\"根据分数获取等级\"\"\"\n    if score >= 90:\n        return 'A'\n    elif score >= 80:\n        return 'B'\n    elif score >= 70:\n        return 'C'\n    elif score >= 60:\n        return 'D'\n    else:\n        return 'F'\n\ndef generate_report(students):\n    \"\"\"生成成绩报告\"\"\"\n    report = []\n    for name, scores in students.items():\n        avg = calculate_average(scores)\n        grade = get_grade(avg)\n        report.append({\n            'name': name,\n            'scores': scores,\n            'average': avg,\n            'grade': grade\n        })\n    return sorted(report, key=lambda x: x['average'], reverse=True)\n\n# 使用示例\nstudents = {}\nadd_student(students, '张三', 85, 90, 78)\nadd_student(students, '李四', 92, 88, 95)\nadd_student(students, '王五', 76, 82, 79)\n\nreport = generate_report(students)\nfor student in report:\n    print(f\"{student['name']}: 平均分{student['average']:.1f}, 等级{student['grade']}\")",
                    "explanation": "展示了如何用函数模块化地构建完整的管理系统"
                }
            ],
            "exercises": [
                {
                    "title": "数学计算库",
                    "description": "创建一个数学计算函数库",
                    "hint": "包含各种数学运算函数",
                    "solution": "def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n\ndef factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\n\ndef gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a\n\n# 测试\nprint(f\"7是素数: {is_prime(7)}\")\nprint(f\"5的阶乘: {factorial(5)}\")\nprint(f\"12和18的最大公约数: {gcd(12, 18)}\")"
                }
            ]
        },
        
        "29": {
            "topic": "错误处理基础",
            "level": "初级",
            "duration": "1-2小时",
            "objectives": "了解异常处理的基本概念",
            "concepts": [
                {
                    "name": "异常处理",
                    "description": "处理程序运行时的错误",
                    "details": [
                        "try-except语句捕获异常",
                        "finally子句：无论如何都会执行",
                        "else子句：没有异常时执行",
                        "常见异常类型：ValueError、TypeError等"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "异常处理示例",
                    "code": "# 基本异常处理\ndef safe_divide(a, b):\n    try:\n        result = a / b\n        print(f\"{a} ÷ {b} = {result}\")\n        return result\n    except ZeroDivisionError:\n        print(\"错误：除数不能为零\")\n        return None\n    except TypeError:\n        print(\"错误：参数类型不正确\")\n        return None\n\n# 用户输入处理\ndef get_number():\n    while True:\n        try:\n            num = float(input(\"请输入一个数字: \"))\n            return num\n        except ValueError:\n            print(\"输入无效，请输入数字\")\n\n# 测试\nsafe_divide(10, 2)\nsafe_divide(10, 0)\nsafe_divide(\"10\", 2)",
                    "explanation": "展示了异常处理在实际编程中的应用"
                }
            ],
            "exercises": [
                {
                    "title": "安全计算器",
                    "description": "创建一个能处理各种错误的计算器",
                    "hint": "使用try-except处理可能的异常",
                    "solution": "def safe_calculator():\n    try:\n        a = float(input(\"第一个数: \"))\n        op = input(\"运算符(+,-,*,/): \")\n        b = float(input(\"第二个数: \"))\n        \n        if op == '+':\n            return a + b\n        elif op == '-':\n            return a - b\n        elif op == '*':\n            return a * b\n        elif op == '/':\n            return a / b\n        else:\n            print(\"不支持的运算符\")\n    except ValueError:\n        print(\"输入格式错误\")\n    except ZeroDivisionError:\n        print(\"除数不能为零\")\n    \nresult = safe_calculator()\nif result is not None:\n    print(f\"结果: {result}\")"
                }
            ]
        },
        
        "30": {
            "topic": "第一月总结与展望",
            "level": "初级",
            "duration": "2-3小时",
            "objectives": "回顾第一个月的学习成果，规划后续学习",
            "concepts": [
                {
                    "name": "知识体系回顾",
                    "description": "总结30天的学习内容",
                    "details": [
                        "Python基础语法和环境搭建",
                        "数据类型：数字、字符串、布尔值",
                        "数据结构：列表、元组、字典、集合",
                        "控制流：条件语句和循环",
                        "函数：定义、参数、返回值、作用域",
                        "异常处理基础"
                    ]
                },
                {
                    "name": "编程思维培养",
                    "description": "培养的编程思维和技能",
                    "details": [
                        "问题分解：将复杂问题分解为简单步骤",
                        "抽象思维：使用函数封装重复逻辑",
                        "调试技能：找出并修复代码错误",
                        "代码规范：编写清晰可读的代码"
                    ]
                }
            ],
            "examples": [
                {
                    "title": "综合项目：个人财务管理器",
                    "code": "class FinanceManager:\n    def __init__(self):\n        self.transactions = []\n        self.balance = 0\n    \n    def add_income(self, amount, description=\"收入\"):\n        \"\"\"添加收入\"\"\"\n        try:\n            amount = float(amount)\n            if amount > 0:\n                self.transactions.append({\n                    'type': 'income',\n                    'amount': amount,\n                    'description': description,\n                    'date': self.get_current_date()\n                })\n                self.balance += amount\n                return f\"添加收入：{amount}元\"\n            else:\n                return \"收入金额必须大于0\"\n        except ValueError:\n            return \"金额格式不正确\"\n    \n    def add_expense(self, amount, description=\"支出\"):\n        \"\"\"添加支出\"\"\"\n        try:\n            amount = float(amount)\n            if amount > 0:\n                self.transactions.append({\n                    'type': 'expense',\n                    'amount': amount,\n                    'description': description,\n                    'date': self.get_current_date()\n                })\n                self.balance -= amount\n                return f\"添加支出：{amount}元\"\n            else:\n                return \"支出金额必须大于0\"\n        except ValueError:\n            return \"金额格式不正确\"\n    \n    def get_balance(self):\n        \"\"\"获取余额\"\"\"\n        return self.balance\n    \n    def get_summary(self):\n        \"\"\"获取财务摘要\"\"\"\n        income_total = sum(t['amount'] for t in self.transactions if t['type'] == 'income')\n        expense_total = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')\n        \n        return {\n            '总收入': income_total,\n            '总支出': expense_total,\n            '当前余额': self.balance,\n            '交易笔数': len(self.transactions)\n        }\n    \n    def get_current_date(self):\n        \"\"\"获取当前日期（简化版）\"\"\"\n        return \"2024-05-30\"\n    \n    def generate_report(self):\n        \"\"\"生成财务报告\"\"\"\n        summary = self.get_summary()\n        report = \"\\n=== 财务报告 ===\\n\"\n        for key, value in summary.items():\n            report += f\"{key}: {value}\\n\"\n        \n        report += \"\\n=== 最近交易 ===\\n\"\n        for transaction in self.transactions[-5:]:  # 显示最近5笔交易\n            report += f\"{transaction['date']} - {transaction['description']}: {transaction['amount']}元 ({transaction['type']})\\n\"\n        \n        return report\n\n# 使用示例\nfm = FinanceManager()\n\n# 添加一些交易\nprint(fm.add_income(5000, \"工资\"))\nprint(fm.add_expense(1200, \"房租\"))\nprint(fm.add_expense(800, \"生活费\"))\nprint(fm.add_income(500, \"兼职收入\"))\nprint(fm.add_expense(200, \"交通费\"))\n\n# 查看报告\nprint(fm.generate_report())",
                    "explanation": "综合运用了类、函数、异常处理、数据结构等知识构建完整的应用"
                }
            ],
            "exercises": [
                {
                    "title": "学习成果展示",
                    "description": "选择一个你感兴趣的小项目，运用学过的知识实现它",
                    "hint": "可以是游戏、工具、数据分析等任何你感兴趣的项目",
                    "solution": "# 这是一个开放性练习，鼓励学生发挥创意\n# 示例：简单的待办事项管理器\ntodo_list = []\n\ndef add_task(task):\n    todo_list.append({'task': task, 'completed': False})\n    print(f\"任务已添加: {task}\")\n\ndef complete_task(index):\n    if 0 <= index < len(todo_list):\n        todo_list[index]['completed'] = True\n        print(f\"任务已完成: {todo_list[index]['task']}\")\n    else:\n        print(\"任务编号不存在\")\n\ndef show_tasks():\n    for i, task in enumerate(todo_list):\n        status = \"✓\" if task['completed'] else \"○\"\n        print(f\"{i}: {status} {task['task']}\")\n\n# 测试\nadd_task(\"学习Python\")\nadd_task(\"完成作业\")\nshow_tasks()\ncomplete_task(0)\nshow_tasks()"
                }
            ]
        }
    } 