#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
from pandasgui import show
import matplotlib.pyplot as plt


# In[2]:


pip install pandasgui


# In[3]:


df= pd.read_excel('Downloads\data.xlsx')


# In[4]:


show(df)


# In[18]:


get_ipython().system('pip install bokeh==3.8.0')


# In[5]:


import dtale
d = dtale.show(df)
d.open_browser()


# In[21]:


pip install dtale


# In[6]:


df.head()


# In[7]:


df.tail()


# In[8]:


df.columns


# In[9]:


df.info()


# In[10]:


df['loan_status'].value_counts()


# In[11]:


df.sample()


# In[12]:


df.sample()


# In[13]:


df.sample(30)


# In[14]:


df.shape


# In[15]:


print ( "number of rows, number of  columns:", df.shape)


# In[16]:


print(f" number of rows, number of columns:", {df.shape})


# In[17]:


df.dtypes


# In[18]:


df.columns


# In[19]:


df.index


# In[20]:


df.describe()


# In[21]:


df['loan_status']


# In[22]:


df['loan_status'].unique()


# In[23]:


df['loan_status'].value_counts()


# In[24]:


df[['loan_amnt', 'loan_status']]


# In[25]:


df[['loan_status', 'int_rate', 'grade']]


# In[26]:


df.iloc[0]


# In[27]:


df.iloc[10]


# In[28]:


df.loc[0]


# In[29]:


df.loc[5398]


# In[30]:


import klib


# In[31]:


pip install klib


# In[49]:


get_ipython().system(' pip install -U klib')


# In[32]:


klib.corr_mat(df)


# In[33]:


klib.corr_plot(df)


# In[34]:


klib.corr_interactive_plot(df, split='neg').show()


# In[35]:


klib.corr_interactive_plot(df, split='neg').show()


# In[36]:


klib.corr_interactive_plot(df, split='pos').show()


# In[37]:


klib.dist_plot(df['loan_amnt'])


# In[38]:


klib.dist_plot(df['dti'])


# In[39]:


klib.dist_plot(df['annual_inc'])


# In[40]:


klib.dist_plot(df['funded_amnt'])


# In[42]:


klib.corr_plot(df, target='loan_amnt')


# In[44]:


klib.cat_plot(df, top=4, bottom=4)


# In[46]:


df.at[0, 'loan_amnt']


# In[48]:


df.plot.scatter(x='loan_amnt', y='funded_amnt')


# In[ ]:




