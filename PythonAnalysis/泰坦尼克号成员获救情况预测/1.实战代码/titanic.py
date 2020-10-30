import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier


titanic = pd.read_csv("train.csv")
# print(titanic.head(5))
#
# print(titanic.info())



# fig = plt.figure(figsize=(15,10))
# fig.set(alpha=0.2)  # 设定图表颜色alpha参数
#
# plt.subplot2grid((2,3),(0,0))
# titanic.Survived.value_counts().plot(kind='bar')
# plt.title("获救情况 (1为获救)")
# plt.ylabel("人数")
#
# plt.subplot2grid((2,3),(0,1))
# titanic.Pclass.value_counts().plot(kind="bar")
# plt.ylabel("人数")
# plt.title("乘客等级分布")
#
# plt.subplot2grid((2,3),(0,2))
# plt.scatter(titanic.Survived, titanic.Age)
# plt.ylabel("年龄")
# plt.grid(b=True, which='major', axis='y')
# plt.title("按年龄看获救分布 (1为获救)")
#
#
# plt.subplot2grid((2,3),(1,0), colspan=2)
# titanic.Age[titanic.Pclass == 1].plot(kind='kde')
# titanic.Age[titanic.Pclass == 2].plot(kind='kde')
# titanic.Age[titanic.Pclass == 3].plot(kind='kde')
# plt.xlabel("年龄")
# plt.ylabel("密度")
# plt.title("各等级的乘客年龄分布")
# plt.legend(('头等舱', '2等舱','3等舱'),loc='best')
#
#
# plt.subplot2grid((2,3),(1,2))
# titanic.Embarked.value_counts().plot(kind='bar')
# plt.title("各登船口岸上船人数")
# plt.ylabel("人数")
# plt.show()

#乘客舱的等级的获救情况
# fig = plt.figure()
# fig.set(alpha=0.2)  # 设定图表颜色alpha参数
#
# Survived_0 = titanic.Pclass[titanic.Survived == 0].value_counts()
# Survived_1 = titanic.Pclass[titanic.Survived == 1].value_counts()
# df=pd.DataFrame({'获救':Survived_1, '未获救':Survived_0})
# df.plot(kind='bar', stacked=True)
# plt.title("各乘客等级的获救情况")
# plt.xlabel("乘客等级")
# plt.ylabel("人数")
#
# plt.show()

#看看各性别的获救情况
# fig = plt.figure()
# fig.set(alpha=0.2)  # 设定图表颜色alpha参数
#
# Survived_m = titanic.Survived[titanic.Sex == 'male'].value_counts()
# Survived_f = titanic.Survived[titanic.Sex == 'female'].value_counts()
# df=pd.DataFrame({u'男性':Survived_m, u'女性':Survived_f})
# df.plot(kind='bar', stacked=True)
# plt.title(u"按性别看获救情况")
# plt.xlabel(u"性别")
# plt.ylabel(u"人数")
# plt.show()



# # 各种舱级别情况下各性别的获救情况
# fig=plt.figure(figsize=(15,10))
# fig.set(alpha=0.65) # 设置图像透明度，无所谓
# plt.title(u"根据舱等级和性别的获救情况")
#
# ax1=fig.add_subplot(141)
# titanic.Survived[titanic.Sex == 'female'][titanic.Pclass != 3].value_counts().plot(kind='bar', label="female highclass", color='#FA2479')
# ax1.set_xticklabels([u"获救", u"未获救"], rotation=0)
# ax1.legend([u"女性/高级舱"], loc='best')
#
# ax2=fig.add_subplot(142, sharey=ax1)
# titanic.Survived[titanic.Sex == 'female'][titanic.Pclass == 3].value_counts().plot(kind='bar', label='female, low class', color='pink')
# ax2.set_xticklabels([u"未获救", u"获救"], rotation=0)
# plt.legend([u"女性/低级舱"], loc='best')
#
# ax3=fig.add_subplot(143, sharey=ax1)
# titanic.Survived[titanic.Sex == 'male'][titanic.Pclass != 3].value_counts().plot(kind='bar', label='male, high class',color='lightblue')
# ax3.set_xticklabels([u"未获救", u"获救"], rotation=0)
# plt.legend([u"男性/高级舱"], loc='best')
#
# ax4=fig.add_subplot(144, sharey=ax1)
# titanic.Survived[titanic.Sex == 'male'][titanic.Pclass == 3].value_counts().plot(kind='bar', label='male low class', color='steelblue')
# ax4.set_xticklabels([u"未获救", u"获救"], rotation=0)
# plt.legend([u"男性/低级舱"], loc='best')
#
# plt.show()

# #看看各登录港口的获救情况
# fig = plt.figure()
# fig.set(alpha=0.2)  # 设定图表颜色alpha参数
#
# Survived_0 = titanic.Embarked[titanic.Survived == 0].value_counts()
# Survived_1 = titanic.Embarked[titanic.Survived == 1].value_counts()
# df=pd.DataFrame({'获救':Survived_1, '未获救':Survived_0})
# df.plot(kind='bar', stacked=True)
# plt.title("各登录港口乘客的获救情况")
# plt.xlabel("登录港口")
# plt.ylabel("人数")
#
# plt.show()


### 使用 RandomForestClassifier 填补缺失的年龄属性
def set_missing_ages(df):
    # 把已有的数值型特征取出来丢进Random Forest Regressor中
    age_df = df[['Age', 'Fare', 'Parch', 'SibSp', 'Pclass']]

    # 乘客分成已知年龄和未知年龄两部分
    known_age = age_df[age_df.Age.notnull()].as_matrix()
    unknown_age = age_df[age_df.Age.isnull()].as_matrix()

    # y即目标年龄
    y = known_age[:, 0]

    # X即特征属性值
    X = known_age[:, 1:]

    # fit到RandomForestRegressor之中
    rfr = RandomForestRegressor(random_state=0, n_estimators=2000, n_jobs=-1)
    rfr.fit(X, y)

    # 用得到的模型进行未知年龄结果预测
    predictedAges = rfr.predict(unknown_age[:, 1::])

    # 用得到的预测结果填补原缺失数据
    df.loc[(df.Age.isnull()), 'Age'] = predictedAges

    return df

titanic = set_missing_ages(titanic)

dummies_Embarked = pd.get_dummies(titanic['Embarked'], prefix= 'Embarked')
dummies_Sex = pd.get_dummies(titanic['Sex'], prefix= 'Sex')
dummies_Pclass = pd.get_dummies(titanic['Pclass'], prefix= 'Pclass')

df = pd.concat([titanic, dummies_Embarked, dummies_Sex, dummies_Pclass], axis=1)
df.drop(['Pclass', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)

# print(df)

# 将数据的Label分离出来
train_label = df['Survived']
train_titanic = df.drop('Survived', 1)

# 对数据进行模型预测
alg = RandomForestClassifier(random_state=1, n_estimators=10, min_samples_split=2, min_samples_leaf=1)
kf = model_selection.KFold(n_splits=3,shuffle=False, random_state=None)
scores = model_selection.cross_val_score(alg, train_titanic, train_label, cv=kf)

# # print(scores.mean())


# 导入测试集的数据，并将数据和测试集上的数据进行一样的处理
titanic_test = pd.read_csv("test.csv")
titanic_test = set_missing_ages(titanic_test)
dummies_Embarked = pd.get_dummies(titanic_test['Embarked'], prefix= 'Embarked')
dummies_Sex = pd.get_dummies(titanic_test['Sex'], prefix= 'Sex')
dummies_Pclass = pd.get_dummies(titanic_test['Pclass'], prefix= 'Pclass')
df_test = pd.concat([titanic_test,dummies_Embarked, dummies_Sex, dummies_Pclass], axis=1)
df_test.drop(['Pclass', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)


# 先用训练集上的数据训练处一个模型，再在测试集上进行预测，并将结果输出到一个csv文件中
model = RandomForestClassifier(random_state=1, n_estimators=10, min_samples_split=2, min_samples_leaf=1)
model.fit(train_titanic, train_label)
predictions = model.predict(df_test)
result = pd.DataFrame({'PassengerId':titanic_test['PassengerId'].as_matrix(), 'Survived':predictions.astype(np.int32)})
result.to_csv("random_forest_predictions.csv", index=False)
print(pd.read_csv("random_forest_predictions.csv"))