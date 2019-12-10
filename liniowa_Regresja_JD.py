########################################################################################################################
# Statistics of sobriety [‰] based on weight [kg], gender [0-female, 1-male], age, alcohol consumption [ml] and        #
# drinking time [hour]. Sobriety  is determined subjectively by the respondents.                                       #
# Created by Jarosław Drząszcz(s16136).                                                                                #
########################################################################################################################
from sklearn.utils import shuffle

import numpy as np
from sklearn import linear_model
from sklearn.svm import SVR

if __name__ == '__main__':
    # Load Statistics of sobriety data
    plik_wejsciowy = "statistics_of_sobriety.txt"
    data = np.loadtxt(plik_wejsciowy, delimiter=',')

    # Shuffle the data
    X, y = shuffle(data[:, :-1], data[:, -1], random_state=7)
    print(X)
    print(y)

    # Split the data into training and testing data
    num_traing = int(len(X)*0.9)
    num_test = len(X) - num_traing

    X_tran, y_tran = X[:num_traing], y[:num_traing]
    X_test, y_test = X[num_traing:], y[num_traing:]

    # Create Support Vector Regression model
    # regressor = linear_model.HuberRegressor()
    regressor = SVR(kernel='linear')
    # Train Support Vector Regressor
    regressor.fit(X_tran, y_tran)

    # Test the regressor on test datapoint
    test_data = [80, 1, 35, 300, 2]
    print("\nPredicted value:", regressor.predict([test_data]))
