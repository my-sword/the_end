import os,json
import random
import datetime
import numpy as np
import math,matplotlib
import matplotlib.pyplot as plt
"""
该技术的基本原理是向粮堆充入浓度为99.5%的高纯度氮气，通过使用专用设备把粮仓内的氧气置换出来，使储粮环境长期保持高氮浓度（96%以上）、低氧浓度（4%以下）或绝氧状态，
地下仓、浅圆仓、立筒仓和近年来新建的高大平房仓均为缺氧危险作业场所。造成缺氧的原因有: 气调储粮，杀灭储粮害虫的浓度要求，氧气浓度控制在2%以下，
抑制储粮害虫生长发育的氧气浓度控制范围在 2%～12%，平均氧气浓度控制在5%；再加上粮食自身的呼吸。因此，缺氧是粮食仓库作业中必须警戒的危险因素。
最低  平均  最高      考虑白天温度高O2变化快 黑夜温度低呼吸作用弱
0.02 0.05 0.12

在粮仓中增加PH3气体传感器，来实时监测PH3的浓度，直到PH3气体浓度达到国家卫生标准以下，才开仓放气。
蒸前1d磷化氢平均浓度粮堆空气中0.06mg/m3,仓内为0.04mg/m3,低于国家卫生标准(工作场所空气磷化氢浓度MAC为0.30mg/m3)
惠蒸期间及二次闭仓后各时段磷化氢浓度见表1打开粮仓门窗放气(自然通风)2d后测定仓内空气磷化氢浓度平均为0.20mg/m3
最低  平均  最高  
0.06 0.20 0.30
"""


matplotlib.rcParams['axes.unicode_minus']=False#显示“-”
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文字符
filestate='F:/WorkSpace/end_design/enddesign/data/state.json'#随机分布，以后解决
#正弦随机数：符合正弦曲线。
def suijitime(n=200):
    hms=[]
    now = datetime.datetime.now()
    hms = np.append(hms, now.strftime("%Y-%m-%d %H:%M:%S"))
    for i in range(n):
        now = now + datetime.timedelta(seconds=-1)#前一秒
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        hms=np.append(hms,date_time)
    return hms[::-1]#原本倒序再倒序输出
arrtime=suijitime()

#相关性函数
def statetime():
    hms = []
    now = datetime.datetime.now()
    date_time = now.strftime("%H")
    #print(date_time)测试当前白天黑夜
    if int(date_time) > 6 and int(date_time) < 18:
        return 1
    else:
        return 0
def risetime():#另外可以模拟根据时间系数上升  中午到达最大值（用sin（x）代替）
    hms = []
    now = datetime.datetime.now()
    date_time = now.strftime("%H")
    if statetime() == 1:
        #if 24-int(date_time) >=12  and 24-int(date_time) <= 18:
        return 24-int(date_time)-5#-5是1~7更好规划
    else:
        return int(date_time)-5
def imitate():
    os.chdir('F:/WorkSpace/0test')
    if (os.path.exists('F:/WorkSpace/0test/imidata_math.txt')):
        os.remove('F:/WorkSpace/0test/imidata_math.txt')
    f = open('imidata_math.txt', 'a+')  # 追加读写
    f.write('O2（%）\tPH3（%mg/m3）\t{}\n'.format('时间'))

    imo_min,imo_max=0.02,0.12#O2
    imp_min,imp_max=0.06,0.30#PH3
    state_b,state_h=1,0#白天1 黑夜0
    for i in range(200):
        a = random.randint(20, 120)
        a = float(a) / 10
        b = random.randint(60, 300)
        b = float(b) / 10
        a,b = ('%.2f' % a),('%.2f' % b)

    f.write(str(a) + '\t' + str(b) + '\t' + arrtime[i] + '\n')
    #先四分之一周期
    #sinx
    f.close()

#标准浓度函数
def matplotlib_O2():#标准O2浓度函数
    # 说明 呼吸作用基本符合正弦函数，某点的导数cosx即为斜率，增长=固定增速*（1+斜率）那么白天黑夜的增长曲线符合CO2
    # 氧气充进去状态即为CO2，倒序则为O2
    number_n = 200
    x = np.linspace(0, 2 * np.pi, number_n)  # 横轴标尺：起始值，终止值，元素个数
    def b(n):
        xx = 0
        s = 15.0#15到162
        y = []
        for j in range(n):
            xx = xx + 2 * math.pi / n
            zeng = 0.1 * (1 + math.fabs(10*math.cos(2*xx)))#增长=固定增速*（1+陡度(有上限值)*斜率(周期*周期列表数据)）
            #print(zeng)
            s = s + zeng
            y.append(s)#最大值162

        #print(y)
        return y

    arr_b = b(number_n)
    arr_b = arr_b[::-1]  #O2的浓度变化  若#则为CO2的浓度变化
    yy = np.array(arr_b)

    plt.plot(x, yy, 'b', label='O2变化曲线')
    plt.legend()  # 图例：将图形的样例显示出来   若无则无label显示 plot：画函数图，legend：显示图片
    plt.show()
    return arr_b
def matplotlib_PH3():
    x = np.linspace(-7, 7, 200)  # 横轴标尺：起始值，终止值，元素个数
    #print(x)
    #print(150 * np.power(1.2, x))
    y=(150 * np.power(1.2, x))[::-1]#幅度比自然对数稍低
    yy=y.tolist()
    plt.plot(x, y, 'b', label='213')
    plt.legend()  # 图例：将图形的样例显示出来   若无则无label显示 plot：画函数图，legend：显示图片
    plt.show()
    return yy

#模拟数据写入
def imitate_math():
    os.chdir('F:\\WorkSpace/0test')
    if (os.path.exists('F:\\WorkSpace/0test/imidata_math.txt')):
        os.remove('F:\\WorkSpace/0test/imidata_math.txt')
    f = open('imidata_math.txt', 'a+')  # 追加读写
    f.write('O2（%）\tPH3（%mg/m3）\t{}\n'.format('时间'))

    o2 = matplotlib_O2()
    ph3 = matplotlib_PH3()
    imo_min,imo_max=0.02,0.12#O2
    imp_min,imp_max=0.06,0.30#PH3
    for i in range(200):
        a=o2[i];b=ph3[i]
        a,b=float(a) / 10,float(b)/10
        a, b = '%.2f' % a, ('%.2f' % b)
        f.write(str(a) + '\t' + str(b) + '\t' + arrtime[i] + '\n')
    f.close()
def imitate_rand():
    os.chdir('F:\\WorkSpace/0test')
    if (os.path.exists('F:\\WorkSpace/0test/imidata_rand.txt')):
        os.remove('F:\\WorkSpace/0test/imidata_rand.txt')
    f = open('imidata_rand.txt', 'a+') #追加读写
    f.write('O2（%）\tPH3（%mg/m3）\t{}\n'.format('时间'))

    imo_min,imo_max=0.02,0.12#O2
    imp_min,imp_max=0.06,0.30#PH3
    for i in range(200):
        a = random.randint(15, 130)#必须有超标值和低于标准值
        a = float(a) / 10
        b = random.randint(50, 350)
        b = float(b) / 10
        a, b = ('%.2f' % a), ('%.2f' % b)
        f.write(str(a) + '\t' + str(b) + '\t' + arrtime[i] + '\n')
    f.close()
#主窗口
#imitate_rand()
#imitate_math()
#imitate()

#Turtle窗口
def suijidealtime():#取当前时间往后的200秒数据
    hms=[]
    now = datetime.datetime.now()
    hms = np.append(hms, now.strftime("%Y-%m-%d %H:%M:%S"))
    now = now + datetime.timedelta(seconds=-1)#前一秒
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    hms=np.append(hms,date_time)
    return hms[::-1]#原本倒序再倒序输出


def datadealtime():
    os.chdir('F:/WorkSpace/0test')
    # if (os.path.exists('F:/WorkSpace/0test/turtle_deal.txt')):
    #     os.remove('F:/WorkSpace/0test/turtle_deal.txt')
    f = open('turtle_deal.txt', 'a+')  # 追加读写
    if os.path.getsize('turtle_deal.txt') ==0:
        f.write('O2（%）\tPH3（%mg/m3）\t{}\n'.format('时间'))# 28byte
    #print(os.path.getsize('turtle_deal.txt')) #189-157=32byte
    if os.path.getsize('turtle_deal.txt')<(28+32*12):
        with open(filestate, 'r') as file_state:
            data_state = json.load(file_state)
        data_state["itime"] = "0"
        with open(filestate, 'w') as file_state:
            json.dump(data_state, file_state, ensure_ascii=False)
        for i in range(12):
            a = random.randint(15, 130)  # 必须有超标值和低于标准值
            a = float(a) / 10
            b = random.randint(50, 350)
            b = float(b) / 10
            a, b = ('%.2f' % a), ('%.2f' % b)
            f.write(str(a) + '\t' + str(b) + '\t' + arrtime[i+187] + '\n')  # arrtime[i_time]时间往后的数据

    imo_min, imo_max = 0.02, 0.12  # O2
    imp_min, imp_max = 0.06, 0.30  # PH3
    a = random.randint(15, 130)  # 必须有超标值和低于标准值
    a = float(a) / 10
    b = random.randint(50, 350)
    b = float(b) / 10
    a, b = ('%.2f' % a), ('%.2f' % b)
    f.write(str(a) + '\t' + str(b) + '\t' + suijidealtime()[0]+ '\n')#arrtime[i_time]时间往后的数据
    f.close()
    with open(filestate, 'r') as file_state:
        data_state = json.load(file_state)
    data_state["itime"] = str(int(data_state["itime"])+1)
    with open(filestate, 'w') as file_state:
        json.dump(data_state, file_state, ensure_ascii=False)

    # 去掉第二行(最新的数据开始读取:最新12个)
    with open(filestate, 'r') as file_state:
        data_state = json.load(file_state)
    with open('turtle_deal.txt','r') as f:
        with open('turtle_datadeal.txt','w') as f1:
            f1.write(f.readline())
        for i in range(int(data_state["itime"])):
            f.readline()#去掉前n行,保持最新，与写入数据同步无需判断if os.path.getsize('turtle_datadeal.txt') 》 (28 + 32 * 12):
        with open('turtle_datadeal.txt','a') as f2:
            for line in f.readlines():
                f2.write(line)
#datadealtime()



"""
关键是Aωb，每经过一周期A变化,b递增
正弦型函数解析式：y=Asin(ωx+φ)+b
各常数值对函数图像的影响：
φ：决定波形与X轴位置关系或横向移动距离（左加右减）
ω：决定周期（最小正周期 ）w越大越宽
A：决定峰值（即纵向拉伸压缩的倍数）
b：表示波形在Y轴的位置关系或纵向移动距离（上加下减）
作图方法运用“五点法”作图
“五点作图法”即取当X分别取0，π/2，π，3π/2，2π时y的值。
"""