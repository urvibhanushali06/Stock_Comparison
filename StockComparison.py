#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install yfinance')
get_ipython().system('pip install sqlalchemy')
#library to collect financial data


# In[4]:


import pandas as pd
import yfinance as yf
#library to connect to SQL DB
from sqlalchemy import create_engine


# In[16]:


engine = create_engine("sqlite:///Stockdata.db")


# In[5]:


dow = pd.read_html("https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average")
dow[1]


# In[6]:


symbols = dow[1].Symbol.to_list()
symbols


# In[8]:


obj = yf.Ticker("MSFT")


# In[9]:


obj.info


# In[10]:


infos = []

for symbol in symbols:
    inf = yf.Ticker(symbol).info
    infos.append(inf)


# In[14]:


df = pd.DataFrame(infos)


# In[ ]:


df = df.drop(columns= "companyOfficers")


# In[19]:


df.to_sql("Fundamentals" , engine, index=False, if_exists="append")


# In[15]:


df


# In[20]:


pd.read_sql("Fundamentals", engine)

