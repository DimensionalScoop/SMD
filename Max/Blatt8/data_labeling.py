import numpy as np
import pandas as pd
from sklearn import preprocessing as pre
from DataFrameImputer import DataFrameImputer

# Reduce labels to numericals


def ascending(set, na=None):
    types = zip(set, range(1, len(set) + 1))

    if na != None:  # if there is a 'not appllicable' classification, generate an array with a 'has' and 'label' quality
        types = map(lambda x: [x[0], 1, x[1]], types)
        types.append([na, 0, 0])

    return dict(types)


unneccessary = ['TotalBsmtSF', 'TotRmsAbvGrd']

special = ['MoSold', 'YrSold', 'SalePrice']

already_numerical = ['LotFrontage', 'LotArea', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea',
                     'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'Bedroom', 'Kitchen', 'TotRmsAbvGrd', 'Fireplaces', 'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF',
                     'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal']

default = ['Ex', 'Gd', 'TA', 'Fa', 'Po']

ordered = {
    'LandContour': ['Low', 'Lvl', 'Bnk', 'HLS'],
    'Utilities': ['AllPub', 'NoSewr', 'NoSeWa', 'ELO'],
    'LandSlope': ['Gtl', 'Mod', 'Sev'],
    'ExterQual': default,
    'ExterCond': default,
    'BsmtQual': default,  # has an NA
    'BsmtCond': default,  # has an NA
    'BsmtExposure': ['Gd', 'Av', 'Mn', 'No'],  # has an NA
    'BsmtFinType1': ['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf'],  # NA
    'BsmtFinType2': ['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf'],
    'HeatingQC': default,
    'KitchenQual': default,
    'Functional': ['Typ', 'Min1', 'Min2', 'Mod', 'Maj1', 'Maj2', 'Sev', 'Sal'],
    'FireplaceQu': default,  # NA
    'GarageFinish': ['Fin', 'RFn', 'Unf'],  # NA
    'GarageQual': default,  # NA
    'GarageCond': default,  # NA
    'PavedDrive': ['Y', 'P', 'N'],
    'PoolQC': default,  # NA
    'Fence': ['GdPrv', 'MnPrv', 'GdWo', 'MnWw', 'NA'],
}

unordered = ['MSSubClass', 'MSZoning', 'Street', 'Alley', 'LotShape', 'LotConfig', 'OverallQual', 'OverallCond',

             'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle',
             'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType',
             'Foundation', 'Heating', 'CentralAir', 'Electrical', 'GarageType', 'MiscFeature', 'SaleType', 'SaleCondition'
             ]


train_original = pd.DataFrame.from_csv("train.csv")
train_cleaned = DataFrameImputer().fit_transform(train_original)
data = pd.DataFrame()

# check for all colummns
all_colummns = set(unneccessary + special + already_numerical + list(ordered.keys()) + unordered)
# print(all_colummns.intersection(train_cleaned.colummns))

# Special:


# Ordered data

# index = 0
# while index < len(train[0]):
#     if isinstance(train[:, index], str):  # if attribute is string
#         le = pre.LabelBinarizer()
#         flags = le.fit_transform(train[:, index])
#         train = np.insert(train, index, flags)
