
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")   #因为警告看着不舒服，这里我把它忽略掉了
#读取数据
admit=pd.read_csv('Admission_Predict_Ver1.1.csv')
print(admit.head())       #看数据前五行
print(admit.dtypes)       #看数据类型，看完决定做什么操作
print (admit.describe())  #看数据的一些指标
#由于此数据集无缺失值，所以不需要进行缺失值操作
#对数据进行预处理

#在这里取一下列名
name=admit.columns.tolist()
print(name)

#计算皮尔逊相关系数
ppmcc=admit.corr()
print(ppmcc)

#这里我们只取皮尔逊系数大于20%的
admit=admit.drop(['Serial No.'],axis=1)

from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor #随机森林回归
predictors=['GRE Score','University Rating','SOP','TOEFL Score','LOR','CGPA','Research']

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold #K折交叉验证
kf= KFold(n_splits=5 ,random_state=1)

alg = RandomForestRegressor(random_state=1, n_estimators=100, min_samples_split=4, min_samples_leaf=2,bootstrap=True,oob_score=True)

predictions = []
for train, test in kf.split(admit):
    train_target = admit["Chance of Admit"].iloc[train]
    full_test_predictions = []
    # 将算法与训练数据相匹配。
    alg.fit(admit[predictors].iloc[train, :], train_target)
    # 进行预测，这里将数据格式转换为浮点数，以避免机器学习错误
    test_predictions =alg.predict(admit[predictors])
    full_test_predictions.append(test_predictions)
    #将所有预测放在一个数组中
    predictions.append(test_predictions)
predictions = np.concatenate(predictions, axis=0)

#模型评估方法
asd=admit["Chance of Admit"]
#模型平均绝对误差mae
errors = abs(asd-test_predictions)
print("随机森林回归模型平均误差mae:",round(np.mean(errors),2))

#均方误差（MSE）
n = len(asd)
mse = sum(np.square(asd - test_predictions))/n
print('随机森林回归均方误差mse:',mse)

#绝对百分比误差 mape
mape = (100*errors)/asd
accurcy1 = np.mean(mape)
print('随机森林回归模型误差率百分比mape:',round(accurcy1,2),'%')


# 计算所有交叉验证折叠的精度分数
score = cross_val_score(alg,admit[predictors],test_predictions,cv=kf)
print("随机森林K折交叉验证的得分值: ",score.mean())

#这里进行编码，代表通过与否
test_predictions[test_predictions>.5]=1
test_predictions[test_predictions<=.5]=0
asd[asd>.5]=1
asd[asd<=.5]=0


#通过与真实数据的比较来计算精度。
accuracy = len(test_predictions[test_predictions == admit["Chance of Admit"]]) / len(test_predictions)
print('随机森林回归模型模型精确度：',accuracy)

#预测减真实值，前150个图像
compare=test_predictions-asd
count_admitted=pd.value_counts(compare,sort=True).sort_index()
print(count_admitted)
count_admitted.plot(kind='bar')
#plt.show()


a=admit['GRE Score']
b=admit['TOEFL Score']
c=admit['University Rating']
d=admit['SOP']
e=admit['LOR']
f=admit['CGPA']
g=admit['Research']




























