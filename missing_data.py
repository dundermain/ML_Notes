#Missing values can create bias towards the model if it is not handled properly

from sklearn.preprocessing import Imputer

imp = Imputer(missing_values = 'Nan', strategy = 'mean', axis=0)
imp.fit(X)
X = imp.transform(X)