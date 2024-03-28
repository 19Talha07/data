#!/usr/bin/env python
# coding: utf-8

# In[24]:


import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd


# In[25]:


import seaborn


# In[26]:


dataset = pd.read_csv("FakeData.csv", delimiter=";")


# In[27]:


dataset


# In[28]:


dataset.shape


# In[29]:


dataset.info()


# In[30]:


dataset.chemy -100


# In[31]:


dataset.describe()


# In[32]:


seaborn.set_theme(context='notebook',
    style='white',
    palette='pastel',)


# In[33]:


plt.figure(figsize=(9, 5.5))
plt.hist(dataset.age, bins=25, density=True, label="Age")

seaborn.despine()

plt.xlabel("Ages")
plt.ylabel("density")

plt.legend(loc="best")
plt.grid(True, alpha= 0.45, ls="-.")
plt.show()


# In[ ]:





# In[ ]:




