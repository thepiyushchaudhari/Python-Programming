import pandas as pd

Border = "--" * 30

###########################################################################
#
#   Step 1 : LOAD THE DATASET
#
###########################################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DataPath = "C:\\Users\\SHRUTI\\Desktop\\iris.csv"

df = pd.read_csv(DataPath)

print("Dataset Loaded Successfully")
print("Initial Entries from dataset are : ")
print(df.head())
