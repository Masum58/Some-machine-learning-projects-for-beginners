#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


# In[4]:


iris_data = load_iris()
dir(iris_data)


# In[8]:


iris_data.data


# In[9]:


iris_data.feature_names


# In[10]:


iris_data.target


# In[11]:


iris_data.target_names


# In[ ]:


df = pd.DataFrame(iris_data.data,columns=['sepal length (cm)',
 'sepal width (cm)',
 'petal length (cm)',
 'petal width (cm)'])

