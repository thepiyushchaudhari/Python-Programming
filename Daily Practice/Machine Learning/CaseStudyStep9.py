import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
                                accuracy_score, 
                                confusion_matrix,
                                classification_report
                            )

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

###########################################################################
#
#   Step 6 : BUILD THE MODEL
#
###########################################################################

print(Border)
print("Step 6 : Build the Model")
print(Border)

model = DecisionTreeClassifier(max_depth = 5)

print("Model is created successfully")

###########################################################################
#
#   Step 7 : TRAIN THE MODEL
#
###########################################################################

print(Border)
print("Step 7 : Train the Model")
print(Border)

model.fit(X_train, Y_train)
print("Model Trained Successfully")

###########################################################################
#
#   Step 8 : EVALUATE THE MODEL
#
###########################################################################

print(Border)
print("Step 8 : Evaluate the Model")
print(Border)

Y_pred = model.predict(X_test)
print("Model Evaluated Successfully")

print("Expected Answers : ")
print(Y_test)

print("Predicted Answers : ")
print(Y_pred)

###########################################################################
#
#   Step 9 : EVALUATE THE MODEL PERFORMANCE
#
###########################################################################

print(Border)
print("Step 9 : Evaluate the Model Performance")
print(Border)

accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of model is : ", accuracy *100)

print("Confusion Matrix")
cm = confusion_matrix(Y_test, Y_pred)
print(cm)

print("Classiication Report")
print(classification_report(Y_test, Y_pred))