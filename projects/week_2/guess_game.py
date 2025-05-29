#!/usr/bin/env python3
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
        
        print(f"\n🎯 猜数字游戏开始！")
        print(f"我想了一个{min_num}到{max_num}之间的数字")
        print(f"你有{max_attempts}次机会猜中它！")
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"\n第{attempts + 1}次猜测: "))
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
        
        print(f"\n💔 游戏结束！正确答案是{target}")
        self.games_played += 1
        self.total_attempts += attempts
        return False
    
    def show_stats(self):
        """显示游戏统计"""
        print("\n📊 游戏统计:")
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
            print("\n" + "="*30)
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
