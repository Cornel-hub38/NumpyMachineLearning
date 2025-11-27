#!/usr/bin/env python
# coding: utf-8

# In[6]:
#  This is a cell
# In[3]:


import numpy as np


my_list = [1, 2, 3]
arr = np.array(my_list)

print(arr)


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
print("LINE_68 ", np.zeros((5,5)))


# In[18]:


# create a (2r x 5c) matrix
print(np.ones((2,5)))


# In[19]:


# linspace( start, stp, number of elements - with even sppacing between start and stop)
print(np.linspace(0, 5, 4))


# In[20]:


print(np.linspace(0, 5, 100))


# In[21]:


#  random numbers btween 0 and 1

print("Line_96 ::: np.random.rand(10) ",np.random.rand(10))
print("\n\n\n\n\n\n")

# In[22]:


# for creating of a 2D array  .....
carl = np.random.rand(6,4)
print(" Line 104 :  ", carl)
print("\n")

# In[23]:


bart = np.random.randint(5, 12, 35)
print(bart, "Line 111 \n")


# In[24]:


# np.arange(25)
lisa = np.arange(25)
print(lisa, "Line 119 \n  np.arange(25):: \n")


# In[27]:


lisasimpson = np.arange(22)
print("Line 126: \n", lisasimpson, "\n")


# In[30]:


# video18 Numpy arrays:  Python for Data Science and Machine Learning

#randint(start, stop, number-of-items)

joe = np.random.randint(93, 194, 27)
print("np.random.randint: ", joe)
print("\n")

# In[31]:


joe = np.random.randint(-33, 79, 70)
print(joe, "Line 144: \n")


# In[32]:


# What of randn - a standard normal distribution around zero
cocker = np.random.randn(12)
print("Line 152: ", "np.random.randn(12): \n", cocker)


# In[34]:


#  lets create a 1D array of 40 numbers between 2 and 98
randomarray = np.random.randint(2, 98, 40)
print("\n", randomarray, "Line 160\n")


# In[ ]:





# In[39]:


#  let's create a 1D array of 40 numbers between 2 and 98 and change th dtype to 64
randomarray = np.random.randint(2, 98, 40,)
print("np.random.randint(2, 98, 40) ", randomarray, "Line 174\n")


# In[40]:


randdommarray = np.random.randint(19,27, 52)
print("Line 181: ", randdommarray)


# In[43]:


#  the .reshape method  onrandonarray object

print("Line 189:  ", randomarray.reshape(5,8), "\n")



# In[45]:


print("Line 196 :\n ",randomarray.reshape(8, 5), "\n")

print("\n joe.min(): ", joe.min(), "Line 198 \n")
# In[48]:


onedimarray = np.random.randint(3,45, 20)
print("Line 203, np.random.randint(3, 45, 20)", onedimarray, "\n")


# In[49]:


print(" .min() \n", onedimarray.min(), "\n")


# In[50]:


print(" .max()", onedimarray.max(), "\n" )

#  indexing via argmin() and argmax()
print("INDEXINNG with argmax and argmin()")
print(" argmin()...... ", onedimarray.argmin(), "\nLine 219\n")
#print("\n")
print("ARGMAX()","\n")
print("argmax() .... indexing\n ", onedimarray.argmax(), "Line222\n")





