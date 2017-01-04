import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

K = 100

train = pd.read_csv('train_new.csv')
test = pd.read_csv('test_new.csv')
test_val = np.matrix(test)
x_test = test_val[:, 1:]

train_val = np.matrix(train)
x = train_val[:, 1:-1]
y = train_val[:, -1]


corrvalues = abs(np.corrcoef(x.T, y.T)[-1, :-1])

maxima = np.array([])
minima = np.array([])
means = np.array([])
k_id = np.array([])

chosen_preds = np.array([])

for K in range(1,170):

    biggest_index = np.argsort(corrvalues)[-K:] # index     of k best params

    x_selected = x[:, biggest_index]

    reg = linear_model.LinearRegression()
    reg.fit(x_selected,y)

    x_test_selected = x_test[:, biggest_index]
    pred = reg.predict(x_test_selected)
    means=np.append(means, np.mean(pred))
    minima=np.append(minima, np.min(pred))
    maxima=np.append(maxima, np.max(pred))
    k_id=np.append(k_id, K)

    if K==35:
        chosen_preds = reg.predict(x_test_selected)

plt.plot(k_id, maxima, label=r'Maxima')
plt.plot(k_id, minima, label=r'Minima')
plt.plot(k_id, means, label=r'Means')
plt.legend()
plt.savefig('linear_data.pdf')

print(chosen_preds)

ids = np.array(range(1461, 2920))
print(np.shape(ids))
print(np.shape(chosen_preds))
np.savetxt("pred_linear.csv", np.column_stack((ids,chosen_preds)), delimiter=",", header="Id,SalePrice", comments='')
