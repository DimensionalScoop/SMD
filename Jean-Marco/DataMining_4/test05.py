import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


from sklearn.linear_model import Ridge, RidgeCV, ElasticNet, LassoCV, LassoLarsCV
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import mutual_info_regression
pd.set_option('display.max_rows', 1000)

ALPHA = 0.1

train = pd.read_csv('train_new.csv')
test = pd.read_csv('test_new.csv')

train_val = np.matrix(train)
x = train_val[:, :-1]
y = train_val[:, -1]

names = list(train)[0:-1]


stats = mutual_info_regression(x,y)

x_selected = x[:, stats>ALPHA]

def rmse_cv(model):
    rmse= np.sqrt(-cross_val_score(model, x_selected, y, scoring="neg_mean_squared_error", cv = 5))
    return(rmse)

model_ridge = LassoCV()



alphas = [0.05, 0.1, 0.3, 1, 3, 5, 10, 15, 30, 50, 75]
cv_ridge = [rmse_cv(LassoCV(alphas = alpha)).mean()
            for alpha in alphas]



cv_ridge = pd.Series(cv_ridge, index = alphas)
cv_ridge.plot(title = "Validation - Just Do It")
plt.xlabel("alpha")
plt.ylabel("rmse")

plt.show()




#reg = linear_model.LinearRegression()
#reg.fit(x,y)
#
#test_val = np.matrix(test)
#x_test = test_val[:, 1:]
#pred = reg.predict(x_test)
#print(np.mean(pred))
