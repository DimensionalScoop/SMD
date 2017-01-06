import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

from sklearn.feature_selection import mutual_info_regression
pd.set_option('display.max_rows', 1000)

ALPHA = 0.03

train = pd.read_csv('train_new.csv')
test = pd.read_csv('test_new.csv')

train_val = np.matrix(train)
x = train_val[:, :-1]
y = train_val[:, -1]

names = list(train)[0:-1]


stats = mutual_info_regression(x,y)

x_selected = x[:, stats>ALPHA]

reg = linear_model.LinearRegression()
reg.fit(x_selected,np.log1p(y))



#print(reg.coef_[-1].shape)
#print(list(train)[1:-1])

coef_set = pd.Series(reg.coef_[-1], index = np.transpose(names)[stats>ALPHA])
print(coef_set.sort_values())



preds = reg.predict(x_selected)
print(np.min(np.exp(preds)-1))


test_val = np.matrix(test)
x_test = test_val[:, :]
x_test_selected = x_test[:, stats>ALPHA]
pred = reg.predict(x_test_selected)
finalres = np.exp(pred)-1
ids = np.array(range(1461, 2920))

np.savetxt("pred_linear_alpha2.csv", np.column_stack((ids,finalres)), delimiter=",", header="Id,SalePrice", comments='')
