import matplotlib.pyplot as plt
import numpy as np
import pickle
import sklearn.metrics as sm
from sklearn import linear_model

if __name__ == '__main__':
    input_file = "mydata.txt"
    data = np.loadtxt(input_file, delimiter=",")

    X , y = data[:, :-1], data[:, -1]

    num_training = int(0.9 * len(X))
    num_test = len(X) - num_training

    X_tran, y_train = X[:num_training], y[:num_training]
    X_test, y_test = X[num_training:], y[num_training:]

    regressor = linear_model.HuberRegressor()
    regressor.fit(X_tran, y_train)
    y_test_pred = regressor.predict(X_test)

    with open("nauczonymodel.pkl", 'wb') as f:
        pickle.dump(regressor, f)

    with open("nauczonymodel.pkl", 'rb') as f:
        regressor_model = pickle.load(f)

    blad = sm.mean_absolute_error(y_test, y_test_pred)
    print ("Mean absolute error: ", blad)

    plt.scatter(X_test, y_test, color='red')
    plt.plot(X_test, y_test_pred, color='black')
    plt.show()
