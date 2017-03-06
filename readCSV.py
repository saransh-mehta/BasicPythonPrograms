#reading basic csv file
import numpy as np

x=[]
for line in open("F:\PYTHON PROGRAMS\gitClone\machine_learning_examples-master\linear_regression_class\data_2d.csv"):
    row=line.split(',')
    #sample=map(float,row)
    x.append(row)
    #np.array(x)
    
print(x)
np.array(x)
print(np.shape(x))
