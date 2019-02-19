from sklearn import datasets,metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

#data set
iris_datasets=datasets.load_iris()

#defining x and y as input and output
x = iris_datasets.data
y = iris_datasets.target

#training the data set with test size of 40%
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.8,random_state=25)

#choosing our model as a gaussain distribution
model=GaussianNB()
##fitting the model with training data
model.fit(x_train,y_train)

#printing the probability of the model
print(f"The Probability of the traning model is {model.score(x_train,y_train)}")

#defining the predicted outcome when our model is applied on the test data
y_pred = model.predict(x_test)
#printing the accuracy of the model
print("The Accuracy of the model is : ",metrics.accuracy_score(y_test, y_pred))