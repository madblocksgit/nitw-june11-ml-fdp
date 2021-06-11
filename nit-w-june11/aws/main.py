# import mongodb
from pymongo import MongoClient

# import pandas for data handling
import pandas as pd

# from sklearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# from flask
from flask import Flask,render_template,request

# flask app object
app=Flask(__name__)

# create a client object
client=MongoClient('127.0.0.1',27017)

# handle the database
db=client['nitfdp']

# handle the collection
c=db['finaldata']

# read the data from database
'''for i in c.find():
 print(i)'''

# Create a dataframe
df=pd.DataFrame(list(c.find()))
#print(df)

# col0 - _id, col1 - mq3, col2-mq2, col3 - label

# Seperate Input and Target Variables
# Input - Independent Variables - MQ3
# Target - Dependent Variables - label

# Input Variables
X=df.iloc[:,1].values
X=X.reshape(-1,1)
#print(X)

# Output Variables
Y=df.iloc[:,-1].values
#print(Y)

# Split the dataset into train and test
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)

#print(X_train.shape)
#print(X_test.shape)
#print(Y_train.shape)
#print(Y_test.shape)

classifier=KNeighborsClassifier(n_neighbors=3)
#print(classifier)

# train the model
classifier.fit(X_train,Y_train) # pass the training dataset

# predict the test data
Y_pred=classifier.predict(X_test)
#print(Y_pred)

print(accuracy_score(Y_pred,Y_test)*100)

def predict_output(value):
 print('Calling Classifier')
 k=classifier.predict([[value]])
 return(k)

@app.route('/')
def get_connected():
 return(render_template('index.html'))

@app.route('/madhu',methods=['POST'])
def read_data():
 value_read=int(request.form['value1'])
 out=classifier.predict([[value_read]])

 return(render_template('index.html',prediction_result=out[0]))

if __name__ =="__main__":
 app.run('0.0.0.0')  # web-server will get launched

