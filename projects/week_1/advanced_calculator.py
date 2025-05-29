#!/usr/bin/env python3
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
        
        print("\n📝 计算历史:")
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
            print("\n" + "="*40)
            choice = input("请选择操作类型:\n1. 基本运算\n2. 查看历史\n3. 清空历史\n4. 退出\n选择: ")
            
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
            
            print(f"\n✅ 结果: {result}")
            
        except ValueError:
            print("❌ 请输入有效的数字！")
        except Exception as e:
            print(f"❌ 发生错误: {e}")

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
