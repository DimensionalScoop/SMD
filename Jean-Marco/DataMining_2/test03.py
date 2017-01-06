import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import cross_val_score

train = pd.read_csv('train_new.csv')
real = pd.read_csv('test_new.csv')

train_val = np.matrix(train)
x = train_val[:, 1:-1]
y = train_val[:, -1]

#x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.4, random_state=0)

#print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)


reg = linear_model.Ridge()
#reg.fit(x,y)

scores = cross_val_score(reg, x, y, cv=5, scoring="neg_mean_squared_error")

print(np.mean(scores), np.std(scores))
print(scores)

#real_val = np.matrix(real)
#x_real = real_val[:, 1:]
#pred = np.exp(reg.predict(x_real))-1
#print(np.mean(pred))
#
