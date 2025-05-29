#!/usr/bin/env python3
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
        print("\n" + "-" * 30)
        
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
        print(f"\n✅ 结果: {num1} {operator} {num2} = {result}")
        
        # 询问是否继续
        continue_calc = input("\n是否继续计算？(y/n): ")
        if continue_calc.lower() != 'y':
            break
    
    print("👋 感谢使用计算器！")

if __name__ == "__main__":
    calculator()
