import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import Ridge, RidgeCV, ElasticNet, LassoCV, LassoLarsCV
from sklearn.model_selection import cross_val_score

# This process will do the pregiven tasks from the Übungsblatt

#  train.columns.get_loc("SalePrice")
# list(train)[37]

# import data made by test00.py
train = pd.read_csv('train_new_log.csv')
test = pd.read_csv('test_new.csv')

train_val = np.matrix(train)
x = train_val[:, 1:-1]
y = train_val[:, -1]

#alpha = 13

reg = Ridge(alpha=13.0, normalize=True)
reg.fit(x,y)

test_val = np.matrix(test)
x_test = test_val[:, 1:]
pred = np.exp(reg.predict(x_test))+1
print(np.mean(pred))

ids = np.array(range(1461, 2920))

np.savetxt("pred_ridge_test_copycat2.csv", np.column_stack((ids,pred)), delimiter=",", header="Id,SalePrice", comments='')
