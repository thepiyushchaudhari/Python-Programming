import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split

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


###########################################################################
#
#   Step 5 : SPLIT THE DATASET FOR TRAINING AND TESTING
#
###########################################################################

print(Border)
print("Step 5 : Split the dataset for training and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5, random_state = 42) #random_state -> shuffels the dataset

print("Dataset splitting activity done")

print("X Shape : ", X.shape)            #(150,4)
print("Y Shape : ", Y.shape)            #(150,)

print("X_train : ", X_train.shape)      #(75,4)
print("X_test : ", X_test.shape)        #(75,4)

print("Y_train : ", Y_train.shape)      #(75,)
print("Y_test : ", Y_test.shape)        #(75,)

