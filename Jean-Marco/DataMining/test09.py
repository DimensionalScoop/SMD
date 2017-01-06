import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# This process will do the pregiven tasks from the Übungsblatt

#  train.columns.get_loc("SalePrice")
# list(train)[37]

# import data made by test00.py
train = pd.read_csv('train_new_log.csv')

#######

sets = np.transpose(train.values)
corrvalues = np.corrcoef(sets)[-1]
corr_set = pd.Series(corrvalues, index = list(train))
print(corr_set.sort_values())

SalePrice = train['SalePrice']
OverallQual = train['OverallQual']
GrLivArea = train['GrLivArea']
GarageCars = train['GarageCars']

SalePrice_v = np.transpose(np.matrix(SalePrice))
OverallQual_v = np.transpose(np.matrix(OverallQual))
GrLivArea_v = np.transpose(np.matrix(GrLivArea))
# Fitty

regr_OverallQual = linear_model.LinearRegression()
regr_OverallQual.fit( OverallQual_v, SalePrice_v)
regr_GrLivArea = linear_model.LinearRegression()
regr_GrLivArea.fit(GrLivArea_v, SalePrice_v)

plt.ylabel('Sale Price')
plt.xlabel('Overall Quality')
plt.plot(OverallQual, SalePrice, 'b.', markersize=2)
plt.plot(OverallQual_v, regr_OverallQual.predict(OverallQual_v))
plt.savefig('overall_qual.pdf')
plt.clf()

plt.ylabel('Sale Price')
plt.xlabel('Ground Living Area')
plt.plot(GrLivArea, SalePrice, 'b.', markersize=2)
plt.plot(GrLivArea_v, regr_GrLivArea.predict(GrLivArea_v))
plt.savefig('GrLivArea.pdf')
plt.clf()

plt.ylabel('Sale Price')
plt.xlabel('Garage Caes')
plt.plot(GarageCars, SalePrice, 'b.',markersize=2)
plt.savefig('garage_cars.pdf')
plt.clf()

# Differences in Prices

diff_OverallQual = np.abs(np.exp(regr_OverallQual.predict(OverallQual_v)) - np.exp(SalePrice_v))
diff_GrLivArea = np.abs(np.exp(regr_GrLivArea.predict(GrLivArea_v)) - np.exp(SalePrice_v))
print(np.mean(diff_OverallQual))
print(np.mean(diff_GrLivArea))

plt.xlabel('Abweichung im SalePrice')
plt.hist(diff_OverallQual, bins=20)
plt.savefig('overall_qual_hist.pdf')
plt.clf()

plt.xlabel('Abweichung im SalePrice')
plt.hist(diff_GrLivArea, bins=20)
plt.savefig('grlivarea_hist.pdf')
plt.clf()
