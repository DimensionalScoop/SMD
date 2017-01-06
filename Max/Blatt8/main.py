import sklearn as sk
import sklearn.covariance as cov
import pandas as pd
import numpy as np


import sklearn.preprocessing as pre
from DataFrameImputer import DataFrameImputer

train_original = pd.DataFrame.from_csv("train.csv")

train_cleaned = DataFrameImputer().fit_transform(train_original)

train = train_cleaned.as_matrix()


def label_set(set):
    names = train_cleaned.columns
    return dict(zip(names, set))


n_attributes = len(train[0])
sample_row = train[0]

data = np.zeros(len(train))

for i in range(n_attributes):
    if isinstance(sample_row[i], str):  # if attribute is string
        print(train[:, i], i)

        le = pre.LabelBinarizer()
        train = np.insert(train, i, le.fit_transform(train[:, i]))

    else:
        data.


imp = pre.Imputer(missing_values="NaN", strategy='most_frequent')
# imp.fit_transform(train)

# cov.empirical_covariance(train)
