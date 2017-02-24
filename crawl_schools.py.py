
# coding: utf-8

# In[11]:

import pandas as pd
import numpy as np
import html5lib
from bs4 import BeautifulSoup
import urllib
import pprint
import re
import sys
import string
import subprocess


# In[12]:

reload(sys)
sys.setdefaultencoding('utf-8')


# In[13]:

school = "https://www.fabert.com/etablissement-prive/2407/"

def refactor(word):
    return word.strip(" :")

the_school = pd.read_html(school,index_col=0)[1]
the_school.index = the_school.index.map(refactor)
the_school = the_school.transpose()
the_school

# Mettre en forme le tableau


# In[14]:

ecole = "https://www.fabert.com/etablissement-prive/2407/"
html = urllib.urlopen(ecole).read()
soup = BeautifulSoup(html, "lxml")

tags = soup('span',{ 'class' : 'encoded' })
for tag in tags:
    print tag['data-content']

print
print html


# In[15]:

# print(subprocess.check_output(["ls", "-l"]))
# subprocess.check_output(["echo", "maxime"])

decoded = []

for tag in tags:
    code = tag["data-content"]
#     print type(code)
    decoded.append(subprocess.check_output(
        ["node", 
         "max.js", 
         code
        ]))

adresses = []
for dec in decoded:
#     print re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",dec)
    adresses += re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",dec)
    
adresses = set(adresses)
adresses = list(adresses)
print adresses
    
# subprocess.check_output(["node", "encode.js", "PGEgcmVsPSJub2ZvbGxvdyIgaHJlZj0iL3RyYWNrLzU0MzMvZW1haWwuaHRtbD9lbWFpbD1zdG1hbmRlLnBpY3B1cyU0MGZyZWUuZnIiPnN0bWFuZGUucGljcHVzQGZyZWUuZnI8L2E+"])

# os.system("echo maxime")


# In[16]:

the_school.columns


# In[17]:

# len(adresses)
# adresses = ["sgwsgsdg","sadfaf","saegagag"]
print(len(adresses))
if len(adresses) == 1:
    the_school.set_value(1, "Mail :", adresses[0])
elif len(adresses) > 1:
    count = 0
    for adresse in adresses:
        if count == 0:
            the_school.set_value(1, "Mail", adresses[0])
        else:
            the_school.set_value(1, "Mail "+str(count+1), adresses[count])
        count+=1

the_school


# In[106]:

# Add to a global csv file
# the_school.to_csv("csv_test.csv")


# In[110]:

# Rajouter le titre
title = soup.title.string
print(title)

# the_school.index = [title]
the_school["Nom"] = title
# the_school
cols = the_school.columns
print cols
# df.rename(index=str, columns={"A": "a", "B": "c"})



# In[18]:

# Mettre option csv
the_school.to_csv("hello.csv")


# In[ ]:

# save to db
# SQLite


