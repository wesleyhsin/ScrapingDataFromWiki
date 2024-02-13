#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[3]:


print(soup)


# In[4]:


#specify what data we are looking for
soup.find_all('table')


# In[5]:


#or we can use soup.find
soup.find('table', class_ = 'wikitable sortable')


# In[6]:


table = soup.find_all('table')[1]


# In[7]:


print(table)


# In[8]:


#Get the titles and headers
soup.find_all('th')


# In[9]:


world_titles = table.find_all('th')


# In[10]:


world_titles


# In[11]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[12]:


import pandas as pd


# In[13]:


df = pd.DataFrame(columns = world_table_titles)
df


# In[14]:


column_data = table.find_all('tr')
#looping through tr (row of data)


# In[15]:


for row in column_data[1:]:
    row_data = row.find_all('td') #individual data (td)
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[16]:


df


# In[17]:


df.to_csv(r'C:\Users\wesle\Documents\Python Tutorials\Companies.csv', index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




