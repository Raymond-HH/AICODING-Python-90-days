#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 90天学习系统
主程序入口

作者: Python培训老师
版本: 1.0
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

class PythonLearningSystem:
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.progress_file = self.base_path / "progress.json"
        self.curriculum_file = self.base_path / "curriculum.json"
        self.current_day = 1
        self.load_progress()
        self.load_curriculum()
    
    def load_progress(self):
        """加载学习进度"""
        if self.progress_file.exists():
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                self.progress = json.load(f)
        else:
            self.progress = {
                "start_date": datetime.now().strftime("%Y-%m-%d"),
                "current_day": 1,
                "completed_days": [],
                "notes": {},
                "weekly_projects": {}
            }
            self.save_progress()
    
    def load_curriculum(self):
        """加载课程大纲"""
        if self.curriculum_file.exists():
            with open(self.curriculum_file, 'r', encoding='utf-8') as f:
                self.curriculum = json.load(f)
        else:
            print("课程大纲文件不存在，请先生成课程大纲！")
            sys.exit(1)
    
    def save_progress(self):
        """保存学习进度"""
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.progress, f, ensure_ascii=False, indent=2)
    
    def show_main_menu(self):
        """显示主菜单"""
        print("\n" + "="*50)
        print("🐍 Python 90天学习系统 🐍")
        print("="*50)
        print(f"📅 开始日期: {self.progress['start_date']}")
        print(f"📊 当前进度: 第 {self.progress['current_day']} 天")
        print(f"✅ 已完成: {len(self.progress['completed_days'])} 天")
        print("-"*50)
        print("1. 📖 今日学习内容")
        print("2. 📋 查看学习计划")
        print("3. ✅ 完成今日学习")
        print("4. 📊 学习进度统计")
        print("5. 📝 添加学习笔记")
        print("6. 🎯 每周项目")
        print("7. 🔧 系统设置")
        print("0. 退出系统")
        print("-"*50)
    
    def show_today_content(self):
        """显示今日学习内容"""
        day = self.progress['current_day']
        if day > 90:
            print("🎉 恭喜！您已完成90天Python学习计划！")
            return
        
        # 确定当前级别和周次
        if day <= 30:
            level = "初级"
            week = (day - 1) // 7 + 1
        elif day <= 60:
            level = "中级"
            week = (day - 31) // 7 + 1
        else:
            level = "高级"
            week = (day - 61) // 7 + 1
        
        day_type = "复习" if day % 7 == 0 else "学习"
        
        print(f"\n📖 第 {day} 天 - {level}阶段 第{week}周 ({day_type})")
        print("="*80)
        
        # 获取今日内容
        day_content = self.get_day_content(day)
        if day_content:
            print(f"📚 主题: {day_content['topic']}")
            print(f"⏰ 预计学习时间: {day_content['duration']}")
            print(f"🎯 学习目标: {day_content['objectives']}")
            
            # 显示核心概念
            if 'concepts' in day_content:
                print("\n" + "="*60)
                print("📋 核心概念")
                print("="*60)
                for i, concept in enumerate(day_content['concepts'], 1):
                    print(f"\n{i}. {concept['name']}")
                    print(f"   {concept['description']}")
                    if 'details' in concept:
                        for detail in concept['details']:
                            print(f"   • {detail}")
            
            # 显示代码示例
            if 'examples' in day_content and isinstance(day_content['examples'], list) and day_content['examples']:
                print("\n" + "="*60)
                print("💡 代码示例")
                print("="*60)
                for i, example in enumerate(day_content['examples'], 1):
                    if isinstance(example, dict):
                        print(f"\n示例 {i}: {example['title']}")
                        print("-" * 40)
                        print(example['code'])
                        print(f"\n说明: {example['explanation']}")
                    else:
                        print(f"  {i}. {example}")
            elif day_content.get('examples'):
                print("\n💡 示例代码:")
                for example in day_content['examples']:
                    print(f"  - {example}")
            
            # 显示练习题
            if 'exercises' in day_content and isinstance(day_content['exercises'], list) and day_content['exercises']:
                print("\n" + "="*60)
                print("🏃‍♂️ 练习题")
                print("="*60)
                for i, exercise in enumerate(day_content['exercises'], 1):
                    if isinstance(exercise, dict):
                        print(f"\n练习 {i}: {exercise['title']}")
                        print(f"描述: {exercise['description']}")
                        if 'hint' in exercise:
                            print(f"提示: {exercise['hint']}")
                        
                        # 询问是否显示答案
                        show_solution = input(f"\n是否查看练习{i}的参考答案？(y/n): ").lower()
                        if show_solution == 'y':
                            print("参考答案:")
                            print("-" * 30)
                            print(exercise.get('solution', '暂无答案'))
                        print("-" * 50)
                    else:
                        print(f"  {i}. {exercise}")
            elif day_content.get('exercises'):
                print("\n🏃‍♂️ 练习任务:")
                for exercise in day_content['exercises']:
                    print(f"  - {exercise}")
                    
            # 显示学习资源
            if day_content.get('resources'):
                print("\n" + "="*60)
                print("📖 学习资源")
                print("="*60)
                for resource in day_content['resources']:
                    print(f"  • {resource}")
            
            # 显示学习建议
            print("\n" + "="*60)
            print("💡 学习建议")
            print("="*60)
            print("1. 仔细阅读每个概念的解释，确保理解")
            print("2. 运行每个代码示例，观察输出结果")
            print("3. 尝试修改示例代码，看看会发生什么")
            print("4. 独立完成所有练习题")
            print("5. 如果遇到问题，先尝试自己解决，再查看答案")
            print("6. 在学习笔记中记录重点和疑问")
            
        else:
            print("❌ 未找到今日学习内容")
            # 尝试从扩展内容获取
            from course_content_manager import get_extended_curriculum
            extended_content = get_extended_curriculum()
            if str(day) in extended_content:
                print("📚 正在加载扩展内容...")
                extended_day_content = extended_content[str(day)]
                self.display_extended_content(extended_day_content)
    
    def display_extended_content(self, content):
        """显示扩展的学习内容"""
        print(f"📚 主题: {content['topic']}")
        print(f"⏰ 预计学习时间: {content['duration']}")
        print(f"🎯 学习目标: {content['objectives']}")
        
        # 显示核心概念
        print("\n" + "="*60)
        print("📋 核心概念")
        print("="*60)
        for i, concept in enumerate(content['concepts'], 1):
            print(f"\n{i}. {concept['name']}")
            print(f"   {concept['description']}")
            for detail in concept['details']:
                print(f"   • {detail}")
        
        # 显示代码示例
        print("\n" + "="*60)
        print("💡 代码示例")
        print("="*60)
        for i, example in enumerate(content['examples'], 1):
            print(f"\n示例 {i}: {example['title']}")
            print("-" * 40)
            print(example['code'])
            print(f"\n说明: {example['explanation']}")
        
        # 显示练习题
        print("\n" + "="*60)
        print("🏃‍♂️ 练习题")
        print("="*60)
        for i, exercise in enumerate(content['exercises'], 1):
            print(f"\n练习 {i}: {exercise['title']}")
            print(f"描述: {exercise['description']}")
            if 'hint' in exercise:
                print(f"提示: {exercise['hint']}")
            
            # 询问是否显示答案
            show_solution = input(f"\n是否查看练习{i}的参考答案？(y/n): ").lower()
            if show_solution == 'y':
                print("参考答案:")
                print("-" * 30)
                print(exercise.get('solution', '暂无答案'))
            print("-" * 50)
    
    def get_day_content(self, day):
        """获取指定天数的学习内容"""
        # 首先尝试从完整课程数据库获取
        try:
            from complete_course_database import get_complete_course_database
            complete_database = get_complete_course_database()
            if str(day) in complete_database:
                return complete_database[str(day)]
        except ImportError:
            pass
        
        # 如果完整数据库中没有，则从原始curriculum获取
        for level_data in self.curriculum.values():
            if isinstance(level_data, dict) and 'days' in level_data:
                if str(day) in level_data['days']:
                    return level_data['days'][str(day)]
        
        # 尝试从扩展内容获取
        try:
            from course_content_manager import get_extended_curriculum
            extended_content = get_extended_curriculum()
            if str(day) in extended_content:
                return extended_content[str(day)]
        except ImportError:
            pass
            
        return None
    
    def mark_day_complete(self):
        """标记今日学习完成"""
        day = self.progress['current_day']
        if day not in self.progress['completed_days']:
            self.progress['completed_days'].append(day)
            print(f"✅ 第 {day} 天学习已完成！")
            
            # 检查是否可以进入下一天
            if day < 90:
                self.progress['current_day'] += 1
                print(f"🚀 已解锁第 {self.progress['current_day']} 天的内容！")
            else:
                print("🎉 恭喜完成90天Python学习计划！")
            
            self.save_progress()
        else:
            print(f"ℹ️ 第 {day} 天已经完成过了")
    
    def show_progress_stats(self):
        """显示学习进度统计"""
        total_days = 90
        completed = len(self.progress['completed_days'])
        completion_rate = (completed / total_days) * 100
        
        print("\n📊 学习进度统计")
        print("="*40)
        print(f"总学习天数: {total_days} 天")
        print(f"已完成天数: {completed} 天")
        print(f"完成进度: {completion_rate:.1f}%")
        print(f"剩余天数: {total_days - completed} 天")
        
        # 进度条
        bar_length = 30
        filled_length = int(bar_length * completed / total_days)
        bar = "█" * filled_length + "░" * (bar_length - filled_length)
        print(f"进度条: [{bar}] {completion_rate:.1f}%")
        
        # 估算完成时间
        if completed > 0:
            start_date = datetime.strptime(self.progress['start_date'], "%Y-%m-%d")
            days_passed = len(self.progress['completed_days'])
            avg_days_per_real_day = days_passed / (datetime.now() - start_date).days if (datetime.now() - start_date).days > 0 else 1
            remaining_real_days = (total_days - completed) / avg_days_per_real_day
            estimated_completion = datetime.now() + timedelta(days=remaining_real_days)
            print(f"预计完成日期: {estimated_completion.strftime('%Y-%m-%d')}")
    
    def add_notes(self):
        """添加学习笔记"""
        day = self.progress['current_day']
        print(f"\n📝 为第 {day} 天添加学习笔记:")
        note = input("请输入您的学习笔记: ")
        
        if note.strip():
            self.progress['notes'][str(day)] = {
                'content': note,
                'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.save_progress()
            print("✅ 笔记已保存！")
        else:
            print("❌ 笔记内容不能为空")
    
    def show_weekly_projects(self):
        """显示每周项目"""
        print("\n🎯 每周实践项目")
        print("="*50)
        
        current_week = (self.progress['current_day'] - 1) // 7 + 1
        
        # 显示所有周的项目
        for week in range(1, 14):  # 13周
            if week <= 4:
                level = "初级"
                week_in_level = week
            elif week <= 8:
                level = "中级"
                week_in_level = week - 4
            else:
                level = "高级"
                week_in_level = week - 8
            
            status = "🟢" if week < current_week else "🟡" if week == current_week else "⚪"
            print(f"{status} 第{week}周 ({level} 第{week_in_level}周)")
            
            project = self.get_weekly_project(week)
            if project:
                print(f"   📋 项目: {project['name']}")
                print(f"   🎯 目标: {project['description']}")
                if week <= current_week:
                    print(f"   📁 文件: ./projects/week_{week}/")
                print()
    
    def get_weekly_project(self, week):
        """获取指定周的项目信息"""
        weekly_projects = {
            1: {"name": "计算器程序", "description": "使用基本语法制作简单计算器"},
            2: {"name": "猜数字游戏", "description": "运用条件语句和循环制作游戏"},
            3: {"name": "学生成绩管理", "description": "使用列表和字典管理数据"},
            4: {"name": "文本文件处理器", "description": "文件操作和异常处理实践"},
            5: {"name": "网页数据抓取", "description": "使用requests和BeautifulSoup"},
            6: {"name": "数据分析小工具", "description": "pandas和matplotlib入门"},
            7: {"name": "简单Web应用", "description": "Flask框架基础应用"},
            8: {"name": "数据库应用", "description": "SQLite数据库操作"},
            9: {"name": "API服务开发", "description": "RESTful API设计与实现"},
            10: {"name": "多线程应用", "description": "并发编程实践"},
            11: {"name": "机器学习入门", "description": "scikit-learn基础应用"},
            12: {"name": "项目部署", "description": "Docker和云部署"},
            13: {"name": "综合项目", "description": "整合所有技能的完整项目"}
        }
        return weekly_projects.get(week)
    
    def run(self):
        """运行主程序"""
        while True:
            self.show_main_menu()
            choice = input("\n请选择操作 (0-7): ").strip()
            
            if choice == '1':
                self.show_today_content()
            elif choice == '2':
                self.show_curriculum_overview()
            elif choice == '3':
                self.mark_day_complete()
            elif choice == '4':
                self.show_progress_stats()
            elif choice == '5':
                self.add_notes()
            elif choice == '6':
                self.show_weekly_projects()
            elif choice == '7':
                self.system_settings()
            elif choice == '0':
                print("👋 感谢使用Python学习系统，祝学习愉快！")
                break
            else:
                print("❌ 无效选择，请重新输入")
            
            input("\n按回车键继续...")
    
    def show_curriculum_overview(self):
        """显示课程大纲概览"""
        print("\n📋 Python 90天学习大纲")
        print("="*60)
        
        levels = ["初级", "中级", "高级"]
        for i, level in enumerate(levels):
            start_day = i * 30 + 1
            end_day = (i + 1) * 30
            print(f"\n📚 {level}阶段 (第{start_day}-{end_day}天)")
            print("-" * 40)
            
            # 显示该级别的周计划
            for week in range(1, 5):
                week_start = start_day + (week - 1) * 7
                week_end = min(week_start + 6, end_day)
                print(f"  第{week}周 (第{week_start}-{week_end}天)")
                
                # 这里可以添加具体的周主题
                week_topics = self.get_week_topics(i + 1, week)
                if week_topics:
                    for topic in week_topics:
                        print(f"    • {topic}")
    
    def get_week_topics(self, level, week):
        """获取指定级别和周次的主题"""
        topics = {
            1: {  # 初级
                1: ["Python基础语法", "变量和数据类型", "运算符"],
                2: ["条件语句", "循环结构", "基础函数"],
                3: ["列表和元组", "字典和集合", "字符串处理"],
                4: ["文件操作", "异常处理", "模块导入"]
            },
            2: {  # 中级
                1: ["面向对象编程", "类和对象", "继承多态"],
                2: ["装饰器", "生成器", "上下文管理器"],
                3: ["正则表达式", "网络编程", "多线程"],
                4: ["数据库操作", "Web开发基础", "测试框架"]
            },
            3: {  # 高级
                1: ["设计模式", "性能优化", "内存管理"],
                2: ["异步编程", "并发处理", "分布式系统"],
                3: ["机器学习", "数据科学", "Web框架"],
                4: ["项目部署", "CI/CD", "综合项目"]
            }
        }
        return topics.get(level, {}).get(week, [])
    
    def system_settings(self):
        """系统设置"""
        print("\n🔧 系统设置")
        print("="*30)
        print("1. 重置学习进度")
        print("2. 备份学习数据")
        print("3. 恢复学习数据")
        print("0. 返回主菜单")
        
        choice = input("\n请选择操作: ").strip()
        
        if choice == '1':
            confirm = input("⚠️ 确认重置所有学习进度？(yes/no): ")
            if confirm.lower() == 'yes':
                self.progress = {
                    "start_date": datetime.now().strftime("%Y-%m-%d"),
                    "current_day": 1,
                    "completed_days": [],
                    "notes": {},
                    "weekly_projects": {}
                }
                self.save_progress()
                print("✅ 学习进度已重置")
        elif choice == '2':
            self.backup_data()
        elif choice == '3':
            self.restore_data()

    def backup_data(self):
        """备份学习数据"""
        backup_dir = self.base_path / "backup"
        backup_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = backup_dir / f"progress_backup_{timestamp}.json"
        
        import shutil
        shutil.copy2(self.progress_file, backup_file)
        print(f"✅ 数据已备份到: {backup_file}")

    def restore_data(self):
        """恢复学习数据"""
        backup_dir = self.base_path / "backup"
        if not backup_dir.exists():
            print("❌ 没有找到备份文件")
            return
        
        backup_files = list(backup_dir.glob("progress_backup_*.json"))
        if not backup_files:
            print("❌ 没有找到备份文件")
            return
        
        print("📁 可用的备份文件:")
        for i, file in enumerate(backup_files):
            print(f"  {i+1}. {file.name}")
        
        try:
            choice = int(input("请选择要恢复的备份 (输入数字): ")) - 1
            if 0 <= choice < len(backup_files):
                import shutil
                shutil.copy2(backup_files[choice], self.progress_file)
                self.load_progress()
                print("✅ 数据恢复成功")
            else:
                print("❌ 无效选择")
        except ValueError:
            print("❌ 请输入有效数字")


if __name__ == "__main__":
    # 检查是否需要初始化课程大纲
    curriculum_path = Path(__file__).parent / "curriculum.json"
    if not curriculum_path.exists():
        print("🚀 首次运行，正在初始化学习系统...")
        from detailed_curriculum import generate_complete_curriculum
        generate_complete_curriculum()
        print("✅ 课程大纲生成完成！")
    
    # 启动学习系统
    system = PythonLearningSystem()
    system.run() 