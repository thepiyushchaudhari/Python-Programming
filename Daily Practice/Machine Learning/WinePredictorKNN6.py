import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    border = "--"*50
###########################################################################
#
# Step 1 : LOAD THE DATASET FROM CSV FILE
#
###########################################################################
    print(border)
    print("Step 1 : LOAD THE DATASET FROM CSV FILE")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some entries from Dataset : ")
    print(df.head())
    print(border)
###########################################################################
#
# Step 2 :  CLEAN THE DATASET
#
###########################################################################
    print(border)
    print("Step 2 : CLEAN THE DATASET")
    print(border)

    df.dropna(inplace = True)

    print("Shape of Dataset : ", df.shape)
    print("Total records : ", df.shape[0])
    print("Total columns : ", df.shape[1])

    print(border)
###########################################################################
#
# Step 3 : SEPARATE INDENDENT AND DEPENDENT VARIABLES
#
###########################################################################
    print(border)
    print("Step 3 : SEPARATE INDENDENT AND DEPENDENT VARIABLES")
    print(border)

    X = df.drop(columns = ['Class'])
    Y = df['Class']

    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)

    print(border)
    print("Input columns : ", X.columns.tolist())
    print("Output column : Class")
    print(border)
###########################################################################
#    
# Step 4 : SPLIT THE DATASET FOR TRAINING AND TESTING
#
###########################################################################

    print(border)
    print("Step 4 : SPLIT THE DATASET FOR TRAINING AND TESTING")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5, random_state=42, stratify=Y)

    print(border)
    print("Details of training and testing are : ")
    print("Shape of X_train : ", X_train.shape)
    print("Shape of X_test : ", X_test.shape)
    print("Shape of Y_train : ", Y_train.shape)
    print("Shape of Y_test : ", Y_test.shape)
    print(border)
###########################################################################
#
# Step 5 : FEATURE SCALING
#
###########################################################################

    print(border)
    print("Step 5 : FEATURE SCALING")
    print(border)

    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("Feature Scaling Done")

    print(border)
###########################################################################
#
# Step 6 : BUILD THE MODEL
#
###########################################################################
    
    print(border)
    print("Step 6 : BUILD THE MODEL")
    print(border)
    
    model = KNeighborsClassifier(n_neighbors=51)

    print("Classifiction Model Created")

    print(border)
###########################################################################
#
# Step 7 : TRAIN THE MODEL
#
###########################################################################

    print(border)
    print("Step 7 : TRAIN THE MODEL")
    print(border)

    model = model.fit(X_train_scaled, Y_train)

    print("Model Training Completed")

    print(border)
###########################################################################
#
# Step 8 : TEST THE MODEL
#
###########################################################################
   
    print(border)
    print("Step 8 : TEST THE MODEL")
    print(border)

    Y_pred = model.predict(X_test_scaled)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Model Accuracy is : ", accuracy*100)


def main():
    MarvellousClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()