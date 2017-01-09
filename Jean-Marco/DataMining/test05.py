import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neural_network

K = 30

train = pd.read_csv('train_new.csv')
test = pd.read_csv('test_new.csv')
test_val = np.matrix(test)
x_test = test_val[:, 1:]

train_val = np.matrix(train)
x = train_val[:, 1:-1]
y = train_val[:, -1]
y = np.ravel(y)

corrvalues = abs(np.corrcoef(x.T, y.T)[-1, :-1])

biggest_index = np.argsort(corrvalues)[-K:] # index     of k best params

x_selected = x[:, biggest_index]

reg = neural_network.MLPRegressor(max_iter=2000)
reg.fit(x_selected,y)
x_test_selected = x_test[:, biggest_index]
pred = reg.predict(x_test_selected)


ids = np.array(range(1461, 2920))
np.savetxt("pred_neural.csv", np.column_stack((ids,pred)), delimiter=",", header="Id,SalePrice", comments='')