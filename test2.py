from tkinter import *
import tkinter.messagebox
import os, json,sys,csv,re
import tkinter
import csv, datain
import matplotlib.pyplot as plt
import matplotlib, subprocess
matplotlib.rcParams['axes.unicode_minus'] = False  # 显示“-”
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文字符
import datain

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.ttk import Combobox
import tkinter.messagebox
from PIL import ImageGrab
import pandas as pd
import json
import data_imiout,turtle
import PIL,webbrowser
from PIL import ImageTk

import tkinter.font as tkFont

image_resoure = "F:/WorkSpace/end_design/resource/"
os.chdir('F:\\WorkSpace/end_design/enddesign/data')#数据目录


w = Tk()
w.geometry('720x480+%d+%d' % (w.winfo_screenwidth() / 2 - 240, w.winfo_screenheight() / 2 - 360))
w.title("你好，Tk")
#w.overrideredirect(True)#窗口无边框，没有任务栏
w.resizable(width=False,height=False)

imggif = 0
colora, colorb, colorc = 15, 0, 0
tempcount, s = 1, ''
class w4_about():
    def __init__(self):a=0
    def about(self):
        def web(e):
            print("sd",e.x,e.y)
            if 205<= e.x <=400 and 280<= e.y <=300:
                print("132213")
                webbrowser.open('https://github.com/my-sword/')  # 打开网页  https是http升级 数据加密

        def on_move(e):
            if 205 <= e.x <= 400 and 280 <= e.y <= 300:
                ca.itemconfigure(ft2,fill="blue")  # 两种刷新方式
            else:
                ca.itemconfigure(ft2, fill="black")

        w4 = Toplevel()
        w4.geometry('400x300+%d+%d' % (w.winfo_screenwidth() / 2 - 240, w.winfo_screenheight() / 2 - 360))
        w4.title("关于")
        w4.resizable(width=False, height=False)#窗口不可改大小
        w4.iconbitmap(image_resoure + "mi64.ico")

        imgw4_0 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "flower/frame1.png"))
        imgw4_1 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "mi1.png"))
        imgw4_2 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "mi2.png"))
        imgw4_3 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "titleabout.png"))
        #imagestyle='flower/'
        imagestyle='house/'
        imggif_1 = ImageTk.PhotoImage(PIL.Image.open(image_resoure +imagestyle+ "frame1.png"))
        imggif_2 = ImageTk.PhotoImage(PIL.Image.open(image_resoure +imagestyle+ "frame2.png"))
        imggif_3 = ImageTk.PhotoImage(PIL.Image.open(image_resoure +imagestyle+ "frame3.png"))
        imggif_4 = ImageTk.PhotoImage(PIL.Image.open(image_resoure +imagestyle+ "frame4.png"))
        imggif_5 = ImageTk.PhotoImage(PIL.Image.open(image_resoure +imagestyle+ "frame5.png"))



        #make in china by 小子斌#动态图：tkinter有一种复杂的方法：先分成多帧数的图片再逐一config
        la0 = Label(w4, image=imggif_1, borderwidth=0, compound='center')  # top_label
        #la0.place(x=0, y=0, width=400, height=300)

        ll0 = Label(w4, text='', borderwidth=0, compound='center')  # top_label
        #ll0.place(x=150, y=0, width=80, height=80)
        ll0 = Label(w4, image=imgw4_2, borderwidth=0, compound='center')  # top_label
        #ll0.place(x=150, y=0, width=80, height=80)

        ca = Canvas(w4, width=400, height=300)
        ca.place(x=0, y=0, width=400, height=300)

        ca.create_image(0,0,anchor=NW,image=imgw4_0)#1

        ft3=ca.create_image(50,130,anchor=NW,image=imgw4_1)#2 mi64
        ca.create_image(50,50,anchor=NW,image=imgw4_3)
        ca.create_text(192,130,anchor=NW,text='by',font=('迷你简少儿',20),fill='pink')
        ca.create_text(155,175,anchor=NW,text='小子斌',font=('汉仪雪峰体简',25),fill='blue')#5
        ca.create_text(2,280,anchor=NW,text='QQ：1367228212',font=('汉仪雪峰体简',9))
        ca.create_text(100,280,anchor=NW,text='  2020年3月9日',font=('黑体',10))
        ft1 = tkFont.Font(family='黑体',size=10, slant=tkFont.ITALIC)
        ft2=ca.create_text(205,280,anchor=NW,text='https://github.com/my-sword/',font=ft1,fill='black')

        #ca.move(2,0,-100)#移动ID为2的事物，使得横坐标加0，纵坐标减3
        #updata非常卡
        def updata():
            global imggif,imgw4_0
            if imggif % 5 == 0:
                imgw4_0 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "flower/frame1.png"))
                ca.create_image(0, 0, anchor=NW, image=imgw4_0)
                ca.create_image(50, 130, anchor=NW, image=imgw4_1)
                ca.create_image(50, 50, anchor=NW, image=imgw4_3)
                ca.create_text(185, 130, anchor=NW, text='by', font=('迷你简少儿', 20), fill='blue')
                ca.create_text(155, 175, anchor=NW, text='小子斌', font=('汉仪雪峰体简', 25), fill='blue')
                ca.create_text(2, 280, anchor=NW, text='QQ：1367228212', font=('汉仪雪峰体简', 9), fill='purple')
                ca.create_text(100, 280, anchor=NW, text='  2020年3月9日', font=('黑体', 10), fill='purple')
                ft1 = tkFont.Font(family='黑体', size=10, slant=tkFont.ITALIC)
                ca.create_text(205, 280, anchor=NW, text='http://github.com/my-sword', font=ft1, fill='purple')
            elif imggif % 5 == 1:
                imgw4_0 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "flower/frame2.png"))
                ca.create_image(0, 0, anchor=NW, image=imgw4_0)
                ca.create_image(50, 130, anchor=NW, image=imgw4_1)
                ca.create_image(50, 50, anchor=NW, image=imgw4_3)
                ca.create_text(185, 130, anchor=NW, text='by', font=('迷你简少儿', 20), fill='blue')
                ca.create_text(155, 175, anchor=NW, text='小子斌', font=('汉仪雪峰体简', 25), fill='blue')
                ca.create_text(2, 280, anchor=NW, text='QQ：1367228212', font=('汉仪雪峰体简', 9), fill='purple')
                ca.create_text(100, 280, anchor=NW, text='  2020年3月9日', font=('黑体', 10), fill='purple')
                ft1 = tkFont.Font(family='黑体', size=10, slant=tkFont.ITALIC)
                ca.create_text(205, 280, anchor=NW, text='http://github.com/my-sword', font=ft1, fill='purple')
            elif imggif % 5 == 2:
                imgw4_0 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "flower/frame3.png"))
                ca.create_image(0, 0, anchor=NW, image=imgw4_0)
                ca.create_image(50, 130, anchor=NW, image=imgw4_1)
                ca.create_image(50, 50, anchor=NW, image=imgw4_3)
                ca.create_text(185, 130, anchor=NW, text='by', font=('迷你简少儿', 20), fill='blue')
                ca.create_text(155, 175, anchor=NW, text='小子斌', font=('汉仪雪峰体简', 25), fill='blue')
                ca.create_text(2, 280, anchor=NW, text='QQ：1367228212', font=('汉仪雪峰体简', 9), fill='purple')
                ca.create_text(100, 280, anchor=NW, text='  2020年3月9日', font=('黑体', 10), fill='purple')
                ft1 = tkFont.Font(family='黑体', size=10, slant=tkFont.ITALIC)
                ca.create_text(205, 280, anchor=NW, text='http://github.com/my-sword', font=ft1, fill='purple')
            elif imggif % 5 == 3:
                imgw4_0 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "flower/frame4.png"))
                ca.create_image(0, 0, anchor=NW, image=imgw4_0)
                ca.create_image(50, 130, anchor=NW, image=imgw4_1)
                ca.create_image(50, 50, anchor=NW, image=imgw4_3)
                ca.create_text(185, 130, anchor=NW, text='by', font=('迷你简少儿', 20), fill='blue')
                ca.create_text(155, 175, anchor=NW, text='小子斌', font=('汉仪雪峰体简', 25), fill='blue')
                ca.create_text(2, 280, anchor=NW, text='QQ：1367228212', font=('汉仪雪峰体简', 9), fill='purple')
                ca.create_text(100, 280, anchor=NW, text='  2020年3月9日', font=('黑体', 10), fill='purple')
                ft1 = tkFont.Font(family='黑体', size=10, slant=tkFont.ITALIC)
                ca.create_text(205, 280, anchor=NW, text='http://github.com/my-sword', font=ft1, fill='purple')
            else:
                imgw4_0 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "flower/frame5.png"))
                ca.create_image(0, 0, anchor=NW, image=imgw4_0)
                ca.create_image(50, 130, anchor=NW, image=imgw4_1)
                ca.create_image(50, 50, anchor=NW, image=imgw4_3)
                ca.create_text(185, 130, anchor=NW, text='by', font=('迷你简少儿', 20), fill='blue')
                ca.create_text(155, 175, anchor=NW, text='小子斌', font=('汉仪雪峰体简', 25), fill='blue')
                ca.create_text(2, 280, anchor=NW, text='QQ：1367228212', font=('汉仪雪峰体简', 9), fill='purple')
                ca.create_text(100, 280, anchor=NW, text='  2020年3月9日', font=('黑体', 10), fill='purple')
                ft1 = tkFont.Font(family='黑体', size=10, slant=tkFont.ITALIC)
                ca.create_text(205, 280, anchor=NW, text='http://github.com/my-sword', font=ft1, fill='purple')
            imggif = imggif + 1
            #print(imggif)
            w4.after(200,updata)
        #updata()
        def imgconfig(event):
            #设置event.xy在图片范围触发事件
            pass
        def a():
            global imgw4_0,image
            image = PIL.Image.open(image_resoure + "flower/frame3.png")
            imgw4_0 = ImageTk.PhotoImage(image)
            ca.create_image(0, 0, anchor=NW, image=imgw4_0)
        def updata2():
            global caimg,imggif
            if imggif % 5 == 0:la0['image']=imggif_1
            elif imggif % 5 == 1:
                la0['image']=imggif_2
            elif imggif % 5 == 2:
                la0['image']=imggif_3
            elif imggif % 5 == 3:
                la0['image']=imggif_4
            else:
                la0['image']=imggif_5
            imggif = imggif + 1
            #print(imggif)
            w4.after(200,updata2)
        def updata3():
            global caimg,imggif
            if imggif % 5 == 0:
                ca.itemconfigure(1,image=imggif_1)
                ca.itemconfigure(1,image=imggif_1)
            elif imggif % 5 == 1:
                ca.itemconfigure(1,image=imggif_2)
                ca.itemconfigure(1,image=imggif_2)
            elif imggif % 5 == 2:
                ca.itemconfigure(1,image=imggif_3)
                ca.itemconfigure(1,image=imggif_3)
            elif imggif % 5 == 3:
                ca.itemconfigure(1,image=imggif_4)
                ca.itemconfigure(1,image=imggif_4)
            else:
                ca.itemconfigure(1,image=imggif_5)
                ca.itemconfigure(1,image=imggif_5)
            imggif = imggif + 1

            w4.after(200,updata3)
        updata3()


        colorful = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'AA', 'BB', 'CC', 'DD', 'EE', 'FF']
        def updatatext():
            global colora, colorb, colorc, tempcount, s
            if tempcount <= 90:  # 16*16*3=768
                s = '#' + colorful[colora] + colorful[colorb] + colorful[colorc]
            else:
                # colora,colorb,colorc = 15,0,0
                tempcount = 1

            if tempcount <= 15:
                colorc = colorc + 1
            elif 15 < tempcount <= 30:
                colora = colora - 1
            elif 30 < tempcount <= 45:
                colorb = colorb + 1
            elif 45 < tempcount <= 60:
                colorc = colorc - 1
            elif 60 < tempcount <= 75:
                colora = colora + 1
            else:
                colorb = colorb - 1
            tempcount = tempcount + 1
            ca.itemconfigure(5, fill=s)


            w4.after(100, updatatext)
        updatatext()
        ca.bind('<1>',web)
        ca.bind('<Motion>',on_move)

        but=Button(w4,command=a)
        #but.place(x=0, y=0, width=30, height=10)
        w4.mainloop()
w4_w4=w4_about()


button1=Button(w,text='打开',width=10,font=('GB2312',18),background='Tan',command=w4_w4.about)   #window2不带括号
button1.place(x=0, y=0, width=150, height=50)
button2=Button(w,text='第二个',width=10,font=('GB2312',18),background='Tan',command=w4_w4.about)   #window2不带括号
button2.place(x=0, y=50, width=150, height=50)
button3=Button(w,text='测试',width=10,font=('GB2312',18),background='Tan',command=w4_w4.about)   #window2不带括号
button3.place(x=0, y=100, width=150, height=50)
lb=Label(w,bg='blue',text='asdsadasdasdsadsadsadasdasdsadas')
lb.place(x=40, y=125, width=640, height=325)

w.mainloop()


