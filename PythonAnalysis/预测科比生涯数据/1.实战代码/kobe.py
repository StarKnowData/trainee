import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.ensemble import RandomForestClassifier  #导入随机森林分类器
from sklearn.cross_validation import KFold
from sklearn.metrics import log_loss

# 导入数据
filename = "data.csv"
raw = pd.read_csv(filename)
# print(raw.shape)
# print(raw.head())  #head函数打印前5行，如果需要打印前10行，这样写print(raw.head(10))


# 删除shot_made_flag为空的数据项，并且命名为kobe用作训练
kobe = raw[pd.notnull(raw['shot_made_flag'])]
# print(kobe.shape)


# #画散点图用来分析lat loc_x  loc_y lon这4个标签
# alpha = 0.02   #指定一个数字，用于后面的透明度
# plt.figure(figsize=(6,6))  #指定画图域
# # loc_x and loc_y
# plt.subplot(121)    #一行两列   第一个位置
# plt.scatter(kobe.loc_x, kobe.loc_y, color='R', alpha=alpha)   #画散点图
# plt.title('loc_x and loc_y')
# # lat and lon
# plt.subplot(122)    #一行两列   第二个位置
# plt.scatter(kobe.lon, kobe.lat, color='B', alpha=alpha)
# plt.title('lat and lon')
# # plt.show()


#对于lat，loc_x，loc_y，lon这4个标签，我们取loc_x和loc_y这2个标签，并将其转化为极坐标的形式
#dist表示离篮筐的距离，angle表示投篮的角度，这样将会更好的科比投篮的反应结果`
raw['dist'] = np.sqrt(raw['loc_x']**2 + raw['loc_y']**2)
loc_x_zero = raw['loc_x'] == 0
raw['angle'] = np.array([0]*len(raw))
raw['angle'][~loc_x_zero] = np.arctan(raw['loc_y'][~loc_x_zero] / raw['loc_x'][~loc_x_zero])
raw['angle'][loc_x_zero] = np.pi / 2


#画图展示dist和shot_distance的正相关性
plt.figure(figsize=(5,5))
plt.scatter(raw.dist, raw.shot_distance, color='blue')
plt.title('dist and shot_distance')
# plt.show()


# 对于minutes_remaining：离比赛结束还有多少分钟；seconds_remaining：离比赛结束还有多少秒（0-60），这
# 2个属性我们合成距离比赛结束的时间
raw['remaining_time'] = raw['minutes_remaining'] * 60 + raw['seconds_remaining']


# 机器学习只能识别数值型的数据
# 将赛季中'Jan-00' 'Feb-01' 'Mar-02'  ···  '1998-99'转换成
# 0  1  2  ··· 99
# print(raw['season'].unique())
raw['season'] = raw['season'].apply(lambda x: int(x.split('-')[1]) )
# print(raw['season'].unique())

# 先保存一下shot_id,为接下来的创建result.csv做准备
test_shot_id = raw[pd.isnull(raw['shot_made_flag'])]

#删除对于比赛结果没有影响的数据
drops = ['shot_id', 'team_id', 'team_name', 'shot_zone_area', 'shot_zone_range', 'shot_zone_basic','matchup', 'lon',
         'lat', 'seconds_remaining', 'minutes_remaining','shot_distance', 'loc_x', 'loc_y', 'game_event_id', 'game_id',
         'game_date']
for drop in drops:
    raw = raw.drop(drop, 1)


#将非数值型的数据转换成为onehot编码的格式，加入到数据中并且将原来的数据删除
categorical_vars = ['action_type', 'combined_shot_type', 'shot_type', 'opponent', 'period', 'season']
for var in categorical_vars:
    raw = pd.concat([raw, pd.get_dummies(raw[var], prefix=var)], 1)
    raw = raw.drop(var, 1)
# print(raw)


#将数据分为训练集和测试集
train_kobe = raw[pd.notnull(raw['shot_made_flag'])]
train_label = train_kobe['shot_made_flag']
train_kobe = train_kobe.drop('shot_made_flag', 1)

test_kobe = raw[pd.isnull(raw['shot_made_flag'])]
test_kobe = test_kobe.drop('shot_made_flag', 1)



# print('寻找随机森林分类器的的最佳树的数量...')
# min_score = 100000
# best_n = 0
# scores_n = []
# range_n = np.logspace(0, 2, num=10).astype(int)
# for n in range_n:
#     print('树的数量 : {0}'.format(n))
#     t1 = time.time()
#     rfc_score = 0.
#     rfc = RandomForestClassifier(n_estimators=n)
#     for train_k, test_k in KFold(len(train_kobe), n_folds=10, shuffle=True):
#         rfc.fit(train_kobe.iloc[train_k], train_label.iloc[train_k])
#         pred = rfc.predict(train_kobe.iloc[test_k])
#         rfc_score += log_loss(train_label.iloc[test_k], pred) / 10
#     scores_n.append(rfc_score)
#     if rfc_score < min_score:
#         min_score = rfc_score
#         best_n = n
#     t2 = time.time()
#     print('建造 {0} 颗树(耗时{1:.3f}秒)'.format(n, t2 - t1))
# # print(best_n, min_score)
# print("最佳树的颗树为 : {0},得分为: {1}".format(best_n,min_score))
#
# print('\n')
#
# print('寻找随机森林分类器的最佳树的最佳深度...')
# min_score = 100000
# best_m = 0
# scores_m = []
# range_m = np.logspace(0, 2, num=10).astype(int)
# for m in range_m:
#     print("树的最大的深度 : {0}".format(m))
#     t1 = time.time()
#     rfc_score = 0.
#     rfc = RandomForestClassifier(max_depth=m, n_estimators=best_n)
#     for train_k, test_k in KFold(len(train_kobe), n_folds=10, shuffle=True):
#         rfc.fit(train_kobe.iloc[train_k], train_label.iloc[train_k])
#         pred = rfc.predict(train_kobe.iloc[test_k])
#         rfc_score += log_loss(train_label.iloc[test_k], pred) / 10
#     scores_m.append(rfc_score)
#     if rfc_score < min_score:
#         min_score = rfc_score
#         best_m = m
#     t2 = time.time()
#     print('树的最大深度为: {0}(耗时{1:.3f}秒)'.format(m, t2 - t1))
# print('最佳树的深度: {0},得分为：{1}'.format(best_m, min_score))

# plt.figure(figsize=(10,5))
# plt.subplot(121)
# plt.plot(range_n, scores_n)
# plt.ylabel('score')
# plt.xlabel('number of trees')
#
# plt.subplot(122)
# plt.plot(range_m, scores_m)
# plt.ylabel('score')
# plt.xlabel('max depth')
# plt.show()

model = RandomForestClassifier(n_estimators=100, max_depth=12)
model.fit(train_kobe, train_label)


predictions = model.predict(test_kobe)
result = pd.DataFrame({'shot_id':test_shot_id['shot_id'].as_matrix(), 'shot_made_flag':predictions.astype(np.int32)})
result.to_csv("result.csv", index=False)

print(pd.read_csv("result.csv"))
