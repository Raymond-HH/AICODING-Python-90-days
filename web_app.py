#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python学习系统 - Web版本
基于Flask框架的现代化学习平台

版本: 2.0
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
import sys

# 添加当前目录到Python路径，确保能导入我们的模块
sys.path.append(str(Path(__file__).parent))

try:
    from complete_course_database import get_complete_course_database
    from course_content_manager import get_extended_curriculum
except ImportError as e:
    print(f"警告：无法导入课程模块: {e}")

app = Flask(__name__)
app.secret_key = 'python_learning_system_2024'  # 用于session管理

class WebLearningSystem:
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.progress_file = self.base_path / "progress.json"
        self.curriculum_file = self.base_path / "curriculum.json"
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
            self.curriculum = {"error": "课程大纲文件不存在"}
    
    def save_progress(self):
        """保存学习进度"""
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.progress, f, ensure_ascii=False, indent=2)
    
    def get_day_content(self, day):
        """获取指定天数的学习内容"""
        # 首先尝试从详细课程内容获取
        try:
            from detailed_course_content import get_detailed_course_content
            detailed_content = get_detailed_course_content()
            if str(day) in detailed_content:
                content = detailed_content[str(day)]
                # 如果没有拓展阅读，尝试添加
                if 'extended_reading' not in content:
                    content = self._add_extended_reading(content, day)
                return content
        except Exception as e:
            print(f"无法加载详细课程内容: {e}")
        
        # 尝试从第二部分详细课程内容获取
        try:
            from detailed_course_content_part2 import get_detailed_course_content_part2
            detailed_content_part2 = get_detailed_course_content_part2()
            if str(day) in detailed_content_part2:
                content = detailed_content_part2[str(day)]
                # 如果没有拓展阅读，尝试添加
                if 'extended_reading' not in content:
                    content = self._add_extended_reading(content, day)
                return content
        except Exception as e:
            print(f"无法加载第二部分详细课程内容: {e}")
        
        # 尝试从完整课程数据库获取
        try:
            complete_database = get_complete_course_database()
            if str(day) in complete_database:
                content = complete_database[str(day)]
                content = self._add_extended_reading(content, day)
                return content
        except:
            pass
        
        # 尝试从扩展内容获取
        try:
            extended_content = get_extended_curriculum()
            if str(day) in extended_content:
                content = extended_content[str(day)]
                content = self._add_extended_reading(content, day)
                return content
        except:
            pass
        
        # 尝试从简单课程内容获取
        try:
            from simple_course_content import get_simple_course_content
            simple_content = get_simple_course_content()
            if str(day) in simple_content:
                content = simple_content[str(day)]
                content = self._add_extended_reading(content, day)
                return content
        except:
            pass
        
        # 使用完整课程大纲作为后备
        try:
            from complete_curriculum import get_complete_curriculum
            complete_curriculum = get_complete_curriculum()
            if str(day) in complete_curriculum:
                curriculum_data = complete_curriculum[str(day)]
                # 构建基本的内容结构
                content = {
                    "topic": curriculum_data["topic"],
                    "level": curriculum_data["level"],
                    "duration": "1-2小时",
                    "objectives": f"掌握{curriculum_data['topic']}的核心概念和实践应用",
                    "concepts": [
                        {
                            "name": curriculum_data["topic"],
                            "description": f"第{day}天的主要学习内容",
                            "details": [
                                "理论学习与概念理解",
                                "实践练习与代码编写",
                                "问题解决与调试技巧"
                            ]
                        }
                    ],
                    "examples": [
                        {
                            "title": f"{curriculum_data['topic']}示例",
                            "code": "# 第" + str(day) + "天：" + curriculum_data['topic'] + "\n# 示例代码将在课程中详细讲解\nprint('今天学习：" + curriculum_data['topic'] + "')",
                            "explanation": "这是今天学习内容的示例代码"
                        }
                    ],
                    "exercises": [
                        {
                            "title": "今日练习",
                            "description": f"完成{curriculum_data['topic']}相关的练习题",
                            "hint": "仔细阅读课程内容，动手实践",
                            "solution": "# 解答将在课程中提供"
                        }
                    ]
                }
                content = self._add_extended_reading(content, day)
                return content
        except Exception as e:
            print(f"无法加载完整课程大纲: {e}")
        
        # 从原始curriculum获取
        for level_data in self.curriculum.values():
            if isinstance(level_data, dict) and 'days' in level_data:
                if str(day) in level_data['days']:
                    content = level_data['days'][str(day)]
                    content = self._add_extended_reading(content, day)
                    return content
        
        # 如果都没有，返回默认内容
        content = {
            "topic": f"第{day}天课程",
            "duration": "1-2小时", 
            "objectives": "学习Python编程技能",
            "concepts": [
                {
                    "name": "课程内容",
                    "description": f"第{day}天的学习内容正在准备中...",
                    "details": ["课程内容即将发布", "请继续关注"]
                }
            ],
            "examples": [
                {
                    "title": "示例代码",
                    "code": "# 第{}天示例代码\nprint(\"今天我们学习Python编程！\")".format(day),
                    "explanation": "这是一个简单的示例"
                }
            ],
            "exercises": [
                {
                    "title": "练习题",
                    "description": "完成今天的学习任务",
                    "hint": "仔细阅读课程内容",
                    "solution": "# 解答将在后续提供"
                }
            ]
        }
        content = self._add_extended_reading(content, day)
        return content
    
    def _add_extended_reading(self, content, day):
        """为课程内容添加拓展阅读"""
        try:
            from extended_reading_config import get_extended_reading_config
            extended_config = get_extended_reading_config()
            
            if str(day) in extended_config:
                content['extended_reading'] = extended_config[str(day)]
            else:
                # 提供默认的拓展阅读
                content['extended_reading'] = {
                    "title": "拓展阅读",
                    "description": "官方文档和学习资源",
                    "materials": [
                        {
                            "title": "Python官方教程",
                            "url": "https://docs.python.org/zh-cn/3/tutorial/index.html",
                            "description": "Python官方教程，权威的学习资源",
                            "type": "official_doc"
                        },
                        {
                            "title": "Python标准库",
                            "url": "https://docs.python.org/zh-cn/3/library/index.html",
                            "description": "Python标准库完整参考",
                            "type": "official_doc"
                        }
                    ],
                    "tips": [
                        "多练习是学习编程的最佳方式",
                        "善用官方文档查找详细信息",
                        "加入Python社区，与其他开发者交流"
                    ]
                }
        except Exception as e:
            print(f"无法加载拓展阅读配置: {e}")
            # 如果加载失败，提供基本的拓展阅读
            content['extended_reading'] = {
                "title": "拓展阅读",
                "description": "推荐的学习资源",
                "materials": [
                    {
                        "title": "Python官方文档",
                        "url": "https://docs.python.org/zh-cn/3/",
                        "description": "Python官方文档，最权威的参考资料",
                        "type": "official_doc"
                    }
                ],
                "tips": ["持续练习，多读官方文档"]
            }
        
        return content
    
    def get_progress_stats(self):
        """获取学习进度统计"""
        total_days = 90
        completed = len(self.progress['completed_days'])
        completion_rate = (completed / total_days) * 100
        
        return {
            'total_days': total_days,
            'completed_days': completed,
            'completion_rate': completion_rate,
            'remaining_days': total_days - completed,
            'current_day': self.progress['current_day']
        }
    
    def mark_day_complete(self, day):
        """标记指定天完成"""
        day = int(day)
        if day not in self.progress['completed_days']:
            self.progress['completed_days'].append(day)
            if day == self.progress['current_day'] and day < 90:
                self.progress['current_day'] += 1
            self.save_progress()
            return True
        return False
    
    def add_note(self, day, content):
        """添加学习笔记"""
        self.progress['notes'][str(day)] = {
            'content': content,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.save_progress()
    
    def update_note(self, day, content):
        """更新学习笔记"""
        if str(day) in self.progress['notes']:
            self.progress['notes'][str(day)]['content'] = content
            self.progress['notes'][str(day)]['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_progress()
            return True
        return False
    
    def delete_note(self, day):
        """删除学习笔记"""
        if str(day) in self.progress['notes']:
            del self.progress['notes'][str(day)]
            self.save_progress()
            return True
        return False
    
    def get_weekly_projects(self):
        """获取所有周项目信息"""
        projects = {
            1: {"name": "计算器程序", "description": "使用基本语法制作简单计算器", "level": "初级"},
            2: {"name": "猜数字游戏", "description": "运用条件语句和循环制作游戏", "level": "初级"},
            3: {"name": "学生成绩管理", "description": "使用列表和字典管理数据", "level": "初级"},
            4: {"name": "文本文件处理器", "description": "文件操作和异常处理实践", "level": "初级"},
            5: {"name": "网页数据抓取", "description": "使用requests和BeautifulSoup", "level": "中级"},
            6: {"name": "数据分析小工具", "description": "pandas和matplotlib入门", "level": "中级"},
            7: {"name": "简单Web应用", "description": "Flask框架基础应用", "level": "中级"},
            8: {"name": "数据库应用", "description": "SQLite数据库操作", "level": "中级"},
            9: {"name": "API服务开发", "description": "RESTful API设计与实现", "level": "高级"},
            10: {"name": "多线程应用", "description": "并发编程实践", "level": "高级"},
            11: {"name": "机器学习入门", "description": "scikit-learn基础应用", "level": "高级"},
            12: {"name": "项目部署", "description": "Docker和云部署", "level": "高级"},
            13: {"name": "综合项目", "description": "整合所有技能的完整项目", "level": "高级"}
        }
        
        current_week = (self.progress['current_day'] - 1) // 7 + 1
        for week, project in projects.items():
            if week < current_week:
                project['status'] = 'completed'
            elif week == current_week:
                project['status'] = 'current'
            else:
                project['status'] = 'locked'
        
        return projects

# 创建全局系统实例
learning_system = WebLearningSystem()

@app.route('/')
def index():
    """主页"""
    stats = learning_system.get_progress_stats()
    return render_template('index.html', stats=stats, progress=learning_system.progress)

@app.route('/dashboard')
def dashboard():
    """学习仪表板"""
    stats = learning_system.get_progress_stats()
    recent_notes = dict(list(learning_system.progress['notes'].items())[-5:])  # 最近5条笔记
    return render_template('dashboard.html', stats=stats, notes=recent_notes)

@app.route('/course/<int:day>')
def course_day(day):
    """显示指定天的课程内容"""
    content = learning_system.get_day_content(day)
    is_completed = day in learning_system.progress['completed_days']
    note = learning_system.progress['notes'].get(str(day))
    
    if not content:
        flash(f'第{day}天的课程内容暂未发布', 'warning')
        return redirect(url_for('curriculum'))
    
    return render_template('course_day.html', 
                         day=day, 
                         content=content, 
                         is_completed=is_completed,
                         note=note)

@app.route('/curriculum')
def curriculum():
    """课程大纲页面"""
    current_day = learning_system.progress['current_day']
    completed_days = learning_system.progress['completed_days']
    
    # 生成课程结构
    course_structure = []
    for level in range(3):
        level_info = {
            'name': ['初级', '中级', '高级'][level],
            'start_day': level * 30 + 1,
            'end_day': (level + 1) * 30,
            'weeks': []
        }
        
        for week in range(4):
            week_start = level_info['start_day'] + week * 7
            week_end = min(week_start + 6, level_info['end_day'])
            
            week_info = {
                'number': week + 1,
                'start_day': week_start,
                'end_day': week_end,
                'days': []
            }
            
            for day in range(week_start, week_end + 1):
                day_info = {
                    'number': day,
                    'completed': day in completed_days,
                    'current': day == current_day,
                    'available': day <= current_day
                }
                content = learning_system.get_day_content(day)
                if content:
                    day_info['topic'] = content.get('topic', f'第{day}天')
                else:
                    day_info['topic'] = f'第{day}天'
                
                week_info['days'].append(day_info)
            
            level_info['weeks'].append(week_info)
        
        course_structure.append(level_info)
    
    return render_template('curriculum.html', course_structure=course_structure)

@app.route('/projects')
def projects():
    """项目页面"""
    weekly_projects = learning_system.get_weekly_projects()
    return render_template('projects.html', projects=weekly_projects)

@app.route('/notes')
def notes():
    """笔记页面"""
    all_notes = learning_system.progress['notes']
    return render_template('notes.html', notes=all_notes)

@app.route('/api/complete_day/<int:day>', methods=['POST'])
def api_complete_day(day):
    """API: 标记天完成"""
    success = learning_system.mark_day_complete(day)
    if success:
        return jsonify({'success': True, 'message': f'第{day}天已完成！'})
    else:
        return jsonify({'success': False, 'message': f'第{day}天已经完成过了'})

@app.route('/api/add_note', methods=['POST'])
def api_add_note():
    """API: 添加笔记"""
    data = request.json
    day = data.get('day')
    content = data.get('content', '').strip()
    
    if not content:
        return jsonify({'success': False, 'message': '笔记内容不能为空'})
    
    learning_system.add_note(day, content)
    return jsonify({'success': True, 'message': '笔记已保存！'})

@app.route('/api/update_note', methods=['POST'])
def api_update_note():
    """API: 更新笔记"""
    data = request.json
    day = data.get('day')
    content = data.get('content', '').strip()
    
    if not content:
        return jsonify({'success': False, 'message': '笔记内容不能为空'})
    
    success = learning_system.update_note(day, content)
    if success:
        return jsonify({'success': True, 'message': '笔记已更新！'})
    else:
        return jsonify({'success': False, 'message': '笔记不存在'})

@app.route('/api/delete_note', methods=['POST'])
def api_delete_note():
    """API: 删除笔记"""
    data = request.json
    day = data.get('day')
    
    success = learning_system.delete_note(day)
    if success:
        return jsonify({'success': True, 'message': '笔记已删除！'})
    else:
        return jsonify({'success': False, 'message': '笔记不存在'})

@app.route('/api/progress')
def api_progress():
    """API: 获取进度统计"""
    stats = learning_system.get_progress_stats()
    return jsonify(stats)

@app.route('/settings')
def settings():
    """设置页面"""
    return render_template('settings.html', progress=learning_system.progress)

@app.route('/api/reset_progress', methods=['POST'])
def api_reset_progress():
    """API: 重置学习进度"""
    learning_system.progress = {
        "start_date": datetime.now().strftime("%Y-%m-%d"),
        "current_day": 1,
        "completed_days": [],
        "notes": {},
        "weekly_projects": {}
    }
    learning_system.save_progress()
    return jsonify({'success': True, 'message': '学习进度已重置'})

@app.route('/about')
def about():
    """关于页面"""
    return render_template('about.html')

if __name__ == '__main__':
    # 确保模板和静态文件目录存在
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('static/images', exist_ok=True)
    
    print("🚀 启动Python学习系统Web版本...")
    print("📱 访问地址: http://localhost:8080")
    print("🐍 开始您的Python学习之旅吧！")
    
    app.run(debug=True, host='0.0.0.0', port=8080) 