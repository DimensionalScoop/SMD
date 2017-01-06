import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# This script will handle the test data the same way the other test data was handled

##### PREPROCESSING GIVEN DATA

train_orig = pd.read_csv('test.csv')


streetp = {None: 0, "NA": 1, "Grvl": 2, "Pave": 2}
train_orig["Alley"] = train_orig["Alley"].map(streetp).astype(int) #fill it before because most values are NA

hazpool = {None: 0, "NA": 0, "Fa": 1, "TA": 1, "Gd": 1, "Ex":1}
train_orig["PoolQC"] = train_orig["PoolQC"].map(hazpool).astype(int)


train_filled = train_orig.fillna(train_orig.mean()) # fill nans with average
#observations: numeriacal NAN's are replaced with average, non-nomerical are casted to dummy variables, but no dummy variable is created for NA and add corersponding dummy variables for this attributes are 0 (for example: Alley=NA, MasVnrType)




#Mapping

quality = {None: 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5}
train_filled["ExterQual"] = train_filled["ExterQual"].map(quality).astype(int)
train_filled["ExterCond"] = train_filled["ExterCond"].map(quality).astype(int)
train_filled["BsmtQual"] = train_filled["BsmtQual"].map(quality).astype(int)
train_filled["BsmtCond"] = train_filled["BsmtCond"].map(quality).astype(int)
train_filled["HeatingQC"] = train_filled["HeatingQC"].map(quality).astype(int)
train_filled["KitchenQual"] = train_filled["KitchenQual"].map(quality).astype(int)
train_filled["FireplaceQu"] = train_filled["FireplaceQu"].map(quality).astype(int)
train_filled["GarageQual"] = train_filled["GarageQual"].map(quality).astype(int)
train_filled["GarageCond"] = train_filled["GarageCond"].map(quality).astype(int)


bsmtex = {None: 0, "No": 0, "Mn": 1, "Av": 2, "Gd": 3}
train_filled["BsmtExposure"] = train_filled["BsmtExposure"].map(bsmtex).astype(int)

density = {None: 0, "C (all)": 3, "RL": 1, "RP": 1, "RM": 2, "RH": 3, "I": 3, "A": 1, "C": 3, "FV": 1}
train_filled["Density"] = train_filled["MSZoning"].map(density).astype(int)
del train_filled['MSZoning']

street = {None: 0, "Grvl": 1, "Pave": 2}
train_filled["Street"] = train_filled["Street"].map(street).astype(int)

lotshape = {None: 0, "Reg": 0, "IR1": 1, "IR2": 1, "IR3": 1}
train_filled["LotShape"] = train_filled["LotShape"].map(lotshape).astype(int)

landcont = {None: 0, "Lvl": 0, "Bnk": 1, "HLS": 1, "Low": 1}
train_filled["LandContour"] = train_filled["LandContour"].map(landcont).astype(int)

del train_filled['Utilities'] # traindata: only one attribute is different -> go away

lotconfig = {None: 0, "Inside": 0, "Corner": 1, "CulDSac": 1, "FR2": 1, "FR3": 1}
train_filled["LotConfig"] = train_filled["LotConfig"].map(lotconfig).astype(int)

landslope = {None: 0, "Gtl": 1, "Mod": 2, "Sev": 2}
train_filled["LandSlope"] = train_filled["LandSlope"].map(landslope).astype(int)


vgood_nb = {None: 0, "CollgCr": 0, "Veenker": 0, "Crawfor": 0, "NoRidge": 1, "Mitchel": 0, "Somerst":0, "NWAmes":0 , "OldTown":0, "BrkSide":0, "Sawyer":0, "NridgHt":1, "NAmes":0 , "SawyerW":0 , "IDOTRR":0, "MeadowV":0, "Edwards":0, "Timber":0, "Gilbert":0, "StoneBr":1 , "ClearCr":0, "NPkVill":0, "Blmngtn":0, "BrDale":0 , "SWISU":0, "Blueste":0}
train_filled["VeryGoodNbh"] = train_filled["Neighborhood"].map(vgood_nb).astype(int)
#>250.000 average
good_nb = {None: 0, "CollgCr": 0, "Veenker": 1, "Crawfor": 0, "NoRidge": 1, "Mitchel": 0, "Somerst":1, "NWAmes":0 , "OldTown":0, "BrkSide":0, "Sawyer":0, "NridgHt":1, "NAmes":0 , "SawyerW":0 , "IDOTRR":0, "MeadowV":0, "Edwards":0, "Timber":1, "Gilbert":0, "StoneBr":1 , "ClearCr":0, "NPkVill":0, "Blmngtn":0, "BrDale":0 , "SWISU":0, "Blueste":0}
train_filled["GoodNbh"] = train_filled["Neighborhood"].map(good_nb).astype(int)
#>225.000 average




dortmund_nordstadt = {None: 0, "CollgCr": 0, "Veenker": 0, "Crawfor": 0, "NoRidge": 0, "Mitchel": 0, "Somerst":0, "NWAmes":0 , "OldTown":1, "BrkSide":1, "Sawyer":1, "NridgHt":0, "NAmes":0 , "SawyerW":0 , "IDOTRR":1, "MeadowV":1, "Edwards":1, "Timber":0, "Gilbert":0, "StoneBr":0 , "ClearCr":0, "NPkVill":0, "Blmngtn":0, "BrDale":1 , "SWISU":0, "Blueste":0}
train_filled["Dortmund_Nordstadt"] = train_filled["Neighborhood"].map(dortmund_nordstadt).astype(int)

Repelen = {None: 0, "CollgCr": 0, "Veenker": 0, "Crawfor": 0, "NoRidge": 0, "Mitchel": 0, "Somerst":0, "NWAmes":0 , "OldTown":0, "BrkSide":0, "Sawyer":0, "NridgHt":0, "NAmes":0 , "SawyerW":0 , "IDOTRR":1, "MeadowV":1, "Edwards":0, "Timber":0, "Gilbert":0, "StoneBr":0 , "ClearCr":0, "NPkVill":0, "Blmngtn":0, "BrDale":1 , "SWISU":0, "Blueste":0}

del train_filled['Neighborhood']


cond1 = {None: 0, "Artery":0, "Feedr":0, "Norm":0, "RRNn": 1, "RRAn": 1, "RRNe": 1, "RRAe":1, "PosN":0 , "PosA":0}
train_filled["NearRailroad1"] = train_filled["Condition1"].map(cond1).astype(int)
train_filled["NearRailroad2"] = train_filled["Condition2"].map(cond1).astype(int)
train_filled['NearRailroad'] = train_filled[["NearRailroad1" , "NearRailroad2"]].max(axis=1)
del train_filled['NearRailroad1']
del train_filled['NearRailroad2']

cond1s = {None: 0, "Artery": 1, "Feedr": 1, "Norm":0, "RRNn": 0, "RRAn": 0, "RRNe": 0, "RRAe":0, "PosN":0 , "PosA":0}
train_filled["NearStreet1"] = train_filled["Condition1"].map(cond1s).astype(int)
train_filled["NearStreet2"] = train_filled["Condition2"].map(cond1s).astype(int)
train_filled['NearStreet'] = train_filled[["NearStreet1" , "NearStreet2"]].max(axis=1)
del train_filled['NearStreet1']
del train_filled['NearStreet2']

cond1p = {None: 0, "Artery": 0, "Feedr": 0, "Norm":0, "RRNn": 0, "RRAn": 0, "RRNe": 0, "RRAe":0,"PosN": 1, "PosA": 1}
train_filled["NearPark1"] = train_filled["Condition1"].map(cond1p).astype(int)
train_filled["NearPark2"] = train_filled["Condition2"].map(cond1p).astype(int)
train_filled['NearPark'] = train_filled[["NearPark1" , "NearPark2"]].max(axis=1)
del train_filled['NearPark1']
del train_filled['NearPark2']

del train_filled['Condition1']
del train_filled['Condition2']

bldgtype = {None: 0, "1Fam": 1, "2fmCon": 0, "Duplex":0, "TwnhsE": 1, "Twnhs": 0}
train_filled["BldgType"] = train_filled["BldgType"].map(bldgtype).astype(int)
#ATTENTION: ONLY AFTER BARANALYSIS ###

masvnrtype = {None: 0, "Stone": 1, "NA": 1, "BrkFace":1, "None": 0, "BrkCmn": 0}
train_filled["MasVnrType"] = train_filled["MasVnrType"].map(masvnrtype).astype(int)

heat = {None: 0, "Floor": 0, "GasA": 1, "GasW":1, "Grav": 0, "OthW": 0, "Wall": 0}
train_filled["Heating"] = train_filled["Heating"].map(heat).astype(int)

ele = {None: 0, "SBrkr": 1, "FuseA": 0, "FuseF":0, "FuseP": 0, "Mix": 0, "NA":0}
train_filled["Electrical"] = train_filled["Electrical"].map(ele).astype(int)
#new electricity?

train_filled["BsmtBath"] = train_filled["BsmtFullBath"] + 0.5*train_filled["BsmtHalfBath"]
del train_filled['BsmtFullBath']
del train_filled['BsmtHalfBath']

train_filled["Bath"] = train_filled["FullBath"] + 0.5*train_filled["HalfBath"]
del train_filled['FullBath']
del train_filled['HalfBath']
#looks even more dumb than it is.

train_filled["AllRooms"] = train_filled["TotRmsAbvGrd"] + train_filled["Bath"]

train_filled["RelKitchen"] = train_filled["KitchenQual"] * train_filled["KitchenAbvGr"]

functional = {None: 0, "Typ": 0, "Min1": 1, "Min2":1, "Mod": 1, "Maj1": 1, "Maj2":1, "Sev":1, "Sal":1}
train_filled["Functional"] = train_filled["Functional"].map(functional).astype(int)

train_filled["RelFirePlaces"] = train_filled["FireplaceQu"] * train_filled["Fireplaces"]

paveddrive = {None: 0, "Y": 1, "P": 0, "N":0}
train_filled["PavedDrive"] = train_filled["PavedDrive"].map(paveddrive).astype(int)

newhouse = {None: 0, "WD": 0, "CWD": 0, "VWD":0, "New": 1, "COD": 0, "Con":0 , "ConLw": 0, "ConLI":0, "ConLD":0, "Oth":0}
train_filled["SaleType"] = train_filled["SaleType"].map(newhouse).astype(int)

newhouse2 = {None: 0, "Normal": 0, "Abnorml": 0, "AdjLand":0, "Alloca": 0, "Family": 0, "Partial":1 }
train_filled["SaleCondition"] = train_filled["SaleCondition"].map(newhouse2).astype(int)

del train_filled['RoofMatl']
#prone to overfitting as fu**

train = pd.get_dummies(train_filled) #cast all non-numericals to dummy variables



train['HouseStyle_2.5Fin'] = 0
#train['Heating_Floor'] = 0
#train['Heating_OthW'] = 0
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

train = train.reindex_axis(sorted(train.columns), axis=1)

print(list(train))
print(np.shape(list(train)))

train.to_csv('test_new.csv', index=False) # new data!
