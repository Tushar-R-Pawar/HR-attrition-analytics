import numpy as np 
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split


df=pd.read_csv("HR Attrition.csv")

oe=OrdinalEncoder()
colname=df.select_dtypes(object).columns
df[colname]=oe.fit_transform(df[colname])
df.drop(['MonthlyRate','DailyRate','HourlyRate','EmployeeNumber','EmployeeCount','StandardHours','Over18'],axis=1,inplace=True)

features=df.iloc[:,2:]
features['Age']=df.iloc[:,0:1]
target=df.iloc[:,1]

X_train,X_test,y_train,y_test=train_test_split(features,target,test_size=0.2,random_state=42)

def mymodel(model):
    model.fit(X_train, y_train)
    return model

def makeprediction():
    logreg=LogisticRegression()
    svm = SVC(kernel='linear',C=1.0,gamma=1)
    model = mymodel(logreg)
    return model
    
