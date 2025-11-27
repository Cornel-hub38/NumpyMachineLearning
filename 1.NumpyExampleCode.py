#!/usr/bin/env python
# coding: utf-8

# In[6]:
#  This is a cell


# In[3]:


import numpy as  np


my_list = [1, 2, 3]
arr = np.array(my_list)

#arr


# In[4]:


print(my_list)


# In[8]:


#Numpy arrays   - scalars and vectors


# In[10]:


my_mat = [ [1, 2,3], [4,5,6], [7,8,9] ]
print(np.array(my_mat))


# In[11]:


bill = np.arange(0,10)
print(bill)


# In[13]:


# np.seroa(3) - print a vectr
np.zeros(3)


# In[14]:


#print another np scalar of 12 0s
print(np.zeros(12))


# In[16]:


print(np.zeros(12) + 4)


# In[17]:


#  now develop a matrix (5 x 5)
np.zeros((5,5))


# In[18]:


# create a (2r x 5c) matrix
np.ones((2,5))


# In[19]:


# linspace( start, stp, number of elements - with even sppacing between start and stop)
np.linspace(0, 5, 4)


# In[20]:


np.linspace(0, 5, 100)


# In[21]:


#  random numbers btween 0 and 1

np.random.rand(10)


# In[22]:


# for creatin of a 2D array  .....
carl = np.random.rand(6,4)
print("CARL: ", carl)


# In[23]:


bart = np.random.randint(5, 12, 35)
print(bart)


# In[24]:


# np.arange(25)
lisa = np.arange(25)
print(lisa)


# In[ ]:


lisasimpson = np.arange(22)
print("LisaSimpsn:  ", lisasimpson)
