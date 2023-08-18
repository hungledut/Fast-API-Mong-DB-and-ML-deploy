"model machine learning"
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

# Loading Iris Dataset
iris = load_iris()

# Getting features and targets from the dataset
X = iris['data']
Y = iris['target']

# Fitting our Model on the dataset
iris_clf = GaussianNB()
iris_clf.fit(X,Y)
