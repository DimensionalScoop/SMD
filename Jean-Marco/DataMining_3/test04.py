import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

from sklearn.feature_selection import mutual_info_regression
pd.set_option('display.max_rows', 1000)


ALPHA = 0.2

train = pd.read_csv('train_new.csv')
test = pd.read_csv('test_new.csv')

train_val = np.matrix(train)
x = train_val[:, 0:-1]
y = train_val[:, -1]

names = list(train)[0:-1]

stats = mutual_info_regression(x,y)

x_selected = x[:, stats>ALPHA]


best_alpha = 0.00099

reg = linear_model.Lasso(alpha=best_alpha, max_iter=50000)

#reg = linear_model.RidgeCV(alphas=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],cv=5, gcv_mode ='auto')
reg.fit(x_selected,y)



#print(reg.coef_[-1].shape)
#print(list(train)[1:-1])

#print(np.transpose(list(train))[stats>ALPHA])
coef_set = pd.Series(reg.coef_[-1], index = np.transpose(names)[stats>ALPHA])
print(coef_set.sort_values())

preds = reg.predict(x_selected)
print(np.max(preds))
#print(np.transpose(list(train))[ALPHA>0.2])
#print(np.transpose(coef_set)[ALPHA>0.2])




#test_val = np.matrix(test)
#x_test = test_val[:, 1:]
#pred = reg.predict(x_test)
#print(np.mean(pred))
