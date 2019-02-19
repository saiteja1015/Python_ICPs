from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets

#data set
iris_datasets = datasets.load_iris()

#defining x and y as input and output
x = iris_datasets.data
y = iris_datasets.target


#training the data set with test size of 40% for linear kernel
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.4, random_state=25)

#training the data set with test size of 40% for rbf kernel
train_x1, test_x1, train_y1, test_y1=train_test_split(x, y, test_size=0.4, random_state=23)

#choosing the model for linear kernel
lmodel=SVC(kernel='linear')

#choosing the model for rbf kernel
rmodel=SVC(kernel='rbf')

#fitting the model with training data
lmodel.fit(train_x, train_y)
prediction=lmodel.predict(test_x)
print("linear kernel Accuracy score is", accuracy_score(prediction, test_y))

#fitting the model with training data
rmodel.fit(train_x1, train_y1)
pred=rmodel.predict(test_x1)
print("RBF kernel accuracy score is", accuracy_score(pred, test_y1))
