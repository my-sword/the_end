#基于python的数据动态可视化管理平台--数据接收与监控的界面设计
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
matplotlib.rcParams['axes.unicode_minus']=False#显示“-”
plt.rcParams['font.sans-serif'] = ['SimHei']   #正常显示中文字符
import sys
filestate=os.getcwd()+'/data/state.json'
filetest=os.getcwd()+'/data/test.json'
fileerror=os.getcwd()+"/data/"
image_resoure = os.getcwd()+"/resource/"

import datain


#登陆次数和拖动坐标
cishu,sheight,salpha =5,240,1
x,y,z,z1,z2,z3,z4,z5=0,0,0,0,0,0,0,0
a2='blue'
#os.chdir(os.getcwd()+'/data')#数据目录
def admin_sign():
    #初始化(防止admin登进去,注销后再登user，出现admin的可操作页面的bug)
    lbmb1.place_forget()
    lbmb2.place_forget()
    lbmb3.place_forget()
    lbmb4.place_forget()
    lb_time.place_forget()

    lbbut1.place_forget()
    lbbut2.place_forget()
    lbbut3.place_forget()
    lbbut4.place_forget()
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
        sys.exit(0)
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

    #选择框功能  出现BUG已解决
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
def lb_gettime():#系统渐变标签算法
    global a2
    s = 'ABCDEF0123456789'
    a2 = '#'
    a1 = []
    for j in range(0, 6):
        a1.append(random.choice(s))
        a2 = a2 + a1[j]
    timestr=time.strftime('%Y-%m-%d %H:%M:%S')
    lb_time.configure(text=timestr,fg=a2)
    w.after(1000, lb_gettime)

#菜单窗口类
import csv
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.ttk import Combobox
import tkinter.messagebox
from PIL import ImageGrab
import pandas as pd
import re,data_imiout,turtle,webbrowser
max_limitone,min_limitone=12,2#数据一
max_limittwo,min_limittwo=30,6#数据二
class w2_datahandle():
    # 初始化登录窗口
    def __init__(self):
        a=0
    #设置预警上下限
    def w2_warning(self):

        def dataconfirm():
            global max_limitone, min_limitone, max_limittwo, min_limittwo
            #if w2in1.get()!='' and w2in2.get()!='':
            reentry='^0$|^[1-9]\d*$'
            if  re.match(reentry,w2in1.get())!=None and re.match(reentry,w2in2.get())!=None and re.match(reentry,w2in3.get())!=None and re.match(reentry,w2in4.get())!=None:
                if int(w2in1.get()) > int(w2in2.get()) and int(w2in3.get()) > int(w2in4.get()):
                    #(只匹配整数) ^0非0开头 $一行结尾 |或 ^[1-9]开头1-9其中评一个个 \d*任意整数
                    max_limitone, min_limitone = int(w2in1.get()), int(w2in2.get())  # 数据一
                    max_limittwo, min_limittwo = int(w2in3.get()), int(w2in4.get())  # 数据二
                    print(max_limitone+min_limitone+max_limittwo+min_limittwo)
                else:
                    tkinter.messagebox.showerror('错误', '上限必须大于下限')
            else:
                tkinter.messagebox.showerror('错误','非整数类型')
        def datareset():
            w2in1.delete(0,END)
            w2in2.delete(0,END)
            w2in3.delete(0,END)
            w2in4.delete(0,END)
            w2in1.insert(0, '12')
            w2in2.insert(0, '2')
            w2in3.insert(0, '30')
            w2in4.insert(0, '6')

        w2 = Toplevel()  # 新建子窗口
        w2.geometry("400x150+%d+%d" % (w2.winfo_screenwidth() / 2 - 150, w2.winfo_screenheight() / 2 - 140))
        w2.title('设置预警值上下限')
        w2.iconbitmap(image_resoure + "mi64.ico")
        # 输入框
        w2in1_var = StringVar(w2, value='')#初始化默认值
        w2in2_var = StringVar(w2, value='')
        w2in3_var = StringVar(w2, value='')
        w2in4_var = StringVar(w2, value='')
        w2lb1_1=Label(w2,text='数据一预警值上限',borderwidth=0)
        w2lb1_1.place(x=0, y=0, width=150, height=50)
        w2lb1_2=Label(w2,text='数据一预警值下限',borderwidth=0)
        w2lb1_2.place(x=0, y=50, width=150, height=50)
        w2lb1_3=Label(w2,text='数据二预警值上限',borderwidth=0)
        w2lb1_3.place(x=200, y=0, width=150, height=50)
        w2lb1_4=Label(w2,text='数据二预警值下限',borderwidth=0)
        w2lb1_4.place(x=200, y=50, width=150, height=50)

        w2in1 = Entry(w2,foreground='red',borderwidth=1,textvariable=w2in1_var)
        w2in1.place(x=150, y=0, width=50, height=50)
        w2in2 = Entry(w2,foreground='red',borderwidth=1,textvariable=w2in2_var)
        w2in2.place(x=150, y=50, width=50, height=50)
        w2in3 = Entry(w2, foreground='red', borderwidth=1, textvariable=w2in3_var)
        w2in3.place(x=350, y=0, width=50, height=50)
        w2in4 = Entry(w2, foreground='red', borderwidth=1, textvariable=w2in4_var)
        w2in4.place(x=350, y=50, width=50, height=50)
        # 初始化
        # imo_min, imo_max = 0.02, 0.12  # O2 datain_rand()
        # imp_min, imp_max = 0.06, 0.30  # PH3
        w2in1.insert(0, '12')
        w2in2.insert(0, '2')
        w2in3.insert(0, '30')
        w2in4.insert(0, '6')


        w2but1 = Button(w2, text='确认', width=10, font=('GB2312', 18), background='Tan', command=dataconfirm)
        w2but1.place(x=50, y=100, width=150, height=50)
        w2but2 = Button(w2, text='重置', width=10, font=('GB2312', 18), background='Tan', command=datareset)
        w2but2.place(x=200,y=100, width=150, height=50)
        w2.mainloop()
    #查看数据信息
    def w2_info(self):#可用dsv读取对应数值
        global max_limitone, min_limitone,max_limittwo, min_limittwo,data_one
        w2 = Toplevel()  # 新建子窗口
        w2.title("数据信息")
        w2.geometry("480x360+%d+%d" % (w2.winfo_screenwidth() / 2 - 150, w2.winfo_screenheight() / 2 - 140))

        w2.iconbitmap(image_resoure + "mi64.ico")

        string='时间段：' + datain.dataset3[0]+'~'+datain.dataset3[data_one]+'\n'+\
               '当前数据一最大值：' + str(max(datain.dataset1[0:data_one]))+'\n'+ \
               '当前数据一最小值：' + str(min(datain.dataset1[0:data_one]))+'\n'+ \
               '当前数据二最大值：' + str(max(datain.dataset2[0:data_one]))+'\n'+ \
               '当前数据二最小值：' + str(min(datain.dataset2[0:data_one]))+'\n'+ \
               '数据一安全范围：' + str(min_limitone) + '~' + str(max_limitone)+'\n'+ \
               '数据二安全范围：' + str(min_limittwo) + '~' + str(max_limittwo)+'\n'+ \
               '时间刷新频率：1秒'+'\n'+'绘图模块：' + 'Matplotlib'

        w2lb2_1 = Label(w2, text=string, borderwidth=0,fg='purple',font=('迷你简少儿',15))
        w2lb2_1.place(x=0, y=0, width=480, height=360)
        def w2info_flush():
            global max_limitone, min_limitone, max_limittwo, min_limittwo
            string = '时间段：' + datain.dataset3[0] + '~' + datain.dataset3[data_one] + '\n' + \
                     '当前数据一最大值：' + str(max(datain.dataset1[0:data_one])) + '\n' + \
                     '当前数据一最小值：' + str(min(datain.dataset1[0:data_one])) + '\n' + \
                     '当前数据二最大值：' + str(max(datain.dataset2[0:data_one])) + '\n' + \
                     '当前数据二最小值：' + str(min(datain.dataset2[0:data_one])) + '\n' + \
                     '数据一安全范围：' + str(min_limitone) + '~' + str(max_limitone) + '\n' + \
                     '数据二安全范围：' + str(min_limittwo) + '~' + str(max_limittwo) + '\n' + \
                     '时间刷新频率：1秒' + '\n' + '绘图模块：' + 'Matplotlib'
            w2lb2_1.config(text=string)
        w2.after(1000,w2info_flush)
        w2.mainloop()
    #导出指定范围数据
    def w2_output(self):
        w2 = Toplevel()  # 新建子窗口
        w2.geometry("270x100+%d+%d" % (
        w2.winfo_screenwidth() / 2 - w2.winfo_width() / 3, w2.winfo_screenheight() / 2 - w2.winfo_height() / 3))
        w2.title('导出数据')
        w2.iconbitmap(image_resoure + "mi64.ico")

        def w2_outputdata():#写入数据
            w2fname=asksaveasfilename(defaultextension='.txt',filetypes=[('保存类型', '.txt')])
            if com.current()==0:
                if w2in5.get()!='' or w2in6.get()!='':
                    with open(w2fname,'a')as f:
                        f.write('数据一'+'\t'+'时间')
                        for i in range(int(w2in6.get())-int(w2in5.get())):
                            f.write(str(datain.dataset1[int(w2in5.get())+i])+'\t'+datain.dataset3[int(w2in5.get())+i]+'\n')
            else:
                if w2in5.get() != '' or w2in6.get() != '':
                    with open(w2fname, 'a')as f:
                        f.write('数据二' + '\t' + '时间')
                        for i in range(int(w2in6.get()) - int(w2in5.get())):
                            f.write(str(datain.dataset2[int(w2in5.get())+i])+'\t'+datain.dataset3[int(w2in5.get())+i]+'\n')
        w2in5_var = StringVar(w2, value='')#初始化默认值
        w2in6_var = StringVar(w2, value='')


        w2lb3_1 = Label(w2, text='导出范围数据：',fg='purple',font=('汉仪雪峰体简',10))
        w2lb3_1.place(x=0, y=0, width=150, height=50)
        w2lb3_2 = Label(w2, text='~~~',fg='blue')
        w2lb3_2.place(x=213, y=20, width=10, height=10)
        w2in5 = Entry(w2, foreground='red', borderwidth=1, textvariable=w2in5_var)
        w2in6 = Entry(w2, foreground='red', borderwidth=1, textvariable=w2in6_var)
        w2in5.place(x=180, y=10, width=30, height=30)
        w2in6.place(x=230, y=10, width=30, height=30)
        comvar = StringVar(value='数据一')
        com = Combobox(w2,textvariable=comvar, values=['数据一', '数据二'])  # 注意values
        com.place(x=120, y=15, width=60, height=20)
        w2but3 = Button(w2, text='导出', width=10, font=('汉仪雪峰体简', 18),fg='orange', background='pink',command=w2_outputdata)
        w2but3.place(x=50, y=50, width=150, height=50)
        w2.mainloop()
    #打开超标数据
    def w2_error1data(self):
        os.popen("notepad.exe "+fileerror+"error1.txt")
    def w2_error2data(self):
        os.popen("notepad.exe "+fileerror+"error2.txt")
    #保存图片
    def w2_savepicture1(self):
        filename = 'savedata1.png'
        w2savesrc1 = asksaveasfilename(defaultextension='.png',filetypes=[('保存类型', '.png')])
        try:#canvas.place(x=40, y=125, width=640, height=325)
            img = ImageGrab.grab()
            im=img.crop((w.winfo_x()+40,w.winfo_y()+125,w.winfo_x()+40+640,w.winfo_y()+125+325))#图片裁剪品目左上角(x,y) (距右边界,底边界)
            print(str(w.winfo_x())+','+str(w.winfo_y()))
            print(str(w.winfo_screenwidth()-(w.winfo_x()+40+640))+','+str(w.winfo_screenheight()-(w.winfo_y()+125+325)))
            print(str(w.winfo_x()+40) + ',' + str(w.winfo_y()+125))
            im.save(w2savesrc1)
            im.close()
            """
            Image.crop(left, up, right, below)
            left：与左边界的距离
            up：与上边界的距离
            right：还是与左边界的距离
            below：还是与右边界的距离"""
        except:
            pass
    def w2_savepicture2(self):
        w2savesrc1 = asksaveasfilename(defaultextension='.png', filetypes=[('保存类型', '.png')])
        try:  # canvas.place(x=40, y=125, width=640, height=325)
            img = ImageGrab.grab()
            im = img.crop((w.winfo_x() + 40, w.winfo_y() + 125, w.winfo_x() + 40 + 640,
                           w.winfo_y() + 125 + 325))  # 图片裁剪品目左上角(x,y) (距左边界,上边界)
            print(str(w.winfo_x()) + ',' + str(w.winfo_y()))
            print(str(w.winfo_screenwidth() - (w.winfo_x() + 40 + 640)) + ',' + str(
                w.winfo_screenheight() - (w.winfo_y() + 125 + 325)))
            print(str(w.winfo_x() + 40) + ',' + str(w.winfo_y() + 125))
            im.save(w2savesrc1)
            im.close()
        except:
            pass

    #打开原数据表目录
    def w2_opencatalog(self):
        cwd=os.getcwd()
        os.popen("start explorer "+cwd)
    #打开原数据表文件
    def w2_opendatafile(self):
        os.popen("notepad.exe F:/WorkSpace/0test/imidata_rand.txt")

    #设置当前数据更新频率
    def w2_flashdata(self):
        tkinter.messagebox.showerror('很抱歉', '该功能没有必要开发！')
class w3_datahandle():
    def __init__(self):
        a = 0
    #实时数据处理 难
    class w3_datarealtime():
        def __init__(self):
            self.filestate = os.getcwd()+'/data/state.json'

        iturtle, screenstate = 0, 1

        def w3_turtle1(self):
            """
            公式：输出范围=实际值*振幅-平均值*振幅   振幅=(画布-50)÷极值差 输出范围=（实际值-平均值）*[(画布-50)÷极值差]
            例如：o2 18.5~23.5  ph3 3.0~4
            o2：平均值21 极值差5  ph3：平均值3.5 极值差1
            (18.5~23.5)*[(400-50)÷5]-21*[(400-50)÷5]= ±175
            (3.0~4.0)*[(400-50)÷1]-3.5*[(400-50)÷1] = ±175
            """
            iturtle = 0
            w3 = Tk()  # 新建子窗口
            w3.geometry("800x450+%d+%d" % (w3.winfo_screenwidth() / 2 - 400, w3.winfo_screenheight() / 2 - 250))
            w3.title('Turtle数据一处理')
            w3.iconbitmap(image_resoure + "mi64.ico")

            # img_turtle = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "turtle.gif"))
            screenstate = 1

            def drawp():
                global iturtle, screenstate
                theScreen = turtle.TurtleScreen(canva)
                t = turtle.RawTurtle(theScreen)
                # turtle.bgpic(img_turtle)#很遗憾失败  r''不会转义，直接输出\n

                # 画笔及速度
                t.pencolor('red')  # 画笔颜色
                t.pensize(2)  # 画笔像素

                # 初始化
                t.speed(0)  # 1~10 0最快
                t.penup()  # 提笔
                t.goto(-400, 0)
                t.pendown()  # 下笔
                t.speed(1)
                screenstate = 1  # 解决name 'screenstate' is not defined

                for iturtle in range(0, 200):
                    min_t, max_t = min(datain.dataset1[iturtle:iturtle + 10]), max(
                        datain.dataset1[iturtle:iturtle + 10])  # [0:1]===[0]
                    # mean_t=np.mean(np.array(datain.dataset1[iturtle:iturtle+10]))
                    # mean_t.tolist()
                    # print(mean_t)
                    s = 0
                    for i in datain.dataset1[iturtle:iturtle + 10]:
                        s = s + i
                    mean_t = s / 10
                    max_min = (400 - 100) / (max_t - min_t)

                    # print(min_t,' ',max_t,' ',mean_t)
                    if iturtle < 10:
                        t.pencolor('orange')
                        t.goto(-400 + (1 + iturtle) * 80, int((datain.dataset1[iturtle] - mean_t) * max_min))
                        t.pencolor('blue')
                        t.write(str(datain.dataset1[iturtle]), move=False, font=('汉仪雪峰体简', 12))
                    if iturtle >= 10:
                        t.clear()
                        t.speed(0)
                        t.penup()
                        t.goto(-400, 0 + int((datain.dataset1[iturtle - 10] - mean_t) * max_min))
                        t.pendown()
                        t.speed(0)
                        # temp=datain.dataset1[iturtle-10:iturtle]
                        # print(temp)
                        for i in range(1, 11):
                            if i < 9:
                                t.pencolor('orange')
                                t.goto(-400 + i * 80, int((datain.dataset1[iturtle - 10 + i] - mean_t) * max_min))
                                t.pencolor('blue')
                                t.write(str(datain.dataset1[iturtle - 10 + i]), move=False, font=('汉仪雪峰体简', 12))
                            else:
                                t.speed(1)
                                t.pencolor('orange')
                                t.goto(-400 + i * 80, int((datain.dataset1[iturtle - 10 + i] - mean_t) * max_min))
                                t.pencolor('blue')
                                t.write(str(datain.dataset1[iturtle - 10 + i]), move=False, font=('汉仪雪峰体简', 12))
                            # print(int((datain.dataset1[iturtle-10+i]-mean_t)*max_min),end=' ')
                        # print()
                    lb.config(text='数据名称：' + datain.dataname1 + ' 数据值：' + str(datain.dataset1[iturtle]) + ' 时间:' +
                                   datain.dataset3[iturtle])
                    # print(datain.dataname1 + '时间:' + datain.dataset3[iturtle])
                    if screenstate == 0:
                        break

                theScreen.mainloop()

            canva = Canvas(w3, width=800, height=400, bg='orange')
            canva.pack()
            lb = Label(w3, text='数据名称：' + datain.dataname1 + '时间:', width=800, height=50, font=('汉仪雪峰体简', 12),
                       fg='green')
            lb.pack()

            def stopcanvas(event):  # 关闭窗口时产生还在绘画的错误，作用是关闭窗口让动画停止，关闭不出错
                global screenstate
                screenstate = 0

            canva.bind("<B1-Motion>", stopcanvas)  # 左键拖动
            try:
                drawp()
            except:
                pass

            w3.mainloop()
        # w3_turtle1()
        def w3_turtle2(self):
            iturtle = 0
            w3 = Tk()  # 新建子窗口
            w3.geometry("800x450+%d+%d" % (w3.winfo_screenwidth() / 2 - 400, w3.winfo_screenheight() / 2 - 250))
            w3.title('Turtle数据二处理')
            w3.iconbitmap(image_resoure + "mi64.ico")

            # img_turtle = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "turtle.gif"))
            def drawp():
                global iturtle, screenstate
                theScreen = turtle.TurtleScreen(canva)
                t = turtle.RawTurtle(theScreen)
                # turtle.bgpic(img_turtle)#很遗憾失败  r''不会转义，直接输出\n

                # 画笔及速度
                t.pencolor('red')  # 画笔颜色
                t.pensize(2)  # 画笔像素

                # 初始化
                t.speed(0)  # 1~10 0最快
                t.penup()  # 提笔
                t.goto(-400, 0)
                t.pendown()  # 下笔
                t.speed(1)
                for iturtle in range(0, 200):
                    min_t, max_t = min(datain.dataset1[iturtle:iturtle + 10]), max(
                        datain.dataset2[iturtle:iturtle + 10])  # [0:1]===[0]
                    s = 0
                    for i in datain.dataset2[iturtle:iturtle + 10]:
                        s = s + i
                    mean_t = s / 10
                    max_min = (400 - 100) / (max_t - min_t)
                    # print(min_t,' ',max_t,' ',mean_t,'jfhj')

                    if iturtle < 10:
                        t.pencolor('orange')
                        t.goto(-400 + (1 + iturtle) * 80,
                               int((datain.dataset2[iturtle] - mean_t) * max_min))  # 10是振幅 200是y轴偏移
                        t.pencolor('blue')
                        t.write(str(datain.dataset2[iturtle]), move=False, font=('汉仪雪峰体简', 12))
                        # print(datain.dataset2[iturtle],',',datain.dataset2[iturtle]*10-200)
                    if iturtle >= 10:
                        t.clear()
                        t.speed(0)
                        t.penup()
                        t.goto(-400, 0 + int((datain.dataset2[iturtle - 10] - mean_t) * max_min))
                        t.pendown()
                        t.speed(0)
                        # temp=datain.dataset2[iturtle-10:iturtle]
                        # print(temp)
                        for i in range(1, 11):
                            if i < 9:
                                t.pencolor('orange')
                                t.goto(-400 + i * 80, int((datain.dataset2[iturtle - 10 + i] - mean_t) * max_min))
                                t.pencolor('blue')
                                t.write(str(datain.dataset2[iturtle - 10 + i]), move=False, font=('汉仪雪峰体简', 12))
                            else:
                                t.speed(1)
                                t.pencolor('orange')
                                t.goto(-400 + i * 80, int((datain.dataset2[iturtle - 10 + i] - mean_t) * max_min))
                                t.pencolor('blue')
                                t.write(str(datain.dataset2[iturtle - 10 + i]), move=False, font=('汉仪雪峰体简', 12))
                            # print(int((datain.dataset2[iturtle-10+i]-mean_t)*max_min),end=' ')
                        # print()
                    lb.config(text='数据名称：' + datain.dataname2 + ' 数据值：' + str(datain.dataset2[iturtle]) + ' 时间:' +
                                   datain.dataset3[iturtle])
                    if screenstate == 0:
                        break
                theScreen.mainloop()

            canva = Canvas(w3, width=800, height=400)
            canva.pack()
            lb = Label(w3, text='数据名称：' + datain.dataname2 + '时间:', width=800, height=50, font=('汉仪雪峰体简', 12),
                       fg='green')
            lb.pack()

            def stopcanvas(event):  # 关闭窗口时产生还在绘画的错误，作用是关闭窗口让动画停止，关闭不出错
                global screenstate
                screenstate = 0

            canva.bind("<B1-Motion>", stopcanvas)
            try:
                drawp()
            except:
                pass

            w3.mainloop()
        # w3_turtle2()

        dataset1 = []  # O2数组(float)
        dataset2 = []  # ph3数组(float)
        dataset3 = []  # 日期时间数组
        dataset4 = []  # 具体时间数组 #由于显示位置不足，需具体时间数组
        dataset5 = []  # 具体日期数组
        dataname1, dataname2, dataname3 = "", "", ""

        # @staticmethod#静态方法无需self
        def dataname(self, filename):
            global filestate, dataname1, dataname2, dataname3
            with open(filename, 'r') as f:
                a = f.readline()
                temp1 = a.strip('\n')
                dataname1, dataname2, dataname3 = temp1.split('\t')
            # print(dataname1, dataname2, dataname3)

            with open(self.filestate, 'r') as file_state:
                f_state = json.load(file_state)

            f_state["数据一名称"] = dataname1
            f_state["数据二名称"] = dataname2
            with open(self.filestate, 'w') as file_state:
                json.dump(f_state, file_state, ensure_ascii=False)

        def datain_dealtime(self):
            global dataset1, dataset2, dataset3, dataset4, dataset5
            # 重置数据
            dataset1 = []  # O2数组(float)
            dataset2 = []  # ph3数组(float)
            dataset3 = []  # 日期时间数组
            dataset4 = []  # 具体时间数组 #由于显示位置不足，需具体时间数组
            dataset5 = []  # 具体日期数组
            filename = 'F:/WorkSpace/0test/turtle_datadeal.txt'

            def loadDatadet(infile):
                f = open(infile, 'r')
                f.readline()  # 去除第一行标题
                sourceInLine = f.readlines()  # 读取所有行的数据
                # dataset1 = []  # O2数组
                for line in sourceInLine:
                    temp1 = line.strip('\n')  # 删除括号内指定字符串头部和尾部字符 split('%\t',1) 1代表%\t分割一次
                    tempz1, tempz2, tempz3 = temp1.split(
                        '\t')  # O2和后面部分 f.write(str(a)  + '\t' + str(b) + '\t' + arrtime[i] )
                    # dataset22, dataset33 = temp1.split('\t')[1].split('\t')#split('\t')[1]取第一个分隔符后的第二组数str(b) + '\t' + arrtime[i]
                    tempz5, tempz4 = tempz3.split()
                    dataset1.append(float(tempz1))  # O2数组 不转数字会出现乱码，y轴排序会出现问题
                    dataset2.append(float(tempz2))  # ph3数组
                    dataset3.append(tempz3)  # 日期时间数组
                    dataset4.append(tempz4)  # 具体时间数组
                    dataset5.append(tempz5)  # 具体日期数组

                    # print(tempz1,' ', tempz2,' ',tempz3,' ',tempz4,' ',tempz5)

            loadDatadet(filename)
            self.dataname(filename)  # 在类里面相互调用

        # datain_dealtime()

        def w3_datadealtime(self):
            self.datain_dealtime()
            iturtle = 0
            w3 = Tk()
            w3.geometry("800x450+%d+%d" % (w3.winfo_screenwidth() / 2 - 400, w3.winfo_screenheight() / 2 - 250))
            w3.title('实时数据更新')
            w3.iconbitmap(image_resoure + "mi64.ico")

            def stopcanvas(event):  # 关闭窗口时产生还在绘画的错误，作用是关闭窗口让动画停止，关闭不出错
                global screenstate
                screenstate = 0

            # w3.protocol("WM_DELETE_WINDOW", closewindow)

            # img_turtle = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "turtle.gif"))

            def drawp():
                global iturtle, dataset1, dataset2, dataset3, screenstate
                theScreen = turtle.TurtleScreen(canva)
                t = turtle.RawTurtle(theScreen)
                # turtle.bgpic(img_turtle)#很遗憾失败  r''不会转义，直接输出\n

                # 画笔及速度
                t.pencolor('red')  # 画笔颜色
                t.pensize(2)  # 画笔像素

                # 初始化
                t.speed(0)  # 1~10 0最快
                t.penup()  # 提笔
                t.goto(-400, 0)
                t.pendown()  # 下笔
                t.speed(1)
                screenstate = 1

                for iturtle in range(0, 200):  # 200次数不是关键
                    if iturtle >= 10:
                        data_imiout.datadealtime()
                        self.datain_dealtime()
                        # print(dataset1,' ', dataset2,' ',dataset3,' ',dataset4,' ',dataset5)
                    min_t, max_t = min(dataset1[0:10]), max(dataset1[0:10])  # [0:1]===[0]
                    s = 0
                    for i in dataset1[0:10]:
                        s = s + i
                    mean_t = s / 10
                    max_min = (400 - 150) / (max_t - min_t)

                    print(min_t, ' ', max_t, ' ', mean_t)
                    if iturtle < 10:
                        t.pencolor('orange')
                        t.goto(-400 + (1 + iturtle) * 80, int((dataset1[iturtle] - mean_t) * max_min))
                        t.pencolor('blue')
                        t.write(str(dataset1[iturtle]), move=False, font=('汉仪雪峰体简', 12))
                        lb.config(
                            text='数据名称：' + dataname1 + ' 数据值：' + str(dataset1[iturtle]) + ' 时间:' + dataset3[iturtle])
                    if iturtle >= 10:  # 已经刷新
                        t.clear()
                        t.speed(0)
                        t.penup()
                        t.goto(-400, 0 + int((dataset1[0] - mean_t) * max_min))
                        t.pendown()
                        t.speed(0)
                        # temp=dataset1[iturtle-10:iturtle]
                        # print(temp)
                        for i in range(1, 11):
                            if i < 9:
                                t.pencolor('orange')
                                t.goto(-400 + i * 80, int((dataset1[i] - mean_t) * max_min))
                                t.pencolor('blue')
                                t.write(str(dataset1[i]), move=False, font=('汉仪雪峰体简', 12))
                            else:
                                t.speed(1)
                                t.pencolor('orange')
                                t.goto(-400 + i * 80, int((dataset1[i] - mean_t) * max_min))
                                t.pencolor('blue')
                                t.write(str(dataset1[i]), move=False, font=('汉仪雪峰体简', 12))
                            # print(int((dataset1[iturtle-10+i]-mean_t)*max_min),end=' ')
                        lb.config(text='数据名称：' + dataname1 + ' 数据值：' + str(dataset1[9]) + ' 时间:' + dataset3[9])
                        # print()
                    if screenstate == 0:
                        break

                    # print(datain.dataname1 + '时间:' + datain.dataset3[0])
                if screenstate == 1:
                    theScreen.mainloop()

            canva = Canvas(w3, width=800, height=400, bg='orange')
            canva.pack()
            lb = Label(w3, text='数据名称：' + dataname1 + '时间:', width=800, height=50, font=('汉仪雪峰体简', 12), fg='green')
            lb.pack()
            canva.bind("<B1-Motion>", stopcanvas)  # 左键拖动
            try:
                drawp()
            except:
                pass

            w3.mainloop()
        # w3_datadealtime()

    #改成流氓表白软件
    def w3_paint(self):
        pass
    #图片处理（改图吧）
    def w3_imagedeal(self):
        pass

    #格式转化
    class w3_formatchange():
        #类变量得外部引用
        def __init__(self):
            a = 0#内变量实例调用
        def w3_txttocsv(self):
            w3_open = askopenfilename(defaultextension='.txt', filetypes=[('打开类型', '.txt')])
            w3_save = asksaveasfilename(defaultextension='.csv', filetypes=[('保存类型', '.csv')])
            try:
                csvFile = open(w3_save, 'w', newline='', encoding='utf-8')
                writer = csv.writer(csvFile)
                csvRow = []
                # 编码说明
                """
                ASC II码全称是“美国信息交换标准代码”，包含常用的英文字母、数字及一些特殊字符和控制符等共计127个字符
                UFT8是一种国际化的编码方式，包含了世界上大部分的语种文字，也兼容ASCII码
                GB2312包含了常用的中文字符，同时也兼容ASCII码
                GBK兼容GB2312编码，但比GB2312包含了更多的汉字
                """
                with open(w3_open, 'r', encoding='GB2312') as f:
                    # f.readline()
                    for line in f:
                        line = line.strip('\n')
                        csvline = line.split('\t')
                        writer.writerow(csvline)
                csvFile.close()
            except:
                pass
        def w3_csvtotxt(self):
            w3_open = askopenfilename(defaultextension='.csv', filetypes=[('打开类型', '.csv')])
            w3_save = asksaveasfilename(defaultextension='.txt', filetypes=[('保存类型', '.txt')])
            try:
                data = pd.read_csv(w3_open, encoding='utf-8', header=None)#header=None使得数据包含第一行
                with open(w3_save, 'a+', encoding='utf-8') as f:
                    for line in data.values:
                        #print(line)
                        f.write(str(line[0]) + '\t' + str(line[1]) + '\t' + str(line[2]) + '\n')

            except:
                pass
        def w3_txttoexcel(self):
            w3_open = askopenfilename(defaultextension='.txt', filetypes=[('打开类型', '.txt')])
            w3_save = asksaveasfilename(defaultextension='.xls', filetypes=[('保存类型', '.xls')])
            try:
                pdtxt = pd.read_csv(w3_open, sep='\t',header=None)#pd.read_csv可用于txt只是sep不同
                df = pd.DataFrame(pdtxt)#形成二维整体不用for循环逐步输入
                writer = pd.ExcelWriter(w3_save)
                #print(pdtxt)
                df.to_excel(writer, 'Sheet1', index=False, header=None)
                writer.save()#没有这个保存失败
            except:
                pass
        def w3_exceltotxt(self):
            w3_open = askopenfilename(defaultextension='.xls', filetypes=[('打开类型', '.xls')])
            w3_save = asksaveasfilename(defaultextension='.txt', filetypes=[('保存类型', '.txt')])
            try:
                with open(w3_save, 'w', encoding='utf-8') as f:
                    df=pd.read_excel(w3_open, header=None, index=False)
                    df.to_csv(f, sep='\t', index=False,header=None)
            except:
                pass
        def w3_csvtoexcel(self):
            w3_open = askopenfilename(defaultextension='.csv', filetypes=[('打开类型', '.csv')])
            w3_save = asksaveasfilename(defaultextension='.xls', filetypes=[('保存类型', '.xls')])
            try:
                pdtxt = pd.read_csv(w3_open, sep=',', header=None)  # pd.read_csv可用于txt只是sep不同
                df = pd.DataFrame(pdtxt)  # 形成二维整体不用for循环逐步输入
                writer = pd.ExcelWriter(w3_save)
                # print(pdtxt)
                df.to_excel(writer, 'Sheet1', index=False, header=None)
                writer.save()  # 没有这个保存失败
            except:
                pass
        def w3_exceltocsv(self):
            w3_open = askopenfilename(defaultextension='.xls', filetypes=[('打开类型', '.xls')])
            w3_save = asksaveasfilename(defaultextension='.csv', filetypes=[('保存类型', '.csv')])
            try:
                with open(w3_save, 'w', encoding='utf-8') as f:
                    df = pd.read_excel(w3_open, header=None, index=False)
                    df.to_csv(f, sep=',', index=False, header=None)
            except:
                pass
    #自由截图+屏幕截图
    def w3_savefreedom(self):
        os.popen("SnippingTool")
    def w3_savescreen(self):  # 利用热键截取屏幕
        w2savesrc1 = asksaveasfilename(defaultextension='.png', filetypes=[('保存类型', '.png')])
        try:
            im = ImageGrab.grab()
            im.save(w2savesrc1)
            im.close()
        except:
            pass

    def s(self):
        win32api.WinExec("python " + os.getcwd() + "/data1.0.py", 1)

import tkinter.font as tkFont
imggif = 0
colora, colorb, colorc,tempcount, s = 15, 0, 0,1, ''
class w4_about():
    def __init__(self):a=0
    def about(self):

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

        ca.create_image(50,130,anchor=NW,image=imgw4_1)#2
        ca.create_image(50,50,anchor=NW,image=imgw4_3)
        ca.create_text(192,130,anchor=NW,text='by',font=('迷你简少儿',20),fill='pink')
        ca.create_text(155,175,anchor=NW,text='小子斌',font=('汉仪雪峰体简',25),fill='blue')#5
        ca.create_text(2,280,anchor=NW,text='QQ：1367228212',font=('汉仪雪峰体简',9),fill='purple')
        ca.create_text(100,280,anchor=NW,text='  2020年3月9日',font=('黑体',10),fill='purple')
        ft1 = tkFont.Font(family='黑体',size=10, slant=tkFont.ITALIC)
        ft2=ca.create_text(205,280,anchor=NW,text='https://github.com/my-sword/',font=ft1,fill='purple')


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

        ca.bind('<1>', web)
        ca.bind('<Motion>', on_move)


        but=Button(w4,command=a)
        #but.place(x=0, y=0, width=30, height=10)
        w4.mainloop()
    def exitwin(self):#菜单退出
        # 结束循环状态
        with open(filestate, 'r') as file_state:
            f_state = json.load(file_state)
        f_state["循环状态"] = "0"
        with open(filestate, 'w') as file_state:
            json.dump(f_state, file_state, ensure_ascii=False)
        os._exit(0)
    def revisepass1(self):
        def diff():
            if in1.get()==in2.get() and in1.get()!='':
                with open(filetest, 'r') as json_file:
                    data = json.load(json_file)
                data["密码"] = in1.get()
                with open(filetest, 'w') as json_file:
                    json.dump(data, json_file, ensure_ascii=False)
                w4.destroy()
            else:
                tkinter.messagebox.showerror('错误', '密码账号不能为空或密码不一致！')
        w4 = Toplevel()
        w4.geometry('200x150+%d+%d' % (w.winfo_screenwidth() / 2 - 240, w.winfo_screenheight() / 2 - 360))
        w4.title("修改密码")
        w4.resizable(width=False, height=False)  # 窗口不可改大小
        w4.iconbitmap(image_resoure + "mi64.ico")

        lb1=Label(w4,text='修改密码:', borderwidth=0,font=('汉仪雪峰体简', 12))
        lb1.place(x=0, y=0, width=100, height=50)
        lb2 = Label(w4, text='确认密码:', borderwidth=0,font=('汉仪雪峰体简', 12))
        lb2.place(x=0, y=50, width=100, height=50)
        in1_var = StringVar(w4, value='')  # 初始化默认值
        in2_var = StringVar(w4, value='')
        in1 = Entry(w4, foreground='orange', show='★', borderwidth=1, textvariable=in1_var)
        in2 = Entry(w4, foreground='orange', show='★', borderwidth=1, textvariable=in2_var)
        in1.place(x=100, y=0, width=100, height=50)
        in2.place(x=100, y=50, width=100, height=50)
        bt1=Button(w4,text='确定',command=diff)
        bt1.place(x=25, y=100, width=100, height=50)
        w4.mainloop()
    def revisepass2(self):
        def diff():
            if in1.get()==in2.get() and in1.get()!='':
                with open(filetest, 'r') as json_file:
                    data = json.load(json_file)
                data["pass"] = in1.get()
                with open(filetest, 'w') as json_file:
                    json.dump(data, json_file, ensure_ascii=False)
                w4.destroy()
            else:
                tkinter.messagebox.showerror('错误', '密码账号不能为空或密码不一致！')
        w4 = Toplevel()
        w4.geometry('200x150+%d+%d' % (w.winfo_screenwidth() / 2 - 240, w.winfo_screenheight() / 2 - 360))
        w4.title("修改密码")
        w4.resizable(width=False, height=False)  # 窗口不可改大小
        w4.iconbitmap(image_resoure + "mi64.ico")

        lb1=Label(w4,text='修改密码:', borderwidth=0,font=('汉仪雪峰体简', 12))
        lb1.place(x=0, y=0, width=100, height=50)
        lb2 = Label(w4, text='确认密码:', borderwidth=0,font=('汉仪雪峰体简', 12))
        lb2.place(x=0, y=50, width=100, height=50)
        in1_var = StringVar(w4, value='')  # 初始化默认值
        in2_var = StringVar(w4, value='')
        in1 = Entry(w4, foreground='orange', show='★', borderwidth=1, textvariable=in1_var)
        in2 = Entry(w4, foreground='orange', show='★', borderwidth=1, textvariable=in2_var)
        in1.place(x=100, y=0, width=100, height=50)
        in2.place(x=100, y=50, width=100, height=50)
        bt1=Button(w4,text='确定',command=diff)
        bt1.place(x=25, y=100, width=100, height=50)
        w4.mainloop()
    def admin_destory(self):
        with open(filetest, 'r') as json_file:
            data = json.load(json_file)
        data["记住密码"] = "0"
        data["自动登录"] = "0"
        data["id"]="1"
        with open(filetest, 'w') as json_file:
            # print(data)
            json.dump(data, json_file, ensure_ascii=False)



# 事件响应
def _ll0_main(event):
    w.geometry('+%d+%d' % (event.x_root - x, event.y_root - y))  # 实现鼠标拖动
def win_mouse_main(event):  # 拖动需要固定坐标
    global x, y
    x = event.x
    y = event.y
def _ll2_close_main(event):
    # 结束循环状态
    with open(filestate, 'r') as file_state:
        f_state = json.load(file_state)
    f_state["循环状态"] = "0"
    with open(filestate, 'w') as file_state:
        json.dump(f_state, file_state, ensure_ascii=False)
    os._exit(0)#X关闭窗口
lbmb1xy,lbmb2xy,lbmb3xy,lbmb4xy=-100, -40, -40, 720
def lb0_2_start_main(event):#‘数据动态管理平台’按钮
    global z,z1,lbmb1xy, lbmb2xy, lbmb3xy, lbmb4xy

    z=z+1
    with open(filetest, 'r') as json_file:
        data = json.load(json_file)
    if data["id"]=="0":#admin用户管理状态
        if z%2 !=0:
            lbmb1xy, lbmb2xy, lbmb3xy, lbmb4xy = -100, -40, -40, 720

            def lbmbflash():
                global lbmb1xy, lbmb2xy, lbmb3xy, lbmb4xy
                lbmb1.place(x=-100, y=45, width=100, height=40)
                lbmb2.place(x=220, y=-40, width=100, height=40)
                lbmb3.place(x=400, y=-40, width=100, height=40)
                lbmb4.place(x=720, y=45, width=100, height=40)

                if lbmb1xy <= 55:  # -100~60=160
                    lbmb1xy = lbmb1xy + 5
                    lbmb1.place(x=lbmb1xy)
                else:
                    lbmb1.place(x=60, y=45, width=100, height=40)

                if lbmb2xy <= 40:  # -40~45=85
                    lbmb2xy = lbmb2xy + 5
                    lbmb2.place(y=lbmb2xy)
                else:
                    lbmb2.place(x=220, y=45, width=100, height=40)
                if lbmb3xy <= 40:  # -40~45=85
                    lbmb3xy = lbmb3xy + 5
                    lbmb3.place(y=lbmb3xy)
                else:
                    lbmb3.place(x=400, y=45, width=100, height=40)

                if lbmb4xy >= 565:  # 560~720=160
                    lbmb4xy = lbmb4xy - 5
                    lbmb4.place(x=lbmb4xy)
                    # 该函数最久
                    w.after(20, lbmbflash)
                else:
                    lbmb4.place(x=560, y=45, width=100, height=40)
            lbmbflash()
            lb_time.place(x=510, y=450, height=30, width=210)
        else:
            if z1%2 !=0:
                z1 = z1 + 1  # 同步
            lbmb1.place_forget()
            lbmb2.place_forget()
            lbmb3.place_forget()
            lbmb4.place_forget()
            lb_time.place_forget()

            lbbut1.place_forget()
            lbbut2.place_forget()
            lbbut3.place_forget()
            lbbut4.place_forget()
    if data["id"]=="1":# user用户禁用状态
        if z%2 !=0:
            lbmb1.place(x=60,y=45,width=100,height=40)
            lb_time.place(x=510, y=450, height=30, width=210)
        else:
            lbmb1.place_forget()
            lb_time.place_forget()
            lbbut1.place_forget()
            lbbut2.place_forget()
            lbbut3.place_forget()
            lbbut4.place_forget()
            if z1 % 2 != 0:
                z1 = z1 + 1  # 同步

    # lbmb2["state"]= 'disabled'照样触发函数
    # lbmb3["state"]= 'disabled'
    # lbmb4["state"]= 'disabled'
def _lb_mb_1(event):
    global z1
    lbmb1.config(fg='#FFD700')
    z1 = z1 + 1
    if z1 % 2 != 0:
        lbbut1.place(x=160, y=90, width=70, height=30)
        lbbut2.place(x=270, y=90, width=70, height=30)
        lbbut3.place(x=380, y=90, width=70, height=30)
        lbbut4.place(x=490, y=90, width=70, height=30)

    else:
        lbbut1.place_forget()
        lbbut2.place_forget()
        lbbut3.place_forget()
        lbbut4.place_forget()

def _plotanimation():
    pass


#图片事件
def _img00_1(event):lb0_1.config(image=img_0_1)
def _img00_2(event):lb0_1.config(image=img_0_2)
def _img00_21(event):lb0_2.config(image=img_0_21)
def _img00_22(event):lb0_2.config(image=img_0_22)
    #主菜单事件
def _img_mb_11(event):lbmb1['fg']='#00FF00';lbmb1['image']=img_mb_12
def _img_mb_12(event):lbmb1.config(fg='#00FA9A');lbmb1['image']=img_mb_11
def _img_mb_13(event):lbmb1.config(fg='#FFD700');mb4.post(w.winfo_x()+lbmb1.winfo_x(), w.winfo_y()+lbmb1.winfo_y()+lbmb1.winfo_height())  # 鼠标的触发位置xy轴
def _img_mb_21(event):lbmb2.config(fg='#00FF00');lbmb2['image']=img_mb_12
def _img_mb_22(event):lbmb2.config(fg='#00FA9A');lbmb2['image']=img_mb_11
def _img_mb_23(event):lbmb2.config(fg='#FFD700');mb2.post(w.winfo_x()+lbmb2.winfo_x(), w.winfo_y()+lbmb2.winfo_y()+lbmb2.winfo_height())  # 鼠标的触发位置xy轴
def _img_mb_31(event):lbmb3.config(fg='#00FF00');lbmb3['image']=img_mb_12
def _img_mb_32(event):lbmb3.config(fg='#00FA9A');lbmb3['image']=img_mb_11
def _img_mb_33(event):lbmb3.config(fg='#FFD700');mb3.post(w.winfo_x()+lbmb3.winfo_x(), w.winfo_y()+lbmb3.winfo_y()+lbmb3.winfo_height())  # 鼠标的触发位置xy轴
def _img_mb_41(event):lbmb4.config(fg='#00FF00');lbmb4['image']=img_mb_12
def _img_mb_42(event):lbmb4.config(fg='#00FA9A');lbmb4['image']=img_mb_11
def _img_mb_43(event):lbmb4.config(fg='#FFD700');mb4.post(w.winfo_x()+lbmb4.winfo_x(), w.winfo_y()+lbmb4.winfo_y()+lbmb4.winfo_height())  # 鼠标的触发位置xy轴
    #次菜单事件
