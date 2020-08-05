import datetime,json,matplotlib
import numpy as np
import matplotlib.pyplot as plt
#from paint import datain#不能在其他目录打开
"""4、最后了解一下 python 在不同层级目录import 模块的方法（重点）
有一个文件夹/home/a, 里面有个模块叫b.py, 我怎么把他import到程序里？
方法一:    (属于刚开始分析的代码里第一种情况)
import sys; 
sys.path.append(“/home/a/”) 
import b
方法二：
在目录里面增加__init__.py文件，里面可以写import时执行的代码，当然也可以留空就可以. 
import home.a.b
方法三：
from home.a.b import * 
前提 home、a中都包括__init__.py 即：要导入的文件的当前目录和父目录都要有init.py文件"""
import datain,os
matplotlib.rcParams['axes.unicode_minus']=False#显示“-”
plt.rcParams['font.sans-serif']=['SimHei']#正常显示中文字符

def live_xy(x_vec, y1_data, line1, identifier='', pause_time=1):

    if line1 == []:
        plt.ion()#开启动态交互模式

        fig = plt.figure(figsize=(13, 6))
        ax = fig.add_subplot(111)

        print(x_vec, '\n',datain.dataset4[0:len(x_vec)])
        line1, = ax.plot(x_vec, y1_data, '-o', alpha=0.8, color='purple',markerfacecolor='orange',label='氧气')
        plt.legend(loc="upper left", shadow=True)#左上的方块图例 有阴影
        plt.ylabel('占空气百分比')
        plt.title('氧气浓度{}'.format(identifier))
        plt.show()
    if data_n < 20:
        for a, b in zip(x_vec, y1_data):  # 对点显示数据标点数据
            plt.text(a, b, b, ha='center', va='bottom', fontsize=10)  # markerfacecolor='orange'标点颜色
        plt.xticks(x_vec, datain.dataset4[0:len(x_vec)], fontsize=6, rotation=60)
    else:
        plt.clf()#清除画布
        line1, = plt.plot(x_vec, y1_data, '-o', alpha=0.8, color='purple', markerfacecolor='orange', label='氧气')#，曲线 alpha透明度
        for a, b in zip(x_vec, y1_data):  # 标点数据
            plt.text(a, b, b, ha='center', va='bottom', fontsize=10)  # markerfacecolor='orange'标点颜色
        x_vecc=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        #rand_valx = datain.dataset4[data_n]#第21个
        y_vecc = datain.dataset4[data_n-20:data_n]#根据data_n变化数据左移
        y1_data1=datain.dataset1[data_n-20:data_n]
        #for a, b in zip(x_vec, y1_data1):  # 标点数据
        #    c=plt.text(a, b, b, ha='center', va='bottom', fontsize=10)  # markerfacecolor='orange'标点颜色
        # y_vecc[-1] = rand_valx
        # y_vecc = np.append(y_vecc[1:], 0.0)
        #print(rand_valx)
        plt.xticks(x_vecc, y_vecc, fontsize=6, rotation=60)

        #print(datain.dataset4[0:len(x_vec)])

    line1.set_data(x_vec, y1_data)#更新数据
    plt.xlim(0, 21)
    plt.ylim(0, 1)#math
    # plt.ylim(18, 25)#word1
    if np.min(y1_data) <= line1.axes.get_ylim()[0] or np.max(y1_data) >= line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-1, np.max(y1_data) + 1])

    plt.pause(pause_time)

    return line1

#主函数
x = []     #数值序列的变化列表
#datain.datain1()#生成列表
datain.datain_rand()
data_n = 0 #数据位置
line1 = [] #初始化和设置上下限
y_vecc=[]  #时间序列的变化列表
while True:

    if data_n < 20:
        x=[]#防止叠加
        for i in range(1, data_n + 2):
            x.append(i)
        x_vec = x
        y_vec = datain.dataset1[0:len(x)]
        line1 = live_xy(x_vec, y_vec, line1)

    else:
        # data_n=20   #20个数据
        # x=[]
        # for i in range(1, data_n + 2):
        #     x.append(i)
        x_vec = x
        #y_vec = datain.dataset1[0:len(x)]#20个

        rand_val = datain.dataset1[data_n]#第21个数

        y_vec[-1] = rand_val#第21个数给y最后一个
        #print(data_n," ",x_vec," ",rand_val," ",y_vec)#测试

        line1 = live_xy(x_vec, y_vec, line1)#执行函数显示
        y_vec = np.append(y_vec[1:], 0.0)  # 把第一个数切掉，将0.0添加到y_vec[1:]数组的最后，以此实现最后一个数据更新
    data_n = data_n + 1
    #停止
    with open(os.getcwd()+'/data/state.json','r') as f:
        statejson = json.load(f)
    if statejson["循环状态"] == "0":
        exit(0)











