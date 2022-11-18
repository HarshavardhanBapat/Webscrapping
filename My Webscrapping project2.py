#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs


# In[2]:


import requests


# In[3]:


link = "https://www.flipkart.com/hp-pavilion-ryzen-5-hexa-core-amd-r5-5600h-8-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-3050-144-hz-15-ec2145ax-gaming-laptop/p/itmbb28e8f26e4d1?pid=COMG92FXBNZSKYBD&lid=LSTCOMG92FXBNZSKYBDB8CIDK&marketplace=FLIPKART&q=laptop&store=6bo%2Fb5g&srno=s_1_20&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&iid=ec937454-5ee6-4d9c-84a5-22b07e38f6e1.COMG92FXBNZSKYBD.SEARCH&ssid=mhmtujxe0w0000001668677075235&qH=312f91285e048e09"


# In[4]:


page=requests.get(link)


# In[5]:


page


# In[6]:


page.content


# In[8]:


soup=bs(page.content,"html.parser")
soup


# In[9]:


print(soup.prettify())


# # Title of The Product:-

# In[10]:


title=soup.title


# In[11]:


print(type(soup))


# In[12]:


print(type(title))


# In[13]:


print(title.string)


# In[15]:


price=soup.find_all("div",class_="_30jeq3 _16Jk6d")
print(price)


# In[16]:


product_price=[]
for i in range(0,len(price)):
    product_price.append(price[i].get_text())
product_price


# # Get all Customer Name:-

# In[17]:


name=soup.find_all("p",class_="_2sc7ZR _2V5EHH")
name


# In[18]:


cust_name=[]
for i in range(0,len(name)):
    cust_name.append(name[i].get_text())
cust_name


# In[19]:


comment=soup.find_all("p",class_="_2-N8zT")
comment


# In[20]:


cust_comment=[]
for i in range(0,len(comment)):
    cust_comment.append(comment[i].get_text())
cust_comment


# In[21]:


star=soup.find_all("div",class_="_3LWZlK _1BLPMq")
star


# In[22]:


cust_star=[]
for i in range(0,len(star)):
    cust_star.append(star[i].get_text())
cust_star


# In[24]:


review=soup.find_all("div",class_="t-ZTKy")
review


# In[25]:


cust_review=[]
for i in range(0,len(review)):
    cust_review.append(review[i].get_text())
cust_review


# In[26]:


import pandas as pd


# In[27]:


df=pd.DataFrame()
df["Customer_Name"]=cust_name
df["Comment"]=cust_comment
df["Review"]=cust_review
df["Stars"]=cust_star
df


# In[ ]:




