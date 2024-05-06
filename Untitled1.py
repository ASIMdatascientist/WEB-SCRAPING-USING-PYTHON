#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

web = requests.get("https://www.iplt20.com/auction/2022")

web.status_code

web.content

web.url

soup = BeautifulSoup(web.content, 'lxml')
soup

heade= soup.find("table",class_="ih-td-tab auction-tbl")
title= heade.find_all("th")
print(title)

header=[]
for i in title:
  name=i.text
  header.append(name)
  df=pd.DataFrame(columns=header)
print(df)

rows = heade.find_all("tr")
rows

for i in rows[1:]:
  first_td= i.find_all("td")[0].find("div", class_="ih-pt-ic").text.strip()
  data = i.find_all("td")[1:]
  row = [tr.text for tr in data]
  row.insert(0,first_td)
  l=len(df)
  df.loc[l]=row
  print(df)



# In[5]:


directory = "C:/web scraping"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Now you can save the CSV file
df.to_csv("C:/web scraping/helloty.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:




