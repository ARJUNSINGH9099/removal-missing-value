
# try these code in googlecolab
# importing libraries
import pandas as pd
import numpy as np
dataset=pd.read_csv("/content/SalaryGender.csv")

dataset.head()



# checking for the dimension of the dataset
dataset.shape

# old dataset with missed value
dataset["Age"][:10]


# mean missed values
dataset["Age"]=dataset["Age"].replace(np.NaN,dataset["Age"].mean())
dataset["Age"][:20]

# Median-missed value
dataset['Age']=dataset["Age"].replace(np.NaN,dataset["Age"].median())
print(dataset["Age"][:15])

# Mode-missing value
import statistics
dataset["Age"]=dataset["Age"].replace(np.NaN,statistics.mode(dataset["Age"]))
print(dataset["Age"][:100])

# missing value-categorieal
dataset.isnull().sum()

# missing value-categeorical-solution
dataset["PhD"]=dataset["PhD"].fillna("UG")

# checking for missed valuein categeorial
dataset.isnull().sum()
# print(dataset["PhD"][:32])

# LOCF-LAST Observation carried forward
dataset["Age"]=dataset["Age"].fillna(method="ffill")
dataset.isnull().sum()

# prompt: interpolation-linear in age

dataset["Age"] = dataset["Age"].interpolate(method="linear",limit_direction="forward",axis=0)

# Check for missing values again
dataset.isnull().sum()

