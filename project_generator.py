#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
项目生成器
为每周学习内容生成对应的实践项目
"""

import os
from pathlib import Path

def generate_all_projects():
    """生成所有13周的项目文件"""
    base_path = Path(__file__).parent / "projects"
    base_path.mkdir(exist_ok=True)
    
    projects = [
        {"week": 1, "name": "计算器程序", "generator": generate_calculator_project},
        {"week": 2, "name": "猜数字游戏", "generator": generate_guess_game_project},
        {"week": 3, "name": "学生成绩管理", "generator": generate_grade_manager_project},
        {"week": 4, "name": "文本文件处理器", "generator": generate_file_processor_project},
        {"week": 5, "name": "网页数据抓取", "generator": generate_web_scraper_project},
        {"week": 6, "name": "数据分析小工具", "generator": generate_data_analysis_project},
        {"week": 7, "name": "简单Web应用", "generator": generate_web_app_project},
        {"week": 8, "name": "数据库应用", "generator": generate_database_project},
        {"week": 9, "name": "API服务开发", "generator": generate_api_project},
        {"week": 10, "name": "多线程应用", "generator": generate_threading_project},
        {"week": 11, "name": "机器学习入门", "generator": generate_ml_project},
        {"week": 12, "name": "项目部署", "generator": generate_deployment_project},
        {"week": 13, "name": "综合项目", "generator": generate_final_project}
    ]
    
    for project in projects:
        week_path = base_path / f"week_{project['week']}"
        week_path.mkdir(exist_ok=True)
        project["generator"](week_path)
        print(f"✅ 第{project['week']}周项目已生成: {project['name']}")

def generate_calculator_project(project_path):
    """第1周项目：计算器程序"""
    
    # README文件
    readme_content = """# 第1周项目：计算器程序

## 项目目标
使用Python基础语法制作一个简单的计算器程序，能够进行四则运算。

## 学习要点
- 变量和数据类型
- 用户输入和输出
- 基本运算符
- 条件语句

## 项目要求
1. 能够接受用户输入两个数字
2. 选择运算符（+、-、*、/）
3. 计算并显示结果
4. 处理除零错误
5. 支持连续计算

## 实现步骤
1. 设计程序流程
2. 实现基本运算功能
3. 添加错误处理
4. 美化输出格式
5. 添加循环功能

## 扩展功能
- 支持更多运算（平方、开方等）
- 添加历史记录功能
- 实现简单的GUI界面

## 完成标准
- [ ] 基本四则运算
- [ ] 错误处理
- [ ] 用户友好的界面
- [ ] 代码注释完整
"""

    # 基础版本
    basic_calculator = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单计算器 - 基础版本
第1周项目
"""

def add(x, y):
    """加法运算"""
    return x + y

def subtract(x, y):
    """减法运算"""
    return x - y

def multiply(x, y):
    """乘法运算"""
    return x * y

def divide(x, y):
    """除法运算"""
    if y != 0:
        return x / y
    else:
        return "错误：除数不能为零"

def calculator():
    """主计算器函数"""
    print("🧮 欢迎使用简单计算器！")
    print("支持的运算: +、-、*、/")
    print("输入 'quit' 退出程序")
    
    while True:
        print("\\n" + "-" * 30)
        
        # 获取第一个数字
        try:
            num1 = float(input("请输入第一个数字: "))
        except ValueError:
            print("❌ 请输入有效的数字！")
            continue
        
        # 获取运算符
        operator = input("请输入运算符 (+、-、*、/): ")
        if operator not in ['+', '-', '*', '/']:
            print("❌ 无效的运算符！")
            continue
        
        # 获取第二个数字
        try:
            num2 = float(input("请输入第二个数字: "))
        except ValueError:
            print("❌ 请输入有效的数字！")
            continue
        
        # 执行运算
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        
        # 显示结果
        print(f"\\n✅ 结果: {num1} {operator} {num2} = {result}")
        
        # 询问是否继续
        continue_calc = input("\\n是否继续计算？(y/n): ")
        if continue_calc.lower() != 'y':
            break
    
    print("👋 感谢使用计算器！")

if __name__ == "__main__":
    calculator()
'''

    # 高级版本
    advanced_calculator = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单计算器 - 高级版本
第1周项目 - 扩展功能
"""

import math

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, x, y):
        result = x + y
        self.history.append(f"{x} + {y} = {result}")
        return result
    
    def subtract(self, x, y):
        result = x - y
        self.history.append(f"{x} - {y} = {result}")
        return result
    
    def multiply(self, x, y):
        result = x * y
        self.history.append(f"{x} * {y} = {result}")
        return result
    
    def divide(self, x, y):
        if y == 0:
            return "错误：除数不能为零"
        result = x / y
        self.history.append(f"{x} / {y} = {result}")
        return result
    
    def power(self, x, y):
        result = x ** y
        self.history.append(f"{x} ^ {y} = {result}")
        return result
    
    def sqrt(self, x):
        if x < 0:
            return "错误：负数无法开平方根"
        result = math.sqrt(x)
        self.history.append(f"√{x} = {result}")
        return result
    
    def show_history(self):
        if not self.history:
            print("📝 暂无计算历史")
            return
        
        print("\\n📝 计算历史:")
        for i, record in enumerate(self.history[-10:], 1):
            print(f"  {i}. {record}")
    
    def clear_history(self):
        self.history.clear()
        print("✅ 历史记录已清空")
    
    def run(self):
        print("🧮 欢迎使用高级计算器！")
        print("支持的运算: +、-、*、/、^(幂运算)、√(开方)")
        print("特殊命令: history(历史记录)、clear(清空历史)、quit(退出)")
        
        while True:
            print("\\n" + "="*40)
            choice = input("请选择操作类型:\\n1. 基本运算\\n2. 查看历史\\n3. 清空历史\\n4. 退出\\n选择: ")
            
            if choice == '1':
                self.basic_operation()
            elif choice == '2':
                self.show_history()
            elif choice == '3':
                self.clear_history()
            elif choice == '4':
                print("👋 感谢使用计算器！")
                break
            else:
                print("❌ 无效选择！")
    
    def basic_operation(self):
        try:
            num1 = float(input("请输入第一个数字: "))
            operator = input("请输入运算符 (+、-、*、/、^、√): ")
            
            if operator == '√':
                result = self.sqrt(num1)
            else:
                num2 = float(input("请输入第二个数字: "))
                
                if operator == '+':
                    result = self.add(num1, num2)
                elif operator == '-':
                    result = self.subtract(num1, num2)
                elif operator == '*':
                    result = self.multiply(num1, num2)
                elif operator == '/':
                    result = self.divide(num1, num2)
                elif operator == '^':
                    result = self.power(num1, num2)
                else:
                    print("❌ 无效的运算符！")
                    return
            
            print(f"\\n✅ 结果: {result}")
            
        except ValueError:
            print("❌ 请输入有效的数字！")
        except Exception as e:
            print(f"❌ 发生错误: {e}")

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
'''

    # 写入文件
    with open(project_path / "README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    with open(project_path / "basic_calculator.py", 'w', encoding='utf-8') as f:
        f.write(basic_calculator)
    
    with open(project_path / "advanced_calculator.py", 'w', encoding='utf-8') as f:
        f.write(advanced_calculator)

def generate_guess_game_project(project_path):
    """第2周项目：猜数字游戏"""
    
    readme_content = """# 第2周项目：猜数字游戏

## 项目目标
制作一个猜数字游戏，玩家需要在限定次数内猜出随机生成的数字。

## 学习要点
- 条件语句的深入使用
- 循环结构（while, for）
- 随机数生成
- 函数定义和调用

## 项目要求
1. 生成1-100之间的随机数
2. 玩家输入猜测数字
3. 给出"太大"或"太小"的提示
4. 限制猜测次数
5. 记录最佳成绩

## 扩展功能
- 难度选择（不同数字范围）
- 排行榜功能
- 多轮游戏统计
"""
    
    game_code = '''#!/usr/bin/env python3
"""
猜数字游戏
第2周项目
"""

import random

class GuessNumberGame:
    def __init__(self):
        self.best_score = float('inf')
        self.games_played = 0
        self.total_attempts = 0
    
    def play_game(self, min_num=1, max_num=100, max_attempts=7):
        """开始游戏"""
        target = random.randint(min_num, max_num)
        attempts = 0
        
        print(f"\\n🎯 猜数字游戏开始！")
        print(f"我想了一个{min_num}到{max_num}之间的数字")
        print(f"你有{max_attempts}次机会猜中它！")
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"\\n第{attempts + 1}次猜测: "))
                attempts += 1
                
                if guess == target:
                    print(f"🎉 恭喜！你猜中了！数字是{target}")
                    print(f"用了{attempts}次尝试")
                    
                    # 更新最佳成绩
                    if attempts < self.best_score:
                        self.best_score = attempts
                        print("🏆 新纪录！")
                    
                    self.games_played += 1
                    self.total_attempts += attempts
                    return True
                    
                elif guess < target:
                    remaining = max_attempts - attempts
                    if remaining > 0:
                        print(f"📈 太小了！还有{remaining}次机会")
                else:
                    remaining = max_attempts - attempts
                    if remaining > 0:
                        print(f"📉 太大了！还有{remaining}次机会")
                        
            except ValueError:
                print("❌ 请输入有效数字！")
                attempts -= 1
        
        print(f"\\n💔 游戏结束！正确答案是{target}")
        self.games_played += 1
        self.total_attempts += attempts
        return False
    
    def show_stats(self):
        """显示游戏统计"""
        print("\\n📊 游戏统计:")
        print(f"游戏次数: {self.games_played}")
        if self.games_played > 0:
            avg_attempts = self.total_attempts / self.games_played
            print(f"平均尝试次数: {avg_attempts:.1f}")
        if self.best_score != float('inf'):
            print(f"最佳成绩: {self.best_score}次")
    
    def run(self):
        """运行游戏主循环"""
        print("🎮 欢迎来到猜数字游戏！")
        
        while True:
            print("\\n" + "="*30)
            print("1. 开始游戏（简单：1-50）")
            print("2. 开始游戏（普通：1-100）")
            print("3. 开始游戏（困难：1-200）")
            print("4. 查看统计")
            print("5. 退出游戏")
            
            choice = input("请选择: ")
            
            if choice == '1':
                self.play_game(1, 50, 6)
            elif choice == '2':
                self.play_game(1, 100, 7)
            elif choice == '3':
                self.play_game(1, 200, 8)
            elif choice == '4':
                self.show_stats()
            elif choice == '5':
                print("👋 感谢游戏！")
                break
            else:
                print("❌ 无效选择！")

if __name__ == "__main__":
    game = GuessNumberGame()
    game.run()
'''
    
    with open(project_path / "README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    with open(project_path / "guess_game.py", 'w', encoding='utf-8') as f:
        f.write(game_code)

# 为简化代码，其他项目生成函数使用简化版本
def generate_grade_manager_project(project_path):
    """第3周项目：学生成绩管理"""
    readme = "# 第3周项目：学生成绩管理\\n\\n使用列表和字典管理学生成绩数据。"
    code = "# 学生成绩管理系统\\n# TODO: 实现学生信息和成绩管理功能"
    
    with open(project_path / "README.md", 'w') as f:
        f.write(readme)
    with open(project_path / "grade_manager.py", 'w') as f:
        f.write(code)

def generate_file_processor_project(project_path):
    """第4周项目：文本文件处理器"""
    readme = "# 第4周项目：文本文件处理器\\n\\n实现文件读写和异常处理。"
    code = "# 文本文件处理器\\n# TODO: 实现文件操作功能"
    
    with open(project_path / "README.md", 'w') as f:
        f.write(readme)
    with open(project_path / "file_processor.py", 'w') as f:
        f.write(code)

# 继续实现其他项目生成函数...
def generate_web_scraper_project(project_path):
    """第5周项目：网页数据抓取"""
    pass

def generate_data_analysis_project(project_path):
    """第6周项目：数据分析小工具"""
    pass

def generate_web_app_project(project_path):
    """第7周项目：简单Web应用"""
    pass

def generate_database_project(project_path):
    """第8周项目：数据库应用"""
    pass

def generate_api_project(project_path):
    """第9周项目：API服务开发"""
    pass

def generate_threading_project(project_path):
    """第10周项目：多线程应用"""
    pass

def generate_ml_project(project_path):
    """第11周项目：机器学习入门"""
    pass

def generate_deployment_project(project_path):
    """第12周项目：项目部署"""
    pass

def generate_final_project(project_path):
    """第13周项目：综合项目"""
    pass

if __name__ == "__main__":
    generate_all_projects() 