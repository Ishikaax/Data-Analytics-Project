#!/usr/bin/env python
# coding: utf-8

# In[4]:


#import libraries
get_ipython().system('pip install kaggle')
import kaggle


# In[3]:


import kaggle


# In[5]:


import kaggle


# In[6]:


get_ipython().system('kaggle datasets download ankitbansal06/retail-orders -f orders.csv')


# In[8]:


import zipfile 
zip_ref = zipfile.ZipFile('orders.csv.zip')
zip_ref.extractall()
zip_ref.close()


# In[11]:


import pandas as pd

df = pd.read_csv('orders.csv')
df.head(20)


# In[36]:


df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()


# In[43]:


df.rename(columns={'Order Id':'order_id', 'City':'city'})
#df.columns=df.columns.str.lower()
#df.columns=df.columns.str.replace(' ','_')
df.head(5)


# In[49]:


#df['discount']=df['list_price']*df['discount_percent']*.01
df


# In[50]:


df['sale_price']=df['list_price']-df['discount']


# In[51]:


df


# In[52]:


df['profit']=df['sale_price']-df['cost_price']


# In[53]:


df


# In[56]:


df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")


# In[63]:


df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)


# In[64]:


df


# In[65]:


#Load the data into SQL server


# In[ ]:




