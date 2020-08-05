import os,json
import random

dataset1 = []  # O2数组(float)
dataset2 = []  # ph3数组(float)
dataset3 = []  # 日期时间数组
dataset4 = []  # 具体时间数组 #由于显示位置不足，需具体时间数组
dataset5 = []  # 具体日期数组
dataname1,dataname2,dataname3="","",""
filestate='F:/WorkSpace/end_design/enddesign/data/state.json'
def dataname(filename):
    global dataname1,dataname2,dataname3
    with open(filename,'r') as f:
        a=f.readline()
        temp1 = a.strip('\n')
        dataname1, dataname2, dataname3 = temp1.split('\t')
    #print(dataname1, dataname2, dataname3)

    with open(filestate, 'r') as file_state:
        f_state = json.load(file_state)

    f_state["数据一名称"] = dataname1
    f_state["数据二名称"] = dataname2
    with open(filestate, 'w') as file_state:
        json.dump(f_state, file_state, ensure_ascii=False)


def datain1():#带单位的随机数据
    filename = 'F:\\WorkSpace/0test/work1.txt'
    def loadDatadet(infile):
        f = open(infile, 'r')
        f.readline()#去除第一行标题
        sourceInLine = f.readlines()#读取所有行的数据
        #dataset1 = []  # O2数组
        for line in sourceInLine:
            temp1 = line.strip('\n')#删除括号内指定字符串头部和尾部字符 split('%\t',1) 1代表%\t分割一次
            temp2,tempz = temp1.split('%\t')#O2和后面部分 f.write(str(a) + '%' + '\t' + str(b) + 'mg/m3'+ '\t' + arrtime[i] + '\n')
            dataset22,dataset33=temp1.split('%\t')[1].split('mg/m3\t')#split('%\t')[1]：取'%\t'之后的 再分割
            dataset44= temp1.split('%\t')[1].split('mg/m3\t')[1].split()[1]#split()分空格
            dataset1.append(float(temp2))    ##O2数组 不转数字会出现乱码，y轴排序会出现问题
            dataset2.append(float(dataset22))#ph3数组
            dataset3.append(dataset33)# 日期时间数组
            dataset4.append(dataset44)# 具体时间数组
            # for i in range(len(dataset1)):
                #if i % 2 != 0:
                    #dataset.append(temp2[i])#时间数组
                #else:
                    #dataset2.append(temp2[i])#O2数组
                    #dataset3.append(temp3[i])#ph3数组
            #return dataset1
            # data1 = [float(x) for x in dataset1]  # 将字符转为浮点的数
            # data2 = [float(x) for x in dataset2]  # 将字符转为浮点的数
    #dataset1 = loadDatadet(filename)
    loadDatadet(filename)#函数
    #print('dataset1=', dataset1, '\n', dataset2, '\n', dataset3, '\n', dataset4)
#datain1()#带单位的随机数据

def datain2():
    filename='F:\\WorkSpace/0test/work2.txt'
    dataset2 = []
    def loadDatadet(infile):
        f=open(infile,'r')
        f.readline()
        sourceInLine=f.readlines()
        dataset1=[]
        for line in sourceInLine:
            temp1=line.strip('mg/m3\n')
            temp2=temp1.split('%\t')

            for i in range(len(temp2)):#len(temp2)==2
                if i%2==0:
                    dataset1.append(temp2[i])
                else: dataset2.append(temp2[i])
        return dataset1
    dataset1=loadDatadet(filename)
    #print('dataset1=',dataset1,'\ndataset2=',dataset2)
#datain2()

def datain_math():
    filename = 'F:\\WorkSpace/0test/imidata_math.txt'
    def loadDatadet(infile):
        f = open(infile, 'r')
        f.readline()  # 去除第一行标题
        sourceInLine = f.readlines()  # 读取所有行的数据
        # dataset1 = []  # O2数组
        for line in sourceInLine:
            temp1 = line.strip('\n')  # 删除括号内指定字符串头部和尾部字符 split('%\t',1) 1代表%\t分割一次
            tempz1, tempz2,tempz3 = temp1.split('\t')  #O2和后面部分 f.write(str(a)  + '\t' + str(b) + '\t' + arrtime[i] )
            # dataset22, dataset33 = temp1.split('\t')[1].split('\t')#split('\t')[1]取第一个分隔符后的第二组数str(b) + '\t' + arrtime[i]
            tempz5,tempz4 = tempz3.split()
            dataset1.append(float(tempz1))    #O2数组 不转数字会出现乱码，y轴排序会出现问题
            dataset2.append(float(tempz2))    #ph3数组
            dataset3.append(tempz3)   # 日期时间数组
            dataset4.append(tempz4)# 具体时间数组
            dataset5.append(tempz5)   # 具体日期数组

            #print(tempz1,' ', tempz2,' ',tempz3,' ',tempz4,' ',tempz5)
    loadDatadet(filename)
    dataname(filename)
#datain_math()
def datain_rand():
    filename = 'F:\\WorkSpace/0test/imidata_rand.txt'
    def loadDatadet(infile):
        f = open(infile, 'r')
        f.readline()  # 去除第一行标题
        sourceInLine = f.readlines()  # 读取所有行的数据
        # dataset1 = []  # O2数组
        for line in sourceInLine:
            temp1 = line.strip('\n')  # 删除括号内指定字符串头部和尾部字符 split('%\t',1) 1代表%\t分割一次
            tempz1, tempz2,tempz3 = temp1.split('\t')  #O2和后面部分 f.write(str(a)  + '\t' + str(b) + '\t' + arrtime[i] )
            # dataset22, dataset33 = temp1.split('\t')[1].split('\t')#split('\t')[1]取第一个分隔符后的第二组数str(b) + '\t' + arrtime[i]
            tempz5,tempz4 = tempz3.split()
            dataset1.append(float(tempz1))    #O2数组 不转数字会出现乱码，y轴排序会出现问题
            dataset2.append(float(tempz2))    #ph3数组
            dataset3.append(tempz3)   # 日期时间数组
            dataset4.append(tempz4)   # 具体时间数组
            dataset5.append(tempz5)   # 具体日期数组


            #print(tempz1,' ', tempz2,' ',tempz3,' ',tempz4,' ',tempz5)
    loadDatadet(filename)
    dataname(filename)
#datain_rand()

def datain_dealtime():
    filename = 'F:/WorkSpace/0test/turtle_datadeal.txt'

    def loadDatadet(infile):
        f = open(infile, 'r')
        f.readline()  # 去除第一行标题
        sourceInLine = f.readlines()  # 读取所有行的数据
        # dataset1 = []  # O2数组
        for line in sourceInLine:
            temp1 = line.strip('\n')  # 删除括号内指定字符串头部和尾部字符 split('%\t',1) 1代表%\t分割一次
            tempz1, tempz2, tempz3 = temp1.split('\t')  # O2和后面部分 f.write(str(a)  + '\t' + str(b) + '\t' + arrtime[i] )
            # dataset22, dataset33 = temp1.split('\t')[1].split('\t')#split('\t')[1]取第一个分隔符后的第二组数str(b) + '\t' + arrtime[i]
            tempz5, tempz4 = tempz3.split()
            dataset1.append(float(tempz1))  # O2数组 不转数字会出现乱码，y轴排序会出现问题
            dataset2.append(float(tempz2))  # ph3数组
            dataset3.append(tempz3)  # 日期时间数组
            dataset4.append(tempz4)  # 具体时间数组
            dataset5.append(tempz5)  # 具体日期数组

            # print(tempz1,' ', tempz2,' ',tempz3,' ',tempz4,' ',tempz5)

    loadDatadet(filename)
    dataname(filename)











