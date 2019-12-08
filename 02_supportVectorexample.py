import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets

if __name__ == '__main__':
    irysy = datasets.load_iris()
    X = irysy.data[:, :2]
    y = irysy.target

    x_min, x_max = X[:, 0].min() - 1, X[:,0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:,1].max() + 1

    h = (x_max/x_min)/100
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    svm = svm.SVC(kernel = 'linear', C = 2.0)
    svm.fit(X,y)

    X_plot = np.c_ [xx.ravel(), yy.ravel()]

    Z = svm.predict(X_plot)
    Z  = Z.reshape(xx.shape)
    plt.figure()
    plt.contour(xx,yy, Z)
    plt.scatter(X[:,0], X[:,1], c = y)
    plt.show()
