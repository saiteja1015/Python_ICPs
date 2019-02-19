from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets

#data set
iris_datasets = datasets.load_iris()

#defining x and y as input and output
x = iris_datasets.data
y = iris_datasets.target

#training the data set with test size of 40%
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.4, random_state=25)

#choosing the model
lmodel=SVC(kernel='linear')
#fitting the model with training data
lmodel.fit(train_x, train_y)

#defining the predicted outcome when our model is applied on the test data
prediction=lmodel.predict(test_x)
#printing the accuracy of the model
print("The accuracy of the model is", accuracy_score(prediction, test_y))
