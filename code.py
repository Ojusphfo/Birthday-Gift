```python
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import Style
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import tkinter.messagebox
import turtle
import random
from time import sleep
import ctypes
import os

# 清空日志文件
f = open( 'Moon.log', 'w' )
f.close()

# 登录界面
# style = Style(theme = 'classic')
root = Tk()
root.title('XXX专用登录界面')
root.geometry('400x300')

# 美化界面
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/75)

## 主题：['vista', 'classic', 'cyborg', 'journal', 'darkly', 'flatly', 'clam', 'alt', 'solar', 'minty', 'litera', 'united', 'xpnative', 'pulse', 'cosmo', 'lumen', 'yeti', 'superhero', 'winnative', 'sandstone', 'default']

## 登录窗口
### 标签（用户名，密码）
user_name = Label(root, text = 'Username:', font = ('Comic Sans MS',  14))
user_password = Label(root, text='Password', font = ('Comic Sans MS',  14))
user_name.place(relx=0.2, rely = 0.2, anchor = CENTER)
user_password.place(relx=0.2,  rely = 0.5, anchor = CENTER)
### 文本框（用户名，密码）
name = Entry(root,  textvariable = StringVar())
password = Entry(root,  textvariable = StringVar(), show='*')
name.place(relx = 0.65, rely = 0.2, anchor = CENTER)
password.place(relx = 0.65, rely = 0.5, anchor = CENTER)

# 关闭登录界面
def close_login():
    global root
    root.destroy()

# 樱花树下看樱花
def flowerwindow():
    def tree(branchLen, t):
        if branchLen > 3:
            if 8 <= branchLen <= 12:
                if random.randint(0, 2) == 0:
                    t.color('snow')
                else:
                    t.color('lightcoral')
                t.pensize(branchLen / 3)
            elif branchLen < 8:
                if random.randint(0, 1) == 0:
                    t.color('snow')
                else:
                    t.color('lightcoral')
                t.pensize(branchLen / 2)
            else:
                t.color('sienna')
                t.pensize(branchLen / 10)
            t.forward(branchLen)
            a = 1.5 * random.random()
            t.right(20 * a)
            b = 1.5 * random.random()
            tree(branchLen - 10 * b, t)
            t.left(40 * a)
            tree(branchLen-10 * b, t)
            t.right(20 * a)
            t.up()
            t.backward(branchLen)
            t.down()
    def petal(m, t):  # 树下花瓣
        for i in range(m):
            a = 200 - 400 * random.random()
            b = 30 - 40 * random.random()
            t.up()
            t.forward(b)
            t.left(90)
            t.forward(a)
            t.down()
            t.color("lightcoral")
            t.circle(1)
            t.up()
            t.backward(a)
            t.right(90)
            t.backward(b)
    def main():   
        t = turtle.Turtle()
        w = turtle.Screen()
        t.hideturtle() # 隐藏画笔
        t.getscreen().tracer(5, 0)
        w.screensize(bg='wheat') # wheat小麦
        t.left(90)
        t.up()
        t.backward(150)
        t.down()
        t.color('sienna')
        tree(62, t)
        petal(255, t)
        w.exitonclick()
    main()

# 生日蛋糕
## 建立蛋糕图形窗体
def cakewindow():
    window_2 = Tk()
    window_2.title("Birthday Cake")

    singwindow()
    window_2.wm_attributes('-topmost',1)
    fig = plt.figure(figsize = (6, 6))
    plt.style.use('ggplot')
    ax = plt.subplot()
    plt.grid(color = 'w')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
## 建立xy的值
    xy_1 = [(2, 0), (2, 2.5), (8, 2.5), (8, 0)]
    xy_2 = [(2.75, 2.5), (2.75, 5), (7.25, 5), (7.25, 2.5)]
    xy_3 = [(3.5, 5), (3.5, 7), (6.5, 7), (6.5, 5)]
    x1 = np.arange(2, 8.2, 0.4)
    y1 = x1 * 0 + 0.1
    x2 = np.arange(2.75, 7.5, 0.3)
    y2 = x2 * 0 + 2.6
    x3 = np.arange(3.5, 6.8, 0.3)
    y3 = x3 * 0 + 5.1
    x4 = np.arange(3.5, 6.8, 0.3)
    y4 = x4 * 0 + 7
    polygon_1 = Polygon(xy_1, color = '#ff33cc')
    polygon_2 = Polygon(xy_2, color = '#ff66cc')
    polygon_3 = Polygon(xy_3, color = '#ff6699')
    polygon_1.set_zorder(0)
    polygon_2.set_zorder(0)
    polygon_3.set_zorder(0)
    ax.add_patch(polygon_1)
    ax.add_patch(polygon_2)
    ax.add_patch(polygon_3)
## 建立文本
    ax.text(2.85, 0.75, 'Birthday!', fontfamily = 'Comic Sans MS', size = 35)
    ax.text(3.5, 3.25, 'Happy', fontfamily = 'Comic Sans MS', size = 35)
    ax.text(4.25, 5.5, 'XXX', fontfamily = 'Comic Sans MS', size = 35)
    ax.text(4.3, 7.25, '17', fontfamily = 'Comic Sans MS', size = 35)
    ax.text(5.1, 8.1, '$\omega$', fontfamily = 'Comic Sans MS', size = 20, rotation = -15, color = 'orange')
## 建立文本
    ax.scatter(x1, y1, color = '#006699')
    ax.scatter(x2, y2, color = '#0099cc')
    ax.scatter(x3, y3, color = '#3399cc')
    ax.scatter(x4, y4, color = '#f8bbd0')
## 贴图进canvas
    canvas = FigureCanvasTkAgg(fig, master = window_2)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tkinter.TOP, fill = tkinter.BOTH, expand = 1)
    toolbar = NavigationToolbar2Tk(canvas,  window_2)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tkinter.TOP, fill = tkinter.BOTH, expand = 1)
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,  canvas,  toolbar)
        canvas.mpl_connect("key_press_event", on_key_press)
    def _quit():
        window_2.destroy()
    button = tkinter.Button(master = window_2, text = "Quit", font = ('Comic Sans MS',  12),  command = _quit)
    button.pack(side = tkinter.BOTTOM)

# 许愿窗口
def wishwindow():
    ## 许完愿后的弹窗
    def run():
        tkinter.messagebox.showinfo(title = '许完愿啦~', message = '祝小仙女愿望成真~')
        tkinter.messagebox.showinfo(title = '月光女神说：', message = '请把 Moon.log 文件发给xxx')
    def Write():
        with open("Moon.log", "w") as f:
            if(CheckVar1.get() == 1):
                f.write("1\n")
            if(CheckVar2.get() == 1): 
                f.write("2\n")
            if(CheckVar3.get() == 1): 
                f.write("3\n")
            if(CheckVar4.get() == 1): 
                f.write("4\n")
            if(CheckVar5.get() == 1): 
                f.write("5\n")
            if(CheckVar6.get() == 1):
                f.write("6\n")
            if(CheckVar7.get() == 1):
                f.write("7\n")
            f.write(qt1.get())
    def close_wish():
        cake.destroy()
    cake = Tk()
    cake.geometry('400x400')
    cake.title('许愿啦~')
    wishlb1 = Label(cake, text = '请选择你想实现的（小）愿望', font = ('Comic Sans MS', 14))
    wishlb1.pack()
    wishlb2 = Label(cake, text = '也许可以实现哦~', font = ('Comic Sans MS', 14))
    wishlb2.pack()
    ## 愿望按钮*8
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6 = IntVar()
    CheckVar7 = IntVar()
    CheckVar8 = IntVar()
    ch1 = Checkbutton(cake, text = '变得更漂亮？', variable = CheckVar1, onvalue = 1, offvalue = 0)
    ch2 = Checkbutton(cake, text = '想要出去玩？', variable = CheckVar2, onvalue = 1, offvalue = 0)
    ch3 = Checkbutton(cake, text = '看女装照片？', variable = CheckVar3, onvalue = 1, offvalue = 0)
    ch4 = Checkbutton(cake, text = '听xxx高歌一曲？', variable = CheckVar4, onvalue = 1, offvalue = 0)
    ch5 = Checkbutton(cake, text = '想要变得更瘦？', variable = CheckVar5, onvalue = 1, offvalue = 0)
    ch6 = Checkbutton(cake, text = '想要成为一个撸猫怪？', variable = CheckVar6, onvalue = 1, offvalue = 0)
    ch7 = Checkbutton(cake, text = '都想要？', variable = CheckVar7, onvalue = 1, offvalue = 0)
    ch8 = Checkbutton(cake, text = '还有', variable = CheckVar8, onvalue = 1, offvalue = 0)
    ch1.pack()
    ch2.pack()
    ch3.pack()
    ch4.pack()
    ch5.pack()
    ch6.pack()
    ch7.pack()
    ch8.pack()
    qt1 = Entry(cake,  textvariable = StringVar())
    qt1.place(relx = 0.68, rely = 0.58, relwidth = 0.25, anchor = CENTER)
    btn1 = tkinter.Button(cake, text = 'OK', font = ('Comic Sans MS', 14), command = lambda:[run(), Write()])
    btn1.place(relx = 0.25, rely = 0.85, relwidth = 0.25, relheight = 0.08)
    btn2 = tkinter.Button(cake, text = 'Quit', font = ('Comic Sans MS', 14), command = close_wish)
    btn2.place(relx = 0.55, rely = 0.85, relwidth = 0.25, relheight = 0.08)
    
# 播放音乐
def singwindow():
    file = r'.\music.mp3'
    os.system(file)

# 弹出猫猫
def catwindow():
    cat = Tk()
    canvas = Canvas(cat, width = 1000, height = 500)
    canvas.pack()
    img1 = PhotoImage(file = "cat.ppm")
    img2 = PhotoImage(file = "aa.ppm")
    canvas.create_image(500, 500, anchor = CENTER, image = img1)
    canvas.create_image(50, 175, anchor = CENTER, image = img2)    
    mainloop()
    
# 主界面
def main_window():
    main = Tk()
    main.title('生日快乐')
    main.geometry('500x500')
    lb1 = Label(main, text = 'Hi! 生日快乐! ', font = ('Comic Sans MS',  14))
    lb1.place(relx = 0.1, rely = 0.08, relwidth = 0.8, relheight = 0.1)
    lb2 = Label(main, text = '请按顺序点击: ', font = ('Comic Sans MS',  14))
    lb2.place(relx = 0.1, rely = 0.15, relwidth = 0.3, relheight = 0.1)
    btn1 = Button(main, text = '樱花漫天飞舞', command = flowerwindow)
    btn1.place(relx = 0.1, rely = 0.25, relwidth = 0.35, relheight = 0.08)
    btn2 = Button(main, text = '生日快乐', command = cakewindow)
    btn2.place(relx = 0.1, rely = 0.35, relwidth = 0.35, relheight = 0.08)
    btn3 = Button(main, text = '喵~', command = catwindow)
    btn3.place(relx = 0.1, rely = 0.45, relwidth = 0.35, relheight = 0.08)
    btn4 = Button(main, text = '点我许愿', command = wishwindow)
    btn4.place(relx = 0.1, rely = 0.55, relwidth = 0.35, relheight = 0.08)

# 建立login关联函数
def birthday():
    ## 用户名及密码设置
    name_in = name.get()
    password_in = password.get()
    right_username = '1' ### 用户名
    right_password = '1' ### 密码
    if name_in == right_username and password_in == right_password :
        tkinter.messagebox.showinfo(title = 'Sucess!', message = '登陆成功!') ### 登录成功
        main_window()
        name.delete(0, 'end')
        password.delete(0, 'end')
    else:
        tkinter.messagebox.showerror(title = 'Error', message = 'xxx连登录都不会...') ### 登录失败
        name.delete(0, 'end')
        password.delete(0,  'end')

# 建立login按钮
# btn1 = Button(root, text='Login', font = ('Comic Sans MS',  12), command = lambda:[birthday(), close_login()])
btn1 = Button(root, text='Login', command = lambda:[birthday(), close_login()])
btn1.place(relx = 0.5, rely = 0.8, anchor = CENTER)

root.mainloop()
