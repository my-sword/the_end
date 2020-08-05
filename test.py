from tkinter import *
import tkinter.messagebox
import os,json,subprocess,win32api
import PIL
from PIL import ImageTk
import time,random,winsound
#画面会置底
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
import numpy as np
from matplotlib.pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

filestate=os.getcwd()+'/data/state.json'
filetest=os.getcwd()+'/data/test.json'
fileerror=os.getcwd()+"/data/"
image_resoure = os.getcwd()+"/resource/"

#登陆次数和拖动坐标
cishu,sheight,salpha =5,240,1
def admin_sign():

    # 事件响应
    def _ll0(event):
        w1.geometry('+%d+%d' % (event.x_root - x, event.y_root - y))  # 实现鼠标拖动
    def win_mouse(event):  # 拖动需要固定坐标
        global x, y
        x = event.x
        y = event.y
    def _ll2_close(event):#admin关闭按钮
        if var1.get()==1:
            with open(filetest, 'r') as json_file:
                data = json.load(json_file)
            if (in1.get() == data["账号"] and in2.get() == data["密码"]) or (in1.get() == data["user"] and in2.get() == data["pass"]):
                pass
            else:
                print(in1.get(), ' ', in2.get(), '！=', data["账号"], ' ', data["密码"], ' ', data["user"], '+', data["pass"])
                data["记住密码"] = "0"
                with open(filetest, 'w') as json_file:
                    json.dump(data, json_file, ensure_ascii=False)
        os._exit(0)  # w1.quit() X关闭窗口
    #def _ll5_2_lose(event):but2()

    # 图片载入区
    def _img1_1(event):ll1.config(image=img1_1)
    def _img1_2(event):ll1.config(image=img1_2)
    def _img2_1(event):ll2.config(image=img2_1)
    def _img2_2(event):ll2.config(image=img2_2)
    def _img3_1(event):ll3.config(image=img3_1);ll5_3.config(image='')
    def _img3_2(event):ll3.config(image=img3_2);ll5_3.config(image=img5_3_1)#<FocusIn>
    def _img4_1(event):ll4.config(image=img4_1);ll5_3.config(image='')
    def _img4_2(event):ll4.config(image=img4_2);ll5_3.config(image=img5_3_2)#<FocusIn>
    def _img5_1(event):ll5_2.config(image=img5_1)
    def _img5_2(event):ll5_2.config(image=img5_2)


    # 记住密码和自动登录状态的文本写入
    def check_state():
        with open(filetest, 'r') as json_file:
            data = json.load(json_file)
        # 记住密码和自动登录状态
        data["记住密码"]="1" if var1.get()==1 else "0"
        data["自动登录"]="1" if var2.get()==1 else "0"
        # if in1.get() != '' and in2.get() != '':
        #     data["账号"] = in1.get()
        #     data["密码"] = in2.get()
        #
        with open(filetest, 'w') as json_file:
            json.dump(data, json_file, ensure_ascii=False)

    #登录操作
    def but(event):#Enter热键绑定
        global cishu
        check_state()
        with open(filetest, 'r') as json_file:
            data = json.load(json_file)

        if in1.get() == data["账号"] and in2.get() == data["密码"]:
            with open(filetest, 'r') as json_file:
                data = json.load(json_file)
            data["id"] = "0"
            with open(filetest, 'w') as json_file:
                json.dump(data, json_file, ensure_ascii=False)
            w.update()
            w.deiconify()

            # 动画上拉效果
            def heightreduce():
                global sheight
                sheight = sheight - 5
                w1.geometry('340x' + str(sheight))  # 340x240
                w1.after(10, heightreduce)
                # print(w.winfo_width())
                if w1.winfo_height() < 10:
                    w1.destroy()

            heightreduce()
            #w1.withdraw()

        elif in1.get() == data["user"] and in2.get() == data["pass"]:
            with open(filetest, 'r') as json_file:
                data = json.load(json_file)
            data["id"] = "1"
            with open(filetest, 'w') as json_file:
                json.dump(data, json_file, ensure_ascii=False)
            w.update()
            w.deiconify()

            # 动画淡出效果
            def alphareduce():
                global salpha
                salpha = salpha - 0.05
                w1.attributes("-alpha", salpha)  # 窗口透明度60 %
                w1.after(100, alphareduce)
                # print(salpha)
                if salpha < 0.1:
                    w1.destroy()
            alphareduce()
        else:
            cishu=cishu-1
            tkinter.messagebox.showerror('错误','密码错误请重试！您今天还有'+str(cishu)+'次机会！')
    def but2(event):#‘登录’按钮
        global cishu
        check_state()
        with open(filetest, 'r') as json_file:
            data = json.load(json_file)

        if in1.get() == data["账号"] and in2.get() == data["密码"]:
            with open(filetest, 'r') as json_file:
                data = json.load(json_file)
            data["id"] = "0"
            with open(filetest, 'w') as json_file:
                json.dump(data, json_file, ensure_ascii=False)
            w.update()
            w.deiconify()

            # 动画上拉效果
            def heightreduce():
                global sheight
                sheight = sheight - 5
                w1.geometry('340x' + str(sheight))  # 340x240
                w1.after(10, heightreduce)
                # print(w.winfo_width())
                if w1.winfo_height() < 10:
                    w1.destroy()

            heightreduce()
            # w1.withdraw()

        elif in1.get() == data["user"] and in2.get() == data["pass"]:
            with open(filetest, 'r') as json_file:
                data = json.load(json_file)
            data["id"] = "1"
            with open(filetest, 'w') as json_file:
                json.dump(data, json_file, ensure_ascii=False)
            w.update()
            w.deiconify()

            # 动画淡出效果
            def alphareduce():
                global salpha
                salpha = salpha - 0.05
                w1.attributes("-alpha", salpha)  # 窗口透明度60 %
                w1.after(100, alphareduce)
                # print(salpha)
                if salpha < 0.1:
                    w1.destroy()
            alphareduce()
        else:
            cishu = cishu - 1
            tkinter.messagebox.showerror('错误', '密码错误请重试！您今天还有' + str(cishu) + '次机会！')

    #选择框状态
    def write():#记住密码状态  调用new()也预先声明write函数
        if in1.get() != '' and in2.get() != '':
            pass
        else:
            if var1.get()==1:
                tkinter.messagebox.showerror('错误', '密码账号不能为空！')
    def write1():pass

    #选择框功能  出现BUG
    def remember():#打开py执行 记住当前密码之读取密码
        with open(filetest, 'r') as json_file:
            data = json.load(json_file)
        if data["记住密码"] == "1" and data['id']=="0":

            in1.insert(0, data["账号"])
            in2.insert(0, data["密码"])
            ch1.select()
        if data["记住密码"] == "1" and data['id'] == "1":
            with open(filetest, 'r') as json_file:
                data = json.load(json_file)
            in1.insert(0, data["user"])
            in2.insert(0, data["pass"])
            ch1.select()
    def remember1():#自动登录 销毁登录窗口 在主窗口处注销==0
        with open(filetest, 'r') as json_file:
            data = json.load(json_file)
        if data["自动登录"] == "1" :#and in1.get()== data["账号"] and in2.get() ==data["密码"]
            ch2.select()
            w.update()
            w.deiconify()
            w1.destroy()
        # else:
        #     in1.delete(0,END)
        #     in2.delete(0,END)

        # if data["自动登录"] == "1" :#and in1.get()== data["user"] and in2.get() ==data["pass"]
        #     ch2.select()
        #     w.update()
        #     w.deiconify()
        #     w1.destroy()

    #初始化登录窗口
    w.withdraw()
    w1=Toplevel()  #新建子窗口
    w1.geometry('340x240+%d+%d' % (w1.winfo_screenwidth() / 2 - 120, w1.winfo_screenheight() / 2 - 160))
    w1.overrideredirect(True)  # 窗口无边框，没有任务栏
    #图片载入区

    img0_1 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "top_label.png"))
    img1_1 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "一-1.png"))
    img1_2 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "一-2.png"))
    img2_1 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "X-1.png"))
    img2_2 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "X-2.png"))
    img3_1 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "nameword.png"))
    img3_2 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "nameword-2.png"))
    img4_1 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "password.png"))
    img4_2 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "password-2.png"))
    img5_1 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "sign_1.png"))
    img5_2 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "sign_2.png"))
    img5_3_1 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "bottom_left.png"))
    img5_3_2 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "bottom_right.png"))

    #标签图片处理区
    ll0 = Label(w1, image=img0_1, borderwidth=0, compound='center')#top_label
    ll0.place(x=0,y=0,width=340,height=96)
    ll1 = Label(w1, image=img1_1, borderwidth=0)#缩小
    ll1.place(relx=0.84, rely=-0.01)
    ll2 = Label(w1, image=img2_1, borderwidth=0)#关闭
    ll2.place(relx=0.92, rely=-0.01)
    #背景图标签
    ll5_3=Label(w1,bg='White',borderwidth=0)#bottom白色背景
    ll5_3.place(x=0,y=96,width=340,height=144)
    ll5_2=Label(w1,image=img5_1, borderwidth=0)#登录按钮
    ll5_2.place(x=100,y=200,width=141,height=31)
    ll3=Label(w1,image=img3_1,borderwidth=0)#账号图标
    ll3.place(x=70, y=120)
    ll4=Label(w1,image=img4_1,borderwidth=0)#密码图标
    ll4.place(x=70, y=150)
    # 输入框
    in1_var = StringVar(w1, value='')#初始化默认值
    in2_var = StringVar(w1, value='')
    in1 = Entry(w1,foreground='orange',borderwidth=1,textvariable=in1_var)  # ??外加提示账号密码+单击消失
    in2 = Entry(w1,foreground='orange', show='★',borderwidth=1,textvariable=in2_var)  # 外加渐变色、渐变字
    in1.place(x=100, y=120, width=150, height=30)
    in2.place(x=100, y=150, width=150, height=30)

    #热键绑定区
    ll0.bind('<B1-Motion>', _ll0)
    w1.bind('<1>', win_mouse)
    w1.bind("<Return>", but)
    ll1.bind('<Enter>', _img1_2)
    ll1.bind('<Leave>', _img1_1)
    ll2.bind('<Enter>', _img2_2)
    ll2.bind('<Leave>', _img2_1)
    ll2.bind('<1>', _ll2_close)#关闭按钮
    ll5_2.bind('<Enter>', _img5_2)
    ll5_2.bind('<Leave>', _img5_1)
    ll5_2.bind('<1>', but2)#登录按钮
    in1.bind('<FocusIn>', _img3_2)
    in1.bind('<FocusOut>', _img3_1)
    in2.bind('<FocusIn>', _img4_2)
    in2.bind('<FocusOut>', _img4_1)





    #记住密码自动登录
    var1 = IntVar()
    var2 = IntVar()
    ch1 = Checkbutton(w1, text='记住密码', variable=var1, onvalue=1, offvalue=0,command=write,fg='#00CD66')  # 因为有两个值所以变量不能同一个
    ch2 = Checkbutton(w1, text='自动登录', variable=var2, onvalue=1, offvalue=0,command=write1,fg='#00CD66')
    ch1.place(x=100,y=180,width=71,height=16)
    ch2.place(x=180,y=180,width=71,height=16)



    #账号文件是否存在
    if os.path.exists(filetest):
        remember()
        remember1()
    else:
        #with open("work.txt",'w') as f1,open("work1.txt",'w') as f2:
        with open(filetest, 'w') as json_file:
            json.dump({"记住密码":"","自动登录":"","id":"","账号":"admin","密码":"123","user":"user","pass":"000"}, json_file, ensure_ascii=False)

    #登录窗口句柄状态处理
    #w1.configure(bg='White')#重新打开会失败
    #w1.wm_attributes('-topmost', 2)  # 窗口总是前置（0为假，12345为层级）
    #w1.attributes("-topmost", True)
    # w1.attributes("-alpha", 0.4)#窗口透明度60 %
    # win32gui.WindowFromPoint(win32api.GetCursorPos())#获取窗口句柄
    w1.mainloop()