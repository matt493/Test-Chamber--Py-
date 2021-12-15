#!/usr/bin/env python
# coding: utf-8

# In[9]:


'''scale.fit_transform(X)
# Train / Test
# ================
Train/Test is a method to measure the accuracy of your model.
split the the data set into two sets: a training set and a testing set.
80% for training, and 20% for testing.'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = np.poly1d(np.polyfit(train_x, train_y,4))
myline = np.linspace(0, 6, 100)


plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
#plt.scatter(test_x, test_y)
plt.show()

r2 = r2_score(test_y, mymodel(test_x))
print(r2)


# In[16]:


# Import Libraries
#=================
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn import tree

# Load Dataset
# ===============

data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Splitting Data into Training and Test Sets
# ==============================================

X_train, X_test, Y_train, Y_test = train_test_split(df[data.feature_names], df['target'], random_state=0)

# Create Model Pattern
#=========================

clf = DecisionTreeClassifier(max_depth=3, random_state=0)
clf.fit(X_train, Y_train)


# Visualization of tree
#========================

# tree.plot_tree(clf) 

fn=['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']
cn=['setosa', 'versicolor', 'virginica']
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
tree.plot_tree(clf, feature_names = fn, class_names=cn, filled = True);
fig.savefig('imagename.png')