import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neural_network
from sklearn import preprocessing

K = 30

train = pd.read_csv('train_new.csv')
test = pd.read_csv('test_new.csv')
test_val = np.matrix(test)
x_test = test_val[:, 1:]
#x_test = preprocessing.normalize(x_test)

train_val = np.matrix(train)
x = train_val[:, 1:-1]
y = train_val[:, -1]

#x = preprocessing.normalize(x)

y = np.ravel(y)

corrvalues = abs(np.corrcoef(x.T, y.T)[-1, :-1])

biggest_index = np.argsort(corrvalues)[-K:] # index     of k best params

x_selected = x[:, biggest_index]

reg = neural_network.MLPRegressor(hidden_layer_sizes=(100, ), activation='relu', solver='adam', alpha=0.0001, batch_size='auto', learning_rate='constant', learning_rate_init=0.3, power_t=0.5, max_iter=500)
reg.fit(x_selected,y)
x_test_selected = x_test[:, biggest_index]
pred = reg.predict(x_test_selected)


ids = np.array(range(1461, 2920))
np.savetxt("pred_neural_06.csv", np.column_stack((ids,pred)), delimiter=",", header="Id,SalePrice", comments='')
