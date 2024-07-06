#!/usr/bin/env python
# coding: utf-8

# In[99]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[100]:


data = pd.read_csv(r"C:\Users\hp\Downloads\amazon_prime_users.csv")


# In[101]:


data.head(2)


# In[102]:


data


# In[103]:


data.isnull().sum()


# In[104]:


data.shape


# In[105]:


data.info()


# In[106]:


data.columns


# In[107]:


data["User ID"].count()


# In[108]:


data[["Gender"]].value_counts()


# In[109]:


ax=sns.countplot(x="Gender", data=data)
ax.bar_label(ax.containers[0]);


# In[ ]:





# # Subscription Plan

# In[110]:


data["Subscription Plan"].value_counts()


# In[111]:


plt.figure(figsize=(8,5))
ax=sns.countplot(x="Subscription Plan", data=data, hue = 'Gender',width=0.2, )
ax.bar_label(ax.containers[0]);


# As per above analysis using countplot, it is observed that most of the people chose annual sbbscription plan of
# amazon prime because annual subcription plan was resonable than monthly pack.

# In[ ]:





# # Payment Information

# In[112]:


data["Payment Information"].value_counts()


# In[113]:


x=data["Payment Information"].value_counts().index


# In[114]:


y=data["Payment Information"].value_counts().values


# In[115]:


plt.pie(y, data=data,labels=x, autopct='%0.2f%%');


# As per above analysis using pieplot, it is observed that people use three type of payment mode like Mastercard, Amex, and Visa.
# As per analysis most of the people chose Mastercard for payment mode i.e.34.24%.

# # Rennewal Status

# In[116]:


data["Renewal Status"].value_counts()


# In[117]:


plt.figure(figsize=(8,5))
ax=sns.countplot(x='Renewal Status', data=data,orient='h',hue='Gender',width=0.2)
ax.bar_label(ax.containers[0]);


# As per above analysis using countplot, it is observed that people use two type of Renewal mode like Manual and Auto-renew.
# As per analysis most of the people chose Auto-renew for Renewal mode i.e.1274.

# # Favorite Genres

# In[118]:


data["Favorite Genres"].value_counts()


# In[119]:


plt.figure(figsize=(18,5))
ax=sns.countplot(x='Favorite Genres', data=data,orient='h',width=0.4)
ax.bar_label(ax.containers[0]);


# As per above analysis using countplot, it was observed that Horror was favorite Genres of the people i.e. 15% approx.

# # Devices Used

# In[120]:


data["Devices Used"].value_counts()


# In[121]:


plt.figure(figsize=(18,5))
ax=sns.countplot(x='Devices Used', data=data,orient='h',width=0.4)
ax.bar_label(ax.containers[0]);


# As per above analysis using countplot, it was observed that people used their smartphone device (34.68%)for amazon prime service.

# # Purchase History

# In[122]:


data["Purchase History"].value_counts()


# In[123]:


sns.countplot(x="Purchase History",data=data);


# As per above analysis, It was observed that people use the benefit of 
# Amazon prime user membership for purchasing the different category of product like Electronics, Books, Clothing.
# As per purched history books sales was more than the other two catogory. 
# 

# # Usage Frequency

# In[124]:


data["Usage Frequency"].value_counts()


# In[125]:


data["Usage Frequency"].value_counts()/data['User ID'].count()*100


# In[126]:


ax=sns.countplot(x="Usage Frequency",data=data)
ax.bar_label(ax.containers[0]);


# As per above analysis, 34.04% Frequent people use the amazon prime..
# 33.08% Regular people use the amazon prime.
# 32.88% Occasional people use the amazon prime.

# In[ ]:




