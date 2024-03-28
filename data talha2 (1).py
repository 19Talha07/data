#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import seaborn


# In[2]:


dataset = pd.read_csv("Salary.csv")


# In[4]:


dataset.head()


# In[5]:


dataset.shape


# In[6]:


dataset.info()


# In[7]:


np.nan


# In[8]:


dataset.describe()


# In[9]:


plt.plot(dataset.YearsExperience, dataset.Salary)


# In[10]:


plt.plot(np.array(dataset.Salary)/ np.array(dataset.YearsExperience))

plt.show()


# In[ ]:




