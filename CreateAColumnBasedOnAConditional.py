#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[5]:


import numpy as np
df['timemgmt'] = np.where((df['exercise']>3) & (df['hours']>17), 'busy', 'normal')
df.head(10)


# In[ ]:




