#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
Location = "Your Turn Files To Use/AncestryExcelFile.xls"
df = pd.read_excel(Location)


# In[7]:


df.columns = ('AreaName', 'AreaCode', 'Ancestry0F', 'Ancestry0D', 'Ancestry0N1', 'Ancestry0N2', 'Ancestry9F', 'Ancestry9D', 'Ancestry9N1', 'Ancestry9N2')
df.head(10)


# In[ ]:




