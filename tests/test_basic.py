#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基本测试用例
确保系统核心功能正常工作
"""

import unittest
import sys
import os
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

class TestBasicFunctionality(unittest.TestCase):
    """基本功能测试"""
    
    def test_import_modules(self):
        """测试核心模块是否能正常导入"""
        try:
            import web_app
            import detailed_course_content
            import extended_reading_config
            self.assertTrue(True, "所有核心模块导入成功")
        except ImportError as e:
            self.fail(f"模块导入失败: {e}")
    
    def test_flask_app_creation(self):
        """测试Flask应用是否能正常创建"""
        try:
            from web_app import app
            self.assertIsNotNone(app, "Flask应用创建成功")
            self.assertEqual(app.name, 'web_app', "应用名称正确")
        except Exception as e:
            self.fail(f"Flask应用创建失败: {e}")
    
    def test_course_content_structure(self):
        """测试课程内容结构是否正确"""
        try:
            from detailed_course_content import get_detailed_course_content
            content = get_detailed_course_content()
            
            # 检查是否包含第1天的内容
            self.assertIn("1", content, "包含第1天课程内容")
            
            # 检查第1天内容结构
            day1 = content["1"]
            required_fields = ["topic", "concepts", "examples", "exercises"]
            for field in required_fields:
                self.assertIn(field, day1, f"第1天包含{field}字段")
                
        except Exception as e:
            self.fail(f"课程内容结构测试失败: {e}")
    
    def test_extended_reading_config(self):
        """测试拓展阅读配置是否正确"""
        try:
            from extended_reading_config import get_extended_reading_config
            config = get_extended_reading_config()
            
            self.assertIsInstance(config, dict, "拓展阅读配置是字典类型")
            
            # 检查是否包含一些关键天数
            key_days = ["5", "6", "22"]
            for day in key_days:
                if day in config:
                    reading = config[day]
                    self.assertIn("materials", reading, f"第{day}天包含学习材料")
                    self.assertIn("tips", reading, f"第{day}天包含学习建议")
                    
        except Exception as e:
            self.fail(f"拓展阅读配置测试失败: {e}")

class TestWebAppRoutes(unittest.TestCase):
    """Web应用路由测试"""
    
    def setUp(self):
        """设置测试环境"""
        from web_app import app
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_route(self):
        """测试首页路由"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200, "首页能正常访问")
    
    def test_course_route(self):
        """测试课程页面路由"""
        response = self.app.get('/course/1')
        self.assertEqual(response.status_code, 200, "第1天课程页面能正常访问")
    
    def test_api_progress_route(self):
        """测试进度API路由"""
        response = self.app.get('/api/progress')
        self.assertEqual(response.status_code, 200, "进度API能正常访问")
        
        # 检查返回的JSON数据
        data = response.get_json()
        self.assertIsInstance(data, dict, "API返回JSON数据")
        self.assertIn('total_days', data, "包含总天数信息")

if __name__ == '__main__':
    # 创建测试套件
    suite = unittest.TestSuite()
    
    # 添加测试用例
    suite.addTest(unittest.makeSuite(TestBasicFunctionality))
    suite.addTest(unittest.makeSuite(TestWebAppRoutes))
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 输出测试结果
    if result.wasSuccessful():
        print("\n🎉 所有测试通过！")
        sys.exit(0)
    else:
        print(f"\n❌ 测试失败: {len(result.failures)} 个失败, {len(result.errors)} 个错误")
        sys.exit(1) 