import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

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

###########################################################################
#
#   Step 2 : EXPLORATORY DATA ANALYSIS (EDA)
#
###########################################################################

print(Border)
print("Step 2 : Exploratory Data Analysis")
print(Border)

print("Shape of Dataset : ", df.shape)

print("Column Names : ", list(df.columns))

print("Missing Values per Column : ")
print(df.isnull().sum)

print("Class distribtion (Species Count)")
print(df["species"].value_counts())

print("Satistical Report of Dataset : ")
print(df.describe())

###########################################################################
#
#   Step 3 : DECIDE INDEPENDENT AND DEPENDENT VARIABLE
#
###########################################################################

print(Border)
print("Step 3 : Decide Independent and Dependent Variable")
print(Border)


# X : Independent Variable -> Features
# Y : Dependent Variables  -> Labels

feature_cols = [
                "sepal length (cm)",
                "sepal width (cm)",
                "petal length (cm)",
                "petal width (cm)"
               ]

X = df[feature_cols]
Y = df["species"]

print("X Shape : ", X.shape)
print("Y Shape : ", Y.shape)

###########################################################################
#
#   Step 4 : VISUALIZATION OF DATASET
#
###########################################################################

print(Border)
print("Step 4 : Visualiztion of Dataset")
print(Border)

# Scatter plot
plt.figure(figsize = (7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label = sp)

plt.title("Marvellous Iris Case Study")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")


plt.legend()
plt.grid()
plt.show()
