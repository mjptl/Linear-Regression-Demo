#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("student-mat.csv",delimiter=";")
data.head()


# In[3]:


data = data[['G1','G2','G3']]
traing_data = data[0:340]
test_data = data[340:]
print(traing_data.shape,test_data.shape)


# In[4]:


def function(x,m,c):
    y = (m*x) + c
    return y


# In[5]:


def find_cost(y_prd,y_ord):
    delta = y_ord-y_prd
    delta = delta * delta
    return delta


# In[6]:


l_rate = 0.1


# In[7]:


df = pd.DataFrame(traing_data[["G1","G3"]])
df.columns = ["x","y"]
df


# In[8]:


df["y_prd"] = function(df.x,1,0)
df


# In[9]:


find_cost(df.y_prd,df.y).mean()


# In[10]:


trys = np.arange(0,2,0.05)
trys


# In[13]:


l = []
for i in trys:
    df.y_prd = function(df.x,i,-1.49)
    l.append(find_cost(df.y_prd,df.y).mean())
for i in range(len(l)):
    print(l[i]," --> ",trys[i])


# In[12]:


plt.plot(trys,l)
plt.plot(trys,l,"ro")
plt.xlabel("Value of m")
plt.ylabel("Cost")


# In[29]:


df2 = pd.DataFrame()
df2["Y_ord"] = test_data.G3
df2["Y_prd"] = function(test_data.G1,1.1,-1.49)
df2["err"] = df2.Y_ord - df2.Y_prd
df2


# In[32]:


100 - find_cost(df2.Y_prd,df2.Y_ord).mean()


# In[ ]:




