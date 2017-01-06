import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# This script will handle the test data the same way the other test data was handled

##### PREPROCESSING GIVEN DATA

train_orig = pd.read_csv('test.csv')
train_filled = train_orig.fillna(train_orig.mean()) # fill nans with average
#observations: numeriacal NAN's are replaced with average, non-nomerical are casted to dummy variables, but no dummy variable is created for NA and add corersponding dummy variables for this attributes are 0 (for example: Alley=NA, MasVnrType)

train = pd.get_dummies(train_filled) #cast all non-numericals to dummy variables


train['Utilities_NoSeWa'] = 0
train['Condition2_RRAe'] = 0
train['Condition2_RRAn'] = 0
train['Condition2_RRNn'] = 0
train['HouseStyle_2.5Fin'] = 0
train['RoofMatl_Membran'] = 0
train['RoofMatl_Metal'] = 0
train['RoofMatl_Roll'] = 0
train['RoofMatl_ClyTile'] = 0
train['Heating_Floor'] = 0
train['Heating_OthW'] = 0
train['Electrical_Mix'] = 0
train['GarageQual_Ex'] = 0
train['PoolQC_Fa'] = 0
train['MiscFeature_TenC'] = 0
#train['Utilities_ELO'] = 0
#train['Utilities_NoSeWa'] = 0

train['Exterior1st_ImStucc'] = 0
train['Exterior1st_Stone'] = 0
train['Exterior2nd_Other'] = 0




#Exterior: Combine 1st and 2nd

train['ExAsbShng'] = train[ ["Exterior1st_AsbShng" , "Exterior2nd_AsbShng"]].max(axis=1)
del train['Exterior1st_AsbShng']
del train['Exterior2nd_AsbShng']

train['AsphShn'] = train[ ["Exterior1st_AsphShn" , "Exterior2nd_AsphShn"]].max(axis=1)
del train['Exterior1st_AsphShn']
del train['Exterior2nd_AsphShn']

train['ExBrkComm'] = train[["Exterior1st_BrkComm" , "Exterior2nd_Brk Cmn"]].max(axis=1)
del train['Exterior1st_BrkComm']
del train['Exterior2nd_Brk Cmn']

train['ExBrkFace'] = train[["Exterior1st_BrkFace" , "Exterior2nd_BrkFace"]].max(axis=1)
del train['Exterior1st_BrkFace']
del train['Exterior2nd_BrkFace']

train['ExCBlock'] = train[["Exterior1st_CBlock" , "Exterior2nd_CBlock"]].max(axis=1)
del train['Exterior1st_CBlock']
del train['Exterior2nd_CBlock']

train['ExCemntBd'] = train[["Exterior1st_CemntBd" , "Exterior2nd_CmentBd"]].max(axis=1)
del train['Exterior1st_CemntBd']
del train['Exterior2nd_CmentBd']

train['ExHdBoard'] = train[["Exterior1st_HdBoard" , "Exterior2nd_HdBoard"]].max(axis=1)
del train['Exterior1st_HdBoard']
del train['Exterior2nd_HdBoard']

train['ExImStucc'] = train[["Exterior1st_ImStucc" , "Exterior2nd_ImStucc"]].max(axis=1)
del train['Exterior1st_ImStucc']
del train['Exterior2nd_ImStucc']

train['ExMetalSd'] = train[["Exterior1st_MetalSd" , "Exterior2nd_MetalSd"]].max(axis=1)
del train['Exterior1st_MetalSd']
del train['Exterior2nd_MetalSd']

train['ExPlywood'] = train[["Exterior1st_Plywood" , "Exterior2nd_Plywood"]].max(axis=1)
del train['Exterior1st_Plywood']
del train['Exterior2nd_Plywood']

train['ExStone'] = train[["Exterior1st_Stone" , "Exterior2nd_Stone"]].max(axis=1)
del train['Exterior1st_Stone']
del train['Exterior2nd_Stone']

train['ExStucco'] = train[["Exterior1st_Stucco" , "Exterior2nd_Stucco"]].max(axis=1)
del train['Exterior1st_Stucco']
del train['Exterior2nd_Stucco']

train['ExVinylSd'] = train[["Exterior1st_VinylSd" , "Exterior2nd_VinylSd"]].max(axis=1)
del train['Exterior1st_VinylSd']
del train['Exterior2nd_VinylSd']

train['ExWdSdng'] = train[["Exterior1st_Wd Sdng" , "Exterior2nd_Wd Sdng"]].max(axis=1)
del train['Exterior1st_Wd Sdng']
del train['Exterior2nd_Wd Sdng']

train['ExWdShng'] = train[["Exterior1st_WdShing" , "Exterior2nd_Wd Shng"]].max(axis=1)
del train['Exterior1st_WdShing']
del train['Exterior2nd_Wd Shng']


#No Garage -> GarageYearBuilt = NaN -> GarageYearBuil is replaced by average year. Not sure if this is the best way to handle this

#remove useless dummy variables (for example: CentralAir= Y/N). 100% correlated obvsly
del train['CentralAir_N']

# Sortieren... nach Buchstaben, wieso nicht?

train.reindex_axis(sorted(train.columns), axis=1)

print(list(train))

train.to_csv('test_new.csv', index=False) # new data!
