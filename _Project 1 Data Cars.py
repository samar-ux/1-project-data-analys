#!/usr/bin/env python
# coding: utf-8

#  Project 1: Data Cars

# Table of Contents
# 
-Download & Extract data 
-Load & Assess & cleaning data 
1-What are the most common car manufacturers in the dataset?
2-What is the average price of vehicles by manufacturer?
3-What is the distribution of vehicle conditions?
4-How does price vary by vehicle type?
5-What is the relationship between the year of the vehicle and its price?
6-Which cities have the highest average vehicle prices?
7-What are the most common vehicle types listed?
8-Which car models are listed most frequently?
9-What is the distribution of mileage across different vehicle types?
10-How does fuel type affect the price of vehicles?
11-Are certain vehicle conditions associated with higher prices?
12-What is the trend in vehicle prices over different years?
# In[ ]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import datetime 
import warnings
warnings.filterwarnings("ignore")


# -Extract data

# In[3]:


df = pd.read_excel("C:/Users/Lenovo/Documents/archive/vehicles.xlsx")
df.head() # preview rows


# -Assess data

# In[4]:


print(df.info())  #information about the dataset


# In[5]:


print(df.head())  # Display the first few rows of the dataset


# In[6]:


print(df.isnull().sum())     # missing values


# In[7]:


print(df.describe())     # Summary statistics


# In[8]:


print(df.duplicated().sum())      #duplicates values


# In[9]:


# Check unique values in categorical columns
print(df['manufacturer'].unique())


# In[10]:


print(df['condition'].unique())


# In[11]:


print(df['fuel'].unique())


# -Cleaning data 

# In[12]:


df.drop_duplicates(inplace=True)    # Remove duplicates


# -Handle missing values 
# -Filling missing values with a placeholder or removing them

# In[13]:


df['condition'].fillna('unknown', inplace=True)


# In[14]:


df.dropna(subset=['price', 'year', 'manufacturer'], inplace=True)


# In[15]:


# Correct data types
df['price'] = df['price'].astype(float)


# In[16]:


df['year'] = df['year'].astype(int)


# In[17]:


df = df[df['price'] < df['price'].quantile(0.99)]    #Remove outliers


# EDA

# 1-What are the most common car manufacturers in the dataset?

# In[18]:


df['manufacturer'].value_counts().head(10)


# 2-What is the average price of vehicles by manufacturer?

# In[19]:


df.groupby('manufacturer')['price'].mean().sort_values(ascending=False)


# 3-What is the distribution of vehicle conditions?

# In[20]:


df['condition'].value_counts()


# 4-How does price vary by vehicle type?

# In[21]:


df.groupby('type')['price'].mean().sort_values(ascending=False)


# 5-What is the relationship between the year of the vehicle and its price?

# In[22]:


df.plot.scatter(x='year', y='price')


# 6-Which cities have the highest average vehicle prices?

# In[23]:


df.groupby('state')['price'].mean().sort_values(ascending=False).head(10)


# 7-What are the most common vehicle types listed?

# In[24]:


df['type'].value_counts().head(10)


# 8-Which car models are listed most frequently?

# In[25]:


df['model'].value_counts().head(10)


# 9-What is the distribution of mileage across different vehicle types?

# In[27]:


df.groupby('type')['odometer'].mean().sort_values(ascending=False)


# 10-How does fuel type affect the price of vehicles?

# In[28]:


df.groupby('fuel')['price'].mean().sort_values(ascending=False)


# 11-Are certain vehicle conditions associated with higher prices?

# In[29]:


df.groupby('condition')['price'].mean().sort_values(ascending=False)


# 12-What is the trend in vehicle prices over different years?

# In[30]:


df.groupby('year')['price'].mean().plot()


# *Thanks*

# In[ ]:




