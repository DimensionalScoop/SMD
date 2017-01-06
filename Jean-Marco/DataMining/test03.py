import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

train = pd.read_csv('train_new.csv')
test = pd.read_csv('test_new.csv')

train_val = np.matrix(train)
x = train_val[:, 1:-1]
y = train_val[:, -1]
reg = linear_model.LinearRegression()
reg.fit(x,y)

test_val = np.matrix(test)
x_test = test_val[:, 1:]
pred = reg.predict(x_test)
print(np.mean(pred))
