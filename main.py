# ... 现有导入 ...
import tkinter as tk
from tkinter import messagebox

class SnakeGame:
    def __init__(self, master):
        self.master = master
        # 添加菜单栏
        self.create_menu()
        
        # 默认游戏设置
        self.speed = 100  # 默认速度
        self.window_width = 600
        self.window_height = 400
        
        # ... 现有初始化代码 ...
    
    def create_menu(self):
        menubar = tk.Menu(self.master)
        
        # 设置菜单
        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="游戏速度", command=self.set_speed)
        settings_menu.add_command(label="窗口大小", command=self.set_window_size)
        menubar.add_cascade(label="设置", menu=settings_menu)
        
        # 帮助菜单
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="关于", command=self.show_about)
        menubar.add_cascade(label="帮助", menu=help_menu)
        
        self.master.config(menu=menubar)
    
    def set_speed(self):
        # 速度设置对话框
        speed_window = tk.Toplevel(self.master)
        speed_window.title("设置游戏速度")
        
        tk.Label(speed_window, text="选择游戏速度:").pack()
        
        speeds = [("慢速", 200), ("中速", 100), ("快速", 50)]
        speed_var = tk.IntVar(value=self.speed)
        
        for text, speed in speeds:
            tk.Radiobutton(speed_window, text=text, variable=speed_var, 
                          value=speed).pack(anchor=tk.W)
        
        tk.Button(speed_window, text="确定", 
                 command=lambda: self.apply_speed(speed_var.get(), speed_window)).pack()
    
    def apply_speed(self, speed, window):
        self.speed = speed
        window.destroy()
        # 这里可以添加重新设置游戏速度的逻辑
    
    def set_window_size(self):
        # 窗口大小设置对话框
        size_window = tk.Toplevel(self.master)
        size_window.title("设置窗口大小")
        
        tk.Label(size_window, text="宽度:").pack()
        width_entry = tk.Entry(size_window)
        width_entry.insert(0, self.window_width)
        width_entry.pack()
        
        tk.Label(size_window, text="高度:").pack()
        height_entry = tk.Entry(size_window)
        height_entry.insert(0, self.window_height)
        height_entry.pack()
        
        tk.Button(size_window, text="确定", 
                command=lambda: self.apply_window_size(
                    width_entry.get(), height_entry.get(), size_window)).pack()
    
    def apply_window_size(self, width, height, window):
        try:
            self.window_width = int(width)
            self.window_height = int(height)
            self.master.geometry(f"{self.window_width}x{self.window_height}")
            window.destroy()
            # 这里可以添加重新设置游戏区域的逻辑
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字")
    
    def show_about(self):
        messagebox.showinfo("关于", "贪吃蛇游戏 v1.0")
    
    # ... 现有游戏逻辑代码 ...

# ... 现有主程序代码 ...