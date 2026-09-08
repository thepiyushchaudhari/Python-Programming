import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():

    # Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent Variables X : ", X)
    print("Values of Dependent Variable Y : ", Y)

    sum_x = 0
    sum_y = 0

    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]

    mean_x = sum_x / len(X)
    mean_y = sum_y / len(Y)

    print("Mean of X is : ", mean_x)
    print("Mean of Y is : ", mean_y)

    n = len(X) #5

    numerator = 0
    denomenator = 0

# Calculate Slope -> "m"
    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denomenator = denomenator + ((X[i] - mean_x) ** 2)

    m = numerator / denomenator

    print("Slope of Line that is 'm' : ", m)

    # Y = m X + c
    # c = Y - m X
    # c = Y_mean - m * X_mean

    c = mean_y - m * mean_x 
    print("Y - inetrcet that is 'c' is : ", c)

    x = np.linspace(1,6,n)
    y =  c + m * x

    plt.plot(x, y, color = 'g', label = "Regression Line")
    plt.scatter(X, Y, color = 'r', label = "Scatter Plot")

    plt.xlabel ("X : Independent Variables")
    plt.ylabel("Y : Dependent Variable")

    plt.legend()
    plt.show()




def main ():
    MarvellousPredictor()

if __name__ == "__main__" :
    main()