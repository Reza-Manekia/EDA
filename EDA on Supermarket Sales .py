#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import seaborn as sns

data = pd.read_csv('D:/supermarket_sales.csv.csv')
data


# In[5]:


data.shape


# In[6]:


data.columns


# In[8]:


data.isna().sum()


# In[9]:


data.describe()


# In[10]:


data.nunique()


# In[16]:


data['Product line'].unique()


# In[21]:


data.groupby(['Product line'])


# In[17]:


Data = data.drop(['City', 'Time','Customer type', 'Payment','Invoice ID', 'Tax 5%','Date'], axis=1)
Data


# In[8]:


Data.shape


# In[11]:


Correlation = Data.corr()
sns.heatmap(Correlation, xticklabels=Correlation.columns, yticklabels=Correlation.columns, annot = True)


# In[12]:


sns.pairplot(Data)


# In[22]:


sns.relplot(y='Product line',x='Quantity',hue='Branch',data = Data)


# In[24]:


sns.distplot(Data['Quantity'],bins=10)


# In[28]:


sns.catplot(x='Gender', y='Quantity', kind= 'box', data = Data)


# In[ ]:




