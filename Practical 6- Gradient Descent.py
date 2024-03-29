#Gradient Descent

#Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing Dataset
data=pd.read_csv("scoresstudent.csv")
print(data)
print("\n")
x=data.iloc[:15,0]
y=data.iloc[:15,1]
print(x)
print("\n")
print(y)
print("\n")

m_curr = b_curr = 0
iterations = 1000
n = len(x)
learning_rate = 0.001
for i in range(iterations):
 y_predicted = m_curr * x + b_curr #Predicted
 cost = (1/n) * np.sum((y-y_predicted)**2) #Cost
 slope = -(2/n)*sum(x*(y-y_predicted)) #slope here is slope
 intrcpt = -(2/n)*sum(y-y_predicted)     #intrcpt here is intercept i.e.c
 scur = scur - learning_rate * slope
 icur = icur - learning_rate * intrcpt

print("\nvalue of y predicted\n")
print(y_predicted)
print("\n")
print(" value of m is ", m_curr)
print("\n")
print("value of c is" ,b_curr)
plt.scatter(x,y,color='red')
plt.plot(x,y_predicted,color='blue')
plt.title('hours vs scores')
plt.xlabel('hours')
plt.ylabel('scores')
