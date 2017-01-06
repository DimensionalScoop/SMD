import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

from sklearn.feature_selection import mutual_info_regression
pd.set_option('display.max_rows', 1000)


train = pd.read_csv('train_new.csv')
test = pd.read_csv('test_new.csv')

train_val = np.matrix(train)
x = train_val[:, 1:-1]
y = train_val[:, -1]

stats = mutual_info_regression(x,y)

x_selected = train_val[:, stats>0.2]

reg = linear_model.LinearRegression()
reg.fit(x,y)



#print(reg.coef_[-1].shape)
#print(list(train)[1:-1])

coef_set = pd.Series(reg.coef_[-1], index = list(train)[1:-1])
print(coef_set.sort_values())

print(np.transpose(list(train))[stats>0.2])
print(np.transpose(coef_set)[stats>0.2])




#test_val = np.matrix(test)
#x_test = test_val[:, 1:]
#pred = reg.predict(x_test)
#print(np.mean(pred))
