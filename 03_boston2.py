import numpy as np
from sklearn import datasets
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.utils import shuffle

if __name__ == '__main__':
    # Load housing data
    data = datasets.load_boston()

    # Shuffle the data
    #X, y = data.data, data.target
    X, y = shuffle (data.data, data.target, random_state= 7)
    # Shuffle the data


    # Split the data into training and testing datasets
    num_training = int(0.8 * len(X))
    X_train, y_train = X[:num_training], y[:num_training]
    X_test, y_test = X[num_training:], y[num_training:]

    # Create Support Vector Regression model
    sv_regressor = SVR()

    # Train Support Vector Regressor
    sv_regressor.fit(X_train, y_train)

    print(data.DESCR)
    # Test the regressor on test datapoint
    test_data = [3.7, 0, 18.4, 1, 0.87, 5.95, 91, 2.5052, 26, 666, 20.2, 351.34, 15.27]
    print("\nPredicted price:", sv_regressor.predict([test_data]))
