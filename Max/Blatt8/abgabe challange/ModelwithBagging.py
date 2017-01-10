
# coding: utf-8

# In[122]:

import sklearn as sk
import sklearn.covariance as cov
import pandas as pd
import numpy as np
from ggplot import *

train_original = pd.DataFrame.from_csv("cleaned_train.csv")
data = train_original.copy()

apply_price_log = True
log_method = np.log
exp_method = np.exp
if apply_price_log:
    data['SalePrice'] = (data['SalePrice']).map(log_method) #'LOGLOGLO'

train = data.as_matrix()
names = data.columns


# In[123]:

# Drop features with low variance
import sklearn.feature_selection as sel

thredsh = sel.VarianceThreshold(threshold=0.0) # comparing with plots  0.003 seems to be a good threshold; no it doesn't. dont do it
thredsh.fit(train)
deselected = ~thredsh.get_support()
data = data.drop(names[deselected],axis=1)

# regenerate matrix
train = data.as_matrix()
names = data.columns


# In[124]:

import sklearn.preprocessing as pre

# scale all
scaler = pre.RobustScaler()# StandardScaler sucks
train = scaler.fit_transform(train)


# In[125]:

# Split the data
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

labels = train[:,0]
features = train[:,1:]


# In[126]:

# We learned: neural networks suck balls at predicting house prices. Don't use your brain when buing a house. As you tree.


# In[127]:

from sklearn import ensemble

bag_contents = ensemble.GradientBoostingRegressor(
    n_estimators=1800,max_leaf_nodes=15,learning_rate=0.005, random_state=1337, loss='ls')

bag = ensemble.BaggingRegressor(base_estimator=bag_contents, n_jobs=4, random_state=1337)

#scores = cross_val_score(fitter,features,labels,cv=2,scoring='neg_mean_squared_error',n_jobs=4)
#print("RMSE: %0.5f (+/- %0.5f)" % (scores.mean(), scores.std() * 2))


# In[128]:

bag.fit(features,labels)


# In[129]:

#'neg_mean_squared_error'
#from sklearn.metrics import mean_squared_error
#mean_squared_error(y_test,bag.predict(x_test))


# In[130]:

#importance = bag.feature_importances_
#sort = np.argsort(importance)[::-1]
#list(zip(importance[sort],names[1:][sort]))


# In[131]:

to_predict = pd.DataFrame.from_csv("cleaned_test.csv")
# apply transformations
to_predict = to_predict.drop(train_original.columns[deselected],axis=1)
to_predict_matrix = to_predict.as_matrix()
to_predict_matrix = scaler.transform(to_predict_matrix)


# In[132]:

features = to_predict_matrix[:,1:]
labels = bag.predict(features)
prices = scaler.inverse_transform(np.insert(features,0,labels,axis=1))


# In[133]:

to_predict['SalePrice'] = prices
if apply_price_log:
    to_predict['SalePrice'] = (to_predict['SalePrice']).map(exp_method)
to_predict[['SalePrice']].to_csv("submission.csv")

