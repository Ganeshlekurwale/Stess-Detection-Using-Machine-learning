#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd   
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer


# In[4]:


df=pd.read_csv("C:/Users/Rohit/Desktop/spam.csv",encoding="latin-1")


# In[6]:


#visualizing dataset
df.head(n=10)


# In[8]:


df.shape


# In[10]:


#to check whether target attribute is binary or not
np.unique(df['class'])


# In[12]:


np.unique(df['message'])


# In[14]:


#creating sparse matrix

x=df["message"].values
y=df["class"].values

#create count vectorizer object
cv=CountVectorizer()

x=cv.fit_transform(x)
v=x.toarray()

print(v)


# In[16]:


first_col=df.pop('message')
df.insert(0,'message',first_col)
df


# In[18]:


#splitting train + test  3:1

train_x=x[:4180]
train_y=y[:4180]

test_x=x[4180:]
test_y=y[4180:]


# In[20]:


bnb=BernoulliNB(binarize=0.0)
model=bnb.fit(train_x,train_y)

y_pred_train=bnb.predict(train_x)
y_pred_test=bnb.predict(test_x)


# In[22]:


#training score
print(bnb.score(train_x,train_y)*100)

#testing score
print(bnb.score(test_x,test_y)*100)


# In[24]:


from sklearn.metrics import classification_report
print(classification_report(train_y,y_pred_train))


# In[25]:


from sklearn.metrics import classification_report
print(classification_report(test_y,y_pred_test))

