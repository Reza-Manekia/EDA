#!/usr/bin/env python
# coding: utf-8

# ### Importing Libraries and csv file

# In[39]:


import pandas as pd
import seaborn as sns

df = pd.read_csv('D:\StudentsPerformance.csv')


# # <b><i>Step # 1: Understanding the data</i></b>

# In[10]:


df.head()


# In[11]:


df.tail()


# ### some staticstical Calculations

# In[15]:


# describe function give statistical data like (mean, SD, min, Max values) of given data set


# In[14]:


df.describe()


# In[16]:


# shape give the dimension of our data set (rows, coloumns)


# In[18]:


df.shape


# In[19]:


# Column create an list containing all the coloumns in our data set


# In[20]:


df.columns


# In[ ]:


# .nunique function give the no of unique values in int form


# In[22]:


df.nunique()


# In[ ]:


# .unique value give the unique value in given or desired column 


# In[23]:


df['gender'].unique()


# # <b><i>Step # 2: Cleaning the data</i></b>

# It is most important for analysis that our data set must be clean means there is no any null values or N/A values,
# duplicate and raw values contain in our data set.data cleansing allows for accurate, defensible data that generates 
# Wreliable visualizations, models, and business decisions.
# 
# So firstly we check that either we have null values exist in our data set or not 

# In[ ]:


# .null or .isna is a function which give the boolean output that either you contain a null values or not 


# In[34]:


df.isna().any()


# In[35]:


df.isna().sum()


# In[ ]:


# Its Good that our data set doesn't have any null values Now we check the columns 
# which are not helpful for analysis and modelling

# In our case race/ethnicity and parental level of education 
# both are not helpful in future for analysis and modelling so we remove by drop command


# In[38]:


StudentsPerformance = df.drop(['race/ethnicity','parental level of education'], axis=1)
StudentsPerformance


# In[40]:


# Now our dataset only contain values which are sufficient for our analysis
# One more thing is that we gave axis = 1 because we drop according to coloumn if we drop a/c to rows we give axis = 0


# # <b><i>Step # 3: Relationship Analysis</i></b>

# In[41]:


# One of the main features for measuring relation b/w two variables is correlation. 
# We can visualize relation of d/f variables using plots in seaborn library


# In[42]:


correlation = StudentsPerformance.corr()


# In[ ]:


# Heatmap visualize the correlation of d/f variables in b/w  0 and 1 (including)


# In[45]:


sns.heatmap(correlation, xticklabels = correlation.columns, yticklabels = correlation.columns, annot=True)


# In[46]:


sns.pairplot(StudentsPerformance)


# In[ ]:


#.relplot give the relation of three variables we can relate either numerical data and categorical data as well


# In[51]:


sns.relplot(x='math score', y = 'reading score', hue = 'gender', data = StudentsPerformance)


# In[56]:


sns.distplot(StudentsPerformance['math score'], bins = 5)


# In[58]:


sns.catplot(x='gender', y='math score',kind = 'box', data= StudentsPerformance)


# In[ ]:




