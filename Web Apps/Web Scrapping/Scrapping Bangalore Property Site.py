#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup


# In[4]:


r=requests.get('http://www.mybangaloreproperty.com/Properties_For_Sale/page_1420922.html')
c=r.content


# In[5]:


soup=BeautifulSoup(c,'html.parser')


# In[6]:


all=soup.find_all('tr',{'class':'Item'})


# In[7]:


all


# In[8]:


all[0].find('td',{'align':'right'})


# In[9]:


type(all[0].find('td',{'align':'right'}))


# In[10]:


spans=all[0].find('td',{'align':'right'}).find('span')
spans


# In[11]:


type(spans)


# In[12]:


print(spans.text)


# In[25]:


for item in all:
    spans1=item.find('td',{'align':'right'}).find('span')
    spans1
    print(spans1.text)


# In[15]:


all1=soup.find_all('tr',{'class':'AlternatingItem'})
for item in all1:
    spans2=item.find('td',{'align':'right'}).find('span')
    #spans1
    print(spans2.text)


# In[44]:


all[0].find('td', {'class':'Address'}).find_all('span')
#print(add)
#all[0].find('td', {'class':'Address'}).find_all('span').text


# In[38]:


all[0].find('td', {'class':'Address'})


# In[56]:


for item in all:
    add=item.find('td', {'class':'Address'}).find_all('span')[0]
    #spans1
    print(add.text)
    try:
        condition=item.find('td', {'class':'Address'}).find_all('span')[1]
        print(condition.text)
    except:
        pass
    print('')


# In[57]:


for item in all1:
    add=item.find('td', {'class':'Address'}).find_all('span')[0]
    #spans1
    print(add.text)
    try:
        condition=item.find('td', {'class':'Address'}).find_all('span')[1]
        print(condition.text)
    except:
        pass
    print('')


# In[91]:


for item in all:
    style=item.find('td', {'align':'center', 'class':''}).find('span')
    #spans1
    print(style.text)
    try:
        beds=item.find_all('td', {'align':'center', 'class':''})[1].find('span')
        print(beds.text)
    except:
        print('None')
    try:
        size=item.find_all('td', {'align':'center', 'class':''})[2].find('span')
        print(size.text)
    except:
        print('None')
    print('')


# In[92]:


for item in all1:
    style=item.find('td', {'align':'center', 'class':''}).find('span')
    #spans1
    print(style.text)
    try:
        beds=item.find_all('td', {'align':'center', 'class':''})[1].find('span')
        print(beds.text)
    except:
        print('None')
    try:
        size=item.find_all('td', {'align':'center', 'class':''})[2].find('span')
        print(size.text)
    except:
        print('None')
    print('')


# In[96]:


li=[]
for item in all:
    d={}
    d['price']=item.find('td',{'align':'right'}).find('span').text
    d['address']=item.find('td', {'class':'Address'}).find_all('span')[0].text
    d['style']=item.find('td', {'align':'center', 'class':''}).find('span').text
    try:
        d['beds']=item.find_all('td', {'align':'center', 'class':''})[1].find('span').text
    except:
        d['beds']='None'
    try:
        d['size']=item.find_all('td', {'align':'center', 'class':''})[2].find('span').text
    except:
        d['size']='None'
    print('')
    li.append(d)
for item in all1:
    d={}
    d['price']=item.find('td',{'align':'right'}).find('span').text
    d['address']=item.find('td', {'class':'Address'}).find_all('span')[0].text
    d['style']=item.find('td', {'align':'center', 'class':''}).find('span').text
    try:
        d['beds']=item.find_all('td', {'align':'center', 'class':''})[1].find('span').text
    except:
        d['beds']='None'
    try:
        d['size']=item.find_all('td', {'align':'center', 'class':''})[2].find('span').text
    except:
        d['size']='None'
    print('')
    li.append(d)

len(li)


# In[100]:


import pandas
df=pandas.DataFrame(li)


# In[101]:


df


# In[102]:


df.to_csv('output.csv')


# In[105]:


li1=[]
for item in all:
    d={}
    p=(item.find('td',{'align':'right'}).find('span').text).replace('Rs','')
    p=p.replace(' INR','')
    d['price']=int(p.replace(',',''))
    d['address']=item.find('td', {'class':'Address'}).find_all('span')[0].text
    d['style']=item.find('td', {'align':'center', 'class':''}).find('span').text
    try:
        d['beds']=item.find_all('td', {'align':'center', 'class':''})[1].find('span').text
    except:
        d['beds']=None
    try:
        d['size']=item.find_all('td', {'align':'center', 'class':''})[2].find('span').text
    except:
        d['size']=None
    print('')
    li1.append(d)
for item in all1:
    d={}
    p=item.find('td',{'align':'right'}).find('span').text.replace('Rs','')
    p=p.replace(' INR','')
    p=int(p.replace(',',''))
    d['price']=int(p.replace(',',''))
    d['address']=item.find('td', {'class':'Address'}).find_all('span')[0].text
    d['style']=item.find('td', {'align':'center', 'class':''}).find('span').text
    try:
        d['beds']=item.find_all('td', {'align':'center', 'class':''})[1].find('span').text
    except:
        d['beds']=None
    try:
        d['size']=item.find_all('td', {'align':'center', 'class':''})[2].find('span').text
    except:
        d['size']=None
    print('')
    li1.append(d)
li1


# In[107]:


df1=pandas.DataFrame(li1)
df1


# In[108]:


df1.to_csv('output1.csv')


# In[ ]:




