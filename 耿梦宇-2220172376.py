# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 21:02:04 2019

@author: Administrator
"""

#一、提取数据
import pandas as pd
data=pd.read_csv('./4s.csv',index_col=u'纳税人编号')
#二、数据探索分析
import matplotlib.pyplot as plt#导入
import matplotlib as mpl
fig,axes=plt.subplots(1,2)#创建画布
fig.set_size_inches(20,6)#设置画布大小
ax0,ax1=axes.flat#flat是数组的迭代器
mpl.rcParams['font.sans-serif']=[u'simHei']
mpl.rcParams['axes.unicode_minus']=False
data[u'销售类型'].value_counts().plot(kind='barh',ax=ax0,title=u'销售类型分布情况')
data[u'销售模式'].value_counts().plot(kind='barh',ax=ax1,title=u'销售模式分布情况')
data.describe().T#对数据变量进行可视化展示
plt.show()#输出结果

#三、数据预处理

data[u'输出']=pd.Categorical(data[u'输出']).codes
data[u'销售类型']=pd.Categorical(data[u'销售类型']).codes
data[u'销售模式']=pd.Categorical(data[u'销售模式']).codes

#数据划分
from sklearn.model_selection import train_test_split
data=data.as_matrix()
train_x,test_x,train_y,test_y=train_test_split(data[:,:14],data[:,14],test_size=0.2,random_state=1)

#构建LM神经网络模型
from keras.models import Sequential#导入神经网络的初始函数
from keras.layers.core import Dense,Activation
net_file='net.model'
net=Sequential()#建立神经网络模型
net.add(Dense(input_dim=14,output_dim=10))
net.add(Activation('relu'))
net.add(Dense(input_dim=10,output_dim=1))
net.add(Activation('sigmoid'))
net.compile(loss='binary_crossentropy',optimizer='adam')
net.fit(train_x,train_y,nb_epoch=1000,batch_size=10)#每次训练10个样本
net.save_weights(net_file)#保存模型
predict_result=net.predict_classes(train_x).reshape(len(train_x))#预测结果


from cm_plot import cm_plot
cm_plot(train_y,predict_result).show()#混淆矩阵显示
#构建决策树模型
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
tree_file = "tree.pkl"
tree = DecisionTreeClassifier(criterion = "entropy",max_depth =3)
tree.fit(train_x,train_y)
joblib.dump(tree,tree_file)
cm_plot(train_y,tree.predict(train_x)).show()

# 模型评价
# 绘制LM神经网络模型的ROC曲线
from sklearn.metrics import roc_curve  # 导入ROC曲线函数
predict_result = net.predict(test_x).reshape(len(test_x))  # 预测结果
fpr, tpr, thresholds = roc_curve(test_y, predict_result, pos_label=1)

plt.plot(fpr, tpr, linewidth=2, label='ROC of LM')  # 绘制ROC曲线
plt.xlabel('False Positive Rate')  # 坐标轴标签
plt.ylabel('True POstive Rate')
plt.xlim(0, 1.05)  # 设定边界范围
plt.ylim(0, 1.05)
plt.legend(loc=4)  # 设定图例位置
plt.show()  # 显示绘图结果

# 绘制决策树模型的ROC曲线
fpr, tpr, thresholds = roc_curve(test_y, tree.predict_proba(test_x)[:,1], pos_label=1)

plt.plot(fpr, tpr, linewidth=2, label='ROC of CHAR')  # 绘制ROC曲线
plt.xlabel('False Positve Rate')  # 坐标轴标签
plt.ylabel('True Postive Rate')
plt.xlim(0, 1.05)  # 设定边界范围
plt.ylim(0, 1.05)
plt.legend(loc=4)  # 设定图例位置
plt.show()  # 显示绘图结果








