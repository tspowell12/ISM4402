#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


df['Cars Sold'].mean()


# In[28]:


max = df['Cars Sold'].max()


# In[29]:


min = df['Cars Sold'].min()


# In[ ]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])
plt.pie


# In[6]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[7]:


df['Years Experience'].mean()


# In[8]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[74]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[76]:


df.hist(column="Cars Sold", by="Gender")


# In[77]:


df.boxplot(by='Gender', column='Hours Worked')