def _img_but_11(event):lbbut1['fg']='#00FF00';lbbut1['image']=img_mb_22
def _img_but_12(event):lbbut1.config(fg='#C0FF3E');lbbut1['image']=img_mb_21
def _img_but_13(event):lbbut1.config(fg='#FFD700')
def _img_but_21(event):lbbut2.config(fg='#00FF00');lbbut2['image']=img_mb_22
def _img_but_22(event):lbbut2.config(fg='#C0FF3E');lbbut2['image']=img_mb_21
def _img_but_23(event):lbbut2.config(fg='#FFD700')
def _img_but_31(event):lbbut3.config(fg='#00FF00');lbbut3['image']=img_mb_22
def _img_but_32(event):lbbut3.config(fg='#C0FF3E');lbbut3['image']=img_mb_21
def _img_but_33(event):lbbut3.config(fg='#FFD700')
def _img_but_41(event):lbbut4.config(fg='#00FF00');lbbut4['image']=img_mb_22
def _img_but_42(event):lbbut4.config(fg='#C0FF3E');lbbut4['image']=img_mb_21
def _img_but_43(event):lbbut4.config(fg='#FFD700');




def _lb_but1(event):#数据源一
    global z2,z3
    z2 = z2 + 1
    if z2 % 2 != 0:
        draw_set3.get_tk_widget().place_forget()
        draw_set2.get_tk_widget().place_forget()
        draw_set1.get_tk_widget().place(x=40, y=125, width=640, height=325)  # 将画好的画布放置在tkinter界面上
        lb_icon1.place(x=305, y=125, width=35, height=35)  # 在嵌入的mat之上
        lb_icon2.place(x=380, y=125, width=35, height=35)
        if z3 % 2 != 0:
            z3 = z3 + 1
        with open(filestate, 'r') as file_state:
            f_state = json.load(file_state)
        f_state["数据一"]="1"
        f_state["数据二"]="0"
        with open(filestate, 'w') as file_state:
            json.dump(f_state, file_state, ensure_ascii=False)


    else:
        draw_set3.get_tk_widget().place_forget()
        draw_set1.get_tk_widget().place_forget()
        draw_set2.get_tk_widget().place_forget()
        lb_icon1.place_forget()
        lb_icon2.place_forget()
        lb_icon3.place_forget()
        with open(filestate, 'r') as file_state:
            f_state = json.load(file_state)
        f_state["数据一"] = "0"
        with open(filestate, 'w') as file_state:
            json.dump(f_state, file_state, ensure_ascii=False)


    lbbut1.config(fg='#FFD700')
def _lb_but2(event):#数据源二
    global z2,z3
    z3 = z3 + 1
    if z3 % 2 != 0:
        draw_set3.get_tk_widget().place_forget()
        draw_set1.get_tk_widget().place_forget()
        draw_set2.get_tk_widget().place(x=40, y=125, width=640, height=325)  # 将画好的画布放置在tkinter界面上
        lb_icon1.place_forget()
        lb_icon2.place_forget()
        lb_icon3.place(x=343, y=125, width=35, height=35)  # 在嵌入的mat之上
        if z2 % 2 != 0:
            z2 = z2 + 1
        with open(filestate, 'r') as file_state:
            f_state = json.load(file_state)
        f_state["数据二"] = "1"
        f_state["数据一"] = "0"

        with open(filestate, 'w') as file_state:
            json.dump(f_state, file_state, ensure_ascii=False)

    else:
        draw_set3.get_tk_widget().place_forget()
        draw_set2.get_tk_widget().place_forget()
        draw_set1.get_tk_widget().place_forget()
        lb_icon1.place_forget()
        lb_icon2.place_forget()
        lb_icon3.place_forget()
        with open(filestate, 'r') as file_state:
            f_state = json.load(file_state)
        f_state["数据二"] = "0"
        with open(filestate, 'w') as file_state:
            json.dump(f_state, file_state, ensure_ascii=False)


    lbbut2.config(fg='#FFD700')
def _lb_but3(event):#数据源二
    global z2,z3,z4
    z4 = z4 + 1
    if z4 % 2 != 0:
        draw_set1.get_tk_widget().place_forget()
        draw_set2.get_tk_widget().place_forget()
        draw_set3.get_tk_widget().place(x=40, y=125, width=640, height=325)  # 将画好的画布放置在tkinter界面上
        lb_icon1.place(x=305, y=125, width=35, height=35)  # 在嵌入的mat之上
        lb_icon2.place(x=380, y=125, width=35, height=35)
        lb_icon3.place(x=343, y=125, width=35, height=35)
    else:
        draw_set3.get_tk_widget().place_forget()
        draw_set2.get_tk_widget().place_forget()
        draw_set1.get_tk_widget().place_forget()
        lb_icon1.place_forget()
        lb_icon2.place_forget()
        lb_icon3.place_forget()
    lbbut3.config(fg='#FFD700')
def _lb_but4(event):
    global z5
    z5 = z5 + 1
    if z5 % 2 != 0:
        lbbut4.config(text="关闭")
        with open(filestate, 'r') as file_state:
            f_state = json.load(file_state)
        f_state["循环状态"] = "1"
        print(f_state)
        with open(filestate, 'w') as file_state:
            json.dump(f_state, file_state, ensure_ascii=False)
        if f_state["数据一"] == "1" and f_state["数据二"] == "0":
            print('数据一')
            #os.popen()不显示cmd窗口
            #os.system('python F:/WorkSpace/end_design/enddesign/screengif.py')#没有其他参数，有cmd窗口
            #win32api.WinExec("python F:/WorkSpace/end_design/enddesign/screengif.py", 0)#test2.py能显示activitive1.py不显示
            print("python "+os.getcwd()+"activitive_data1.py")
            win32api.WinExec("python "+os.getcwd()+"/activitive_data1.py",1)
        if f_state["数据二"] == "1" and f_state["数据一"] == "0":
            print('数据二')
            win32api.WinExec("python "+os.getcwd()+"/activitive_data2.py",1)
        if f_state["数据二"] != "1" and f_state["数据一"] != "1":
            tkinter.messagebox.showerror('错误', '未指定数据目标！')

    else:
        lbbut4.config(text="外置")
        #结束循环状态
        with open(filestate, 'r') as file_state:
            f_state = json.load(file_state)
        f_state["循环状态"] = "0"
        with open(filestate, 'w') as file_state:
            json.dump(f_state, file_state, ensure_ascii=False)




#窗口初始化
w=Tk()
w.geometry('720x480+%d+%d' % (w.winfo_screenwidth() / 2 - 360, w.winfo_screenheight() / 2 - 360))
w.overrideredirect(True)#窗口无边框，没有任务栏

# 状态文件
if os.path.exists(filestate):
    print('存在')
    pass
else:
    with open(filestate, 'w') as state_file:
        json.dump({"外置关闭": "0", "数据一": "0", "数据二": "0", "循环状态": "", "数据一名称": "氧气", "数据二名称": "磷化氢", "itime": "0"},
                  state_file, ensure_ascii=False)



#图片载入区

img_0 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "main.png"))
img_0_1 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "mainX-1.png"))
img_0_2 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "X-2.png"))
img_0_21 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "main_start1.png"))
img_0_22 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "main_start2.png"))
img_mb_11 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "lb1_1.png"))
img_mb_12 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "lb1_2.png"))
img_mb_21 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "lb2_1.png"))
img_mb_22 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "lb2_2.png"))
img_lb_time = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "label_time2.png"))
img_icon1 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "lb_icon1.png"))
img_icon2 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "lb_icon2.png"))
img_icon3 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "lb_icon3.png"))
img_icon4 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "lb_icon4.png"))
img_icon5 = ImageTk.PhotoImage(PIL.Image.open(image_resoure + "lb_icon5.png"))


#标签
lb0=Label(w,image=img_0,borderwidth=0)#bottom白色背景
lb0.place(x=0,y=0,width=720,height=480)
lb0_1=Label(w,image=img_0_1,borderwidth=0)#X按钮
lb0_1.place(x=691,y=0,width=29,height=29)
lb0_2=Label(w,image=img_0_21,borderwidth=0)#开始按钮
lb0_2.place(x=269,y=11,width=184,height=34)


#标签菜单按钮
w2_w2=w2_datahandle()#实例化
w3_w3=w3_datahandle()
w3_turtle=w3_datahandle.w3_datarealtime()
w3_eformat=w3_datahandle.w3_formatchange()#类中类实例化
w4_w4=w4_about()

def _img_mb_test():#测试
    mb4.post(w.winfo_x()+269, w.winfo_y()+140)
lbmb1=Label(w,image=img_mb_11, text="动态管理",fg='#00FA9A',font=('汉仪雪峰体简',18),compound='center',borderwidth=0)
lbmb2=Label(w,image=img_mb_11, text="数据处理",fg='#00FA9A',font=('汉仪雪峰体简',18),compound='center',borderwidth=0)
mb2= Menu(w,borderwidth=0, tearoff=0,font=('迷你简少儿',10),bg='#FFF68F')#单独设立  tearoff=0 没有分割线触发事件
mb2.add_cascade(label='打开原数据表目录',command=w2_w2.w2_opencatalog)

mb2.add_cascade(label='打开原数据表文件',command=w2_w2.w2_opendatafile)

mb2_1son=Menu(mb2, tearoff=0,font=('迷你简少儿',10),bg='#FFF68F')
mb2_1son.add_command(label='数据一',command=w2_w2.w2_error1data)
mb2_1son.add_command(label='数据二',command=w2_w2.w2_error2data)
mb2.add_cascade(label='打开超标数据',menu=mb2_1son)

mb2_2son=Menu(mb2, tearoff=0,font=('迷你简少儿',10),bg='#FFF68F')
mb2_2son.add_command(label='数据一',command=w2_w2.w2_savepicture1)
mb2_2son.add_command(label='数据二',command=w2_w2.w2_savepicture2)
mb2_2son.add_command(label='合并截图',command=w2_w2.w2_savepicture1)
mb2.add_cascade(label='保存图片',menu=mb2_2son)

mb2.add_cascade(label='设置预警值上下限',command=w2_w2.w2_warning)
mb2.add_cascade(label='查看数据信息',command=w2_w2.w2_info)
mb2.add_cascade(label='导出指定范围数据',command=w2_w2.w2_output)
mb2.add_cascade(label='设置当前数据更新频率',command=w2_w2.w2_flashdata)


lbmb3=Label(w,image=img_mb_11, text="功能扩展",fg='#00FA9A',font=('汉仪雪峰体简',18),compound='center',borderwidth=0)
mb3= Menu(w,borderwidth=0, tearoff=0,font=('迷你简少儿',10),bg='#FFF68F')#tearoff=0 没有分割线触发事件

mb3_3son=Menu(mb3, tearoff=0,font=('迷你简少儿',10),bg='#FFF68F')
mb3_3son.add_command(label='数据一',command=w3_turtle.w3_turtle1)
mb3_3son.add_command(label='数据二',command=w3_turtle.w3_turtle2)
mb3_3son.add_command(label='实时数据处理',command=w3_turtle.w3_datadealtime)
mb3.add_cascade(label='Turtle数据处理',menu=mb3_3son)
mb3.add_cascade(label='研究生数据分析',command=w3_w3.s)
mb3.add_cascade(label='图像处理',command=_img_mb_test)

mb3_1son=Menu(mb3, tearoff=0,font=('迷你简少儿',10),bg='#FFF68F')
mb3_1son.add_command(label='txt转csv',command=w3_eformat.w3_txttocsv)
mb3_1son.add_command(label='csv转txt',command=w3_eformat.w3_csvtotxt)
mb3_1son.add_command(label='txt转excel',command=w3_eformat.w3_txttoexcel)
mb3_1son.add_command(label='excel转txt',command=w3_eformat.w3_exceltotxt)
mb3_1son.add_command(label='csv转excel',command=w3_eformat.w3_csvtoexcel)
mb3_1son.add_command(label='excel转csv',command=w3_eformat.w3_exceltocsv)
mb3.add_cascade(label='格式转化',menu=mb3_1son)

mb3_2son=Menu(mb3, tearoff=0,font=('迷你简少儿',10),bg='#FFF68F')
mb3_2son.add_command(label='全屏截图',command=w3_w3.w3_savescreen)
mb3_2son.add_command(label='自由裁剪',command=w3_w3.w3_savefreedom)
mb3.add_cascade(label='屏幕截图',menu=mb3_2son)

lbmb4=Label(w,image=img_mb_11, text="应用设置",fg='#00FA9A',font=('汉仪雪峰体简',18),compound='center',borderwidth=0)
mb4= Menu(w,borderwidth=0, tearoff=0,font=('迷你简少儿',10),bg='#FFF68F')#tearoff=0 没有分割线触发事件
mb4.add_cascade(label='账户注销',command=w4_w4.admin_destory)
mb4.add_cascade(label='登录窗口',command=admin_sign)

mb4_1son=Menu(mb3, tearoff=0,font=('迷你简少儿',10),bg='#FFF68F')
mb4_1son.add_command(label='Admin',command=w4_w4.revisepass1)
mb4_1son.add_command(label='User',command=w4_w4.revisepass2)
mb4.add_cascade(label='修改密码',menu=mb4_1son)

mb4.add_cascade(label='关于平台',command=w4_w4.about)
mb4.add_cascade(label='退出程序',command=w4_w4.exitwin)
lbmb4.place(x=560,y=45,width=100,height=40)
lbmb1.place_forget()
lbmb2.place_forget()
lbmb3.place_forget()
lbmb4.place_forget()



lbbut1=Label(w,image=img_mb_21, text="数据源一",fg='#C0FF3E',font=('迷你简少儿',12),compound='center',borderwidth=0)
lbbut2=Label(w,image=img_mb_21, text="数据源二",fg='#C0FF3E',font=('迷你简少儿',12),compound='center',borderwidth=0)
lbbut3=Label(w,image=img_mb_21, text="资源合并",fg='#C0FF3E',font=('迷你简少儿',12),compound='center',borderwidth=0)
lbbut4=Label(w,image=img_mb_21, text="外置关闭",fg='#C0FF3E',font=('迷你简少儿',12),compound='center',borderwidth=0)

#数据初始化
datain.datain_rand()#标准随机范围数据
if os.path.exists(fileerror+"error1.txt")==False:#即时错误时钟
    with open(fileerror+"error1.txt", 'w') as error_file:
        error_file.write(datain.dataname1+'\t'+datain.dataname3+'\n')
if os.path.exists(fileerror+"error2.txt")==False:#即时错误时钟
    with open(fileerror+"error2.txt", 'w') as error_file:
        error_file.write(datain.dataname2+'\t'+datain.dataname3+'\n')



#数据一(可用引用模块)                                                                                      +++++++++++++++
# max_limitone,min_limitone=12,2#数据一在前面
# max_limittwo,min_limittwo=30,6#数据二
#基于Matplotlib可嵌入式设计
count=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
plt.switch_backend('agg')
data_one,xdata_one,y1data=1,[],[]#全局变量
fig1 = plt.Figure(figsize=(5, 4), dpi=80)  # 设置空画布fig，figsize为大小英寸，dpi为分辨率像素 低会模糊(place改变大小)
draw_set1 = FigureCanvasTkAgg(fig1, master=w)  # 将空画布设置在tkinter上
ax1 = fig1.add_subplot(111)  # 设置坐标轴

x1data, y1data = [], []
ln1, = ax1.plot([], [], '-o', alpha=0.8, color='purple', markerfacecolor='orange', label=datain.dataname1, animated=False) #ln1，是曲线
fig1.legend(loc="upper left", shadow=True)
def init1():
    ax1.set_xlim(0, 20)
    ax1.set_ylim(-2, 25)
    ax1.set_ylabel('占空气百分比')
    #ax1.set_title(datain.dataname1)
    ax1.set_xticks(count)
    return ln1,  # 返回曲线
def update1(n):#1.画图可以不用np类型  2.子图ax可用set_* (plt的方法)
    global data_one,xdata_one,y1data,max_limitone,min_limitone
    if data_one<20:
        xdata_one.append(data_one)
        y1data.append(n)
        ln1.set_data(xdata_one, y1data)
    else:
        one_last = datain.dataset1[data_one]
        #print(data_one,' ',y1data)
        y1data= y1data[1:]
        y1data.append(one_last)
        ln1.set_data(xdata_one, y1data)
    if datain.dataset1[data_four]<min_limitone or datain.dataset1[data_four]>max_limitone:
        #imo_min, imo_max = 0.02, 0.12  # O2
        #imp_min, imp_max = 0.06, 0.30  # PH3
        #print(max_limitone,' ',min_limitone)
        lb_icon1['image']=img_icon1
        lb_icon2['image']=img_icon4
        winsound.PlaySound(image_resoure+"error.wav", flags=1)
        with open(fileerror+"error1.txt",'a') as ferror:
            ferror.write(str(datain.dataset1[data_four])+'\t'+datain.dataset3[data_four]+'\n')

    else:
        lb_icon1['image'] = img_icon2
        lb_icon2['image'] = img_icon3
    data_one = data_one + 1
    return ln1,
ani1 = FuncAnimation(fig1, update1, frames=datain.dataset1, init_func=init1, blit=True,interval=1000)


#数据二
data_two,x2data,y2data=1,[],[]#全局变量
fig2 = plt.Figure(figsize=(5, 4), dpi=80)  # 设置空画布fig，figsize为大小英寸，dpi为分辨率像素 低会模糊(place改变大小)
draw_set2 = FigureCanvasTkAgg(fig2, master=w)  # 将空画布设置在tkinter上
ax2 = fig2.add_subplot(111)  # 设置坐标轴

ln2, = ax2.plot([], [], '-o', alpha=0.8, color='green', markerfacecolor='orange', label=datain.dataname2, animated=False) #ln2，是曲线
fig2.legend(loc="upper left", shadow=True)
def init2():
    ax2.set_xlim(0, 20)
    ax2.set_ylim(-2, 40)
    ax2.set_ylabel('占空气百分比')
    ax2.set_xticks(count)
    #ax2.set_title(datain.dataname2)
    return ln2,  # 返回曲线
def update2(n):#画图可以不用np类型
    global data_two,x2data,y2data,max_limittwo,min_limittwo
    if data_two<20:
        x2data.append(data_two)
        y2data.append(n)
        ln2.set_data(x2data, y2data)

    else:
        one_last = datain.dataset2[data_two]
        #print(data_two,' ',y2data)
        y2data= y2data[1:]
        y2data.append(one_last)
        ln2.set_data(x2data, y2data)
    if datain.dataset2[data_four]<min_limittwo or datain.dataset2[data_four]>max_limittwo:
        #imp_min, imp_max = 0.06, 0.30  # PH3
        lb_icon3['image']=img_icon4
        winsound.PlaySound(image_resoure+"error.wav", flags=1)
        with open(fileerror+"error2.txt",'a') as ferror:
            ferror.write(str(datain.dataset2[data_four])+'\t'+datain.dataset3[data_four]+'\n')
    else:
        lb_icon3['image'] = img_icon5
    data_two = data_two + 1
    return ln2,
#draw_set2.get_tk_widget().place(x=15, y=20, height=250, width=740)  # 将画好的画布放置在tkinter界面上
ani2 = FuncAnimation(fig2, update2, frames=datain.dataset2, init_func=init2, blit=True,interval=1000)


#资源合并
data_three,x3data,y3data=1,[],[]#全局变量
data_four,x4data,y4data=1,[],[]#全局变量
fig3 = plt.Figure(figsize=(5, 4), dpi=80)  # 设置空画布fig，figsize为大小英寸，dpi为分辨率像素 低会模糊(place改变大小)
draw_set3 = FigureCanvasTkAgg(fig3, master=w)  # 将空画布设置在tkinter上
ax3 = fig3.add_subplot(211)  # 设置坐标轴
ax4 = fig3.add_subplot(212)  # 设置坐标轴
ln3, = ax3.plot([], [], '-o', alpha=0.8, color='purple', markerfacecolor='orange', label=datain.dataname1, animated=False) #ln1，是曲线
ln4, = ax4.plot([], [], '-o', alpha=0.8, color='green', markerfacecolor='orange', label=datain.dataname2, animated=False) #ln2，是曲线
fig3.legend(loc="upper left", shadow=True)
def init3():
    ax3.set_xlim(0, 20)
    ax3.set_ylim(-2, 25)
    ax3.set_ylabel('占空气百分比')
    ax3.set_xticks(count)
    #ax3.set_title(datain.dataname1)
    return ln3,  # 返回曲线
def init4():
    ax4.set_xlim(0, 20)
    ax4.set_ylim(-2, 40)
    ax4.set_ylabel('占空气百分比')
    ax4.set_xticks(count)
    #ax4.set_title(datain.dataname2)
    return ln4,  # 返回曲线

def update3(n):
    global data_three,x3data,y3data
    if data_three<20:
        x3data.append(data_three)
        y3data.append(n)
        ln3.set_data(x3data, y3data)
    else:
        one_last = datain.dataset1[data_three]
        #print(data_three,' ',y3data)
        y3data= y3data[1:]
        y3data.append(one_last)
        ln3.set_data(x3data, y3data)
    data_three = data_three + 1
    return ln3,
def update4(n):
    global data_four,x4data,y4data
    if data_four<20:
        x4data.append(data_four)
        y4data.append(n)
        ln4.set_data(x4data, y4data)
    else:
        one_last = datain.dataset2[data_four]
        #print(data_four,' ',y4data)
        y4data= y4data[1:]
        y4data.append(one_last)
        ln4.set_data(x4data, y4data)
    data_four = data_four + 1
    return ln4,
ani3 = FuncAnimation(fig3, update3, frames=datain.dataset1, init_func=init3, blit=True,interval=1000)
ani4 = FuncAnimation(fig3, update4, frames=datain.dataset2, init_func=init4, blit=True,interval=1000)


lb_time = tkinter.Label(w,image=img_lb_time,fg=a2, font=('汉仪雪峰体简', 15),compound='center')   #标签覆盖但不会增加内存
lb_icon1=Label(w,image=img_icon2,borderwidth=0)
lb_icon2=Label(w,image=img_icon3,borderwidth=0)
lb_icon3=Label(w,image=img_icon5,borderwidth=0)


#热键响应
lb0.bind('<B1-Motion>', _ll0_main)
w.bind('<1>', win_mouse_main)
lb0_1.bind('<Enter>', _img00_2)
lb0_1.bind('<Leave>', _img00_1)
lb0_1.bind('<1>', _ll2_close_main)#关闭按钮
lb0_2.bind('<Enter>', _img00_22)
lb0_2.bind('<Leave>', _img00_21)
lb0_2.bind('<1>', lb0_2_start_main)#开始按钮
    #菜单标签响应
lbmb1.bind('<Enter>', _img_mb_11)
lbmb1.bind('<Leave>', _img_mb_12)
lbmb1.bind('<1>', _lb_mb_1)#修改_img_mb_13
lbmb2.bind('<Enter>', _img_mb_21)
lbmb2.bind('<Leave>', _img_mb_22)
lbmb2.bind('<1>', _img_mb_23)
lbmb3.bind('<Enter>', _img_mb_31)
lbmb3.bind('<Leave>', _img_mb_32)
lbmb3.bind('<1>', _img_mb_33)
lbmb4.bind('<Enter>', _img_mb_41)
lbmb4.bind('<Leave>', _img_mb_42)
lbmb4.bind('<1>', _img_mb_43)
    #次菜单按钮响应
lbbut1.bind('<Enter>', _img_but_11)
lbbut1.bind('<Leave>', _img_but_12)
lbbut1.bind('<1>', _lb_but1)#修改_img_mb_13
lbbut2.bind('<Enter>', _img_but_21)
lbbut2.bind('<Leave>', _img_but_22)
lbbut2.bind('<1>', _lb_but2)
lbbut3.bind('<Enter>', _img_but_31)
lbbut3.bind('<Leave>', _img_but_32)
lbbut3.bind('<1>', _lb_but3)
lbbut4.bind('<Enter>', _img_but_41)
lbbut4.bind('<Leave>', _img_but_42)
lbbut4.bind('<1>', _lb_but4)





#窗口处理
lb_gettime()
w.attributes("-topmost", True)
w.wm_attributes('-topmost', 1)
w.withdraw()#隐藏窗口
admin_sign()#密码登录窗口
w.mainloop()



