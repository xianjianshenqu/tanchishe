import pygame
import sys
import time
import random

# 初始化pygame
pygame.init()

# 默认设置
DEFAULT_SPEED = 10
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600

class SnakeGame:
    def __init__(self):
        # 游戏状态
        self.game_active = False
        self.game_paused = False
        
        # 加载设置
        self.load_settings()
        
        # 初始化屏幕
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('贪吃蛇游戏')
        
        # 颜色定义
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        
        # 蛇和食物
        self.snake_pos = [[100, 50], [90, 50], [80, 50]]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.food_pos = [random.randrange(1, (self.width//10)) * 10, 
                         random.randrange(1, (self.height//10)) * 10]
        self.food_spawn = True
        
        # 方向
        self.direction = 'RIGHT'
        self.change_to = self.direction
        
        # 分数
        self.score = 0
        
        # 时钟
        self.clock = pygame.time.Clock()
        
        # 字体
        self.font = pygame.font.SysFont('arial', 20)
        
    def load_settings(self):
        # 从文件加载设置或使用默认值
        try:
            with open('settings.txt', 'r') as f:
                settings = f.read().splitlines()
                self.speed = int(settings[0])
                self.width = int(settings[1])
                self.height = int(settings[2])
        except:
            self.speed = DEFAULT_SPEED
            self.width = DEFAULT_WIDTH
            self.height = DEFAULT_HEIGHT
    
    def save_settings(self):
        # 保存设置到文件
        with open('settings.txt', 'w') as f:
            f.write(f"{self.speed}\n{self.width}\n{self.height}")
    
    def show_menu(self):
        menu_active = True
        
        while menu_active:
            self.screen.fill(self.BLACK)
            
            # 菜单选项
            title = self.font.render('贪吃蛇游戏 - 菜单', True, self.WHITE)
            start = self.font.render('1. 开始游戏', True, self.WHITE)
            settings = self.font.render('2. 设置', True, self.WHITE)
            about = self.font.render('3. 关于', True, self.WHITE)
            exit = self.font.render('4. 退出', True, self.WHITE)
            
            # 显示菜单
            self.screen.blit(title, (self.width//2 - title.get_width()//2, 50))
            self.screen.blit(start, (self.width//2 - start.get_width()//2, 150))
            self.screen.blit(settings, (self.width//2 - settings.get_width()//2, 200))
            self.screen.blit(about, (self.width//2 - about.get_width()//2, 250))
            self.screen.blit(exit, (self.width//2 - exit.get_width()//2, 300))
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        menu_active = False
                        self.game_active = True
                        self.game_loop()
                    elif event.key == pygame.K_2:
                        self.show_settings()
                    elif event.key == pygame.K_3:
                        self.show_about()
                    elif event.key == pygame.K_4:
                        pygame.quit()
                        sys.exit()
    
    def show_settings(self):
        settings_active = True
        
        while settings_active:
            self.screen.fill(self.BLACK)
            
            # 设置选项
            title = self.font.render('设置', True, self.WHITE)
            speed = self.font.render(f'1. 速度: {self.speed} (方向键左右调整)', True, self.WHITE)
            width = self.font.render(f'2. 宽度: {self.width} (方向键上下调整)', True, self.WHITE)
            height = self.font.render(f'3. 高度: {self.height} (方向键上下调整)', True, self.WHITE)
            back = self.font.render('4. 返回菜单', True, self.WHITE)
            
            # 显示设置
            self.screen.blit(title, (self.width//2 - title.get_width()//2, 50))
            self.screen.blit(speed, (self.width//2 - speed.get_width()//2, 150))
            self.screen.blit(width, (self.width//2 - width.get_width()//2, 200))
            self.screen.blit(height, (self.width//2 - height.get_width()//2, 250))
            self.screen.blit(back, (self.width//2 - back.get_width()//2, 300))
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.speed > 5:
                        self.speed -= 1
                    elif event.key == pygame.K_RIGHT and self.speed < 30:
                        self.speed += 1
                    elif event.key == pygame.K_UP and self.width < 1200:
                        self.width += 50
                    elif event.key == pygame.K_DOWN and self.width > 400:
                        self.width -= 50
                    elif event.key == pygame.K_UP and self.height < 900:
                        self.height += 50
                    elif event.key == pygame.K_DOWN and self.height > 300:
                        self.height -= 50
                    elif event.key == pygame.K_4:
                        self.save_settings()
                        settings_active = False
                    elif event.key == pygame.K_ESCAPE:
                        self.save_settings()
                        settings_active = False
    
    def show_about(self):
        about_active = True
        
        while about_active:
            self.screen.fill(self.BLACK)
            
            # 关于信息
            title = self.font.render('关于', True, self.WHITE)
            version = self.font.render('贪吃蛇游戏 v1.0', True, self.WHITE)
            author = self.font.render('作者: 你的名字', True, self.WHITE)
            copyright = self.font.render('版权所有 © 2023', True, self.WHITE)
            back = self.font.render('按ESC返回菜单', True, self.WHITE)
            
            # 显示关于
            self.screen.blit(title, (self.width//2 - title.get_width()//2, 50))
            self.screen.blit(version, (self.width//2 - version.get_width()//2, 150))
            self.screen.blit(author, (self.width//2 - author.get_width()//2, 200))
            self.screen.blit(copyright, (self.width//2 - copyright.get_width()//2, 250))
            self.screen.blit(back, (self.width//2 - back.get_width()//2, 300))
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        about_active = False
    
    def game_over(self):
        game_over_font = pygame.font.SysFont('arial', 50)
        game_over_surface = game_over_font.render('游戏结束!', True, self.RED)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self.width/2, self.height/4)
        
        score_font = pygame.font.SysFont('arial', 20)
        score_surface = score_font.render(f'得分: {self.score}', True, self.WHITE)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (self.width/2, self.height/2)
        
        self.screen.blit(game_over_surface, game_over_rect)
        self.screen.blit(score_surface, score_rect)
        pygame.display.flip()
        
        time.sleep(2)
        self.game_active = False
        self.show_menu()
    
    def show_score(self):
        score_surface = self.font.render(f'得分: {self.score}', True, self.WHITE)
        score_rect = score_surface.get_rect()
        score_rect.topleft = (10, 10)
        self.screen.blit(score_surface, score_rect)
    
    def game_loop(self):
        while self.game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # 键盘控制
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != 'DOWN':
                        self.change_to = 'UP'
                    elif event.key == pygame.K_DOWN and self.direction != 'UP':
                        self.change_to = 'DOWN'
                    elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                        self.change_to = 'LEFT'
                    elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                        self.change_to = 'RIGHT'
                    elif event.key == pygame.K_SPACE:  # 暂停
                        self.game_paused = not self.game_paused
                    elif event.key == pygame.K_ESCAPE:  # 返回菜单
                        self.game_active = False
            
            # 如果游戏暂停，跳过更新
            if self.game_paused:
                self.screen.fill(self.BLACK)
                pause_text = self.font.render('游戏暂停 - 按空格键继续', True, self.WHITE)
                self.screen.blit(pause_text, (self.width//2 - pause_text.get_width()//2, 
                                             self.height//2 - pause_text.get_height()//2))
                self.show_score()
                pygame.display.update()
                continue
            
            # 更新方向
            if self.change_to == 'UP' and self.direction != 'DOWN':
                self.direction = 'UP'
            elif self.change_to == 'DOWN' and self.direction != 'UP':
                self.direction = 'DOWN'
            elif self.change_to == 'LEFT' and self.direction != 'RIGHT':
                self.direction = 'LEFT'
            elif self.change_to == 'RIGHT' and self.direction != 'LEFT':
                self.direction = 'RIGHT'
            
            # 移动蛇
            if self.direction == 'UP':
                self.snake_pos[0][1] -= 10
            elif self.direction == 'DOWN':
                self.snake_pos[0][1] += 10
            elif self.direction == 'LEFT':
                self.snake_pos[0][0] -= 10
            elif self.direction == 'RIGHT':
                self.snake_pos[0][0] += 10
            
            # 蛇身体增长机制
            self.snake_body.insert(0, list(self.snake_pos[0]))
            if self.snake_pos[0] == self.food_pos:
                self.score += 1
                self.food_spawn = False
            else:
                self.snake_body.pop()
            
            # 食物生成
            if not self.food_spawn:
                self.food_pos = [random.randrange(1, (self.width//10)) * 10, 
                                random.randrange(1, (self.height//10)) * 10]
                self.food_spawn = True
            
            # 绘制
            self.screen.fill(self.BLACK)
            
            # 绘制蛇
            for pos in self.snake_body:
                pygame.draw.rect(self.screen, self.GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
            
            # 绘制食物
            pygame.draw.rect(self.screen, self.RED, pygame.Rect(self.food_pos[0], self.food_pos[1], 10, 10))
            
            # 显示分数
            self.show_score()
            
            # 碰撞检测
            # 撞墙
            if (self.snake_pos[0][0] < 0 or self.snake_pos[0][0] > self.width-10 or
                self.snake_pos[0][1] < 0 or self.snake_pos[0][1] > self.height-10):
                self.game_over()
            
            # 撞自己
            for block in self.snake_body[1:]:
                if self.snake_pos[0] == block:
                    self.game_over()
            
            pygame.display.update()
            self.clock.tick(self.speed)

# 主函数
def main():
    game = SnakeGame()
    game.show_menu()

if __name__ == "__main__":
    main()