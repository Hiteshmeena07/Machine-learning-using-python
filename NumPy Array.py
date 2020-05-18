#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Single dimensional array

import numpy as np

n1 = np.array([10,20,30,40])
n1


# In[4]:


# Multi dimensional array

import numpy as np

n2 = np.array([[10,20,30,40],[50,60,70,80]])
n2


# In[7]:


#type
type(np.array)


# In[10]:


# Initilization Numpy array with zero

import numpy as np
n1 = np.zeros((2,4))
n1


# In[19]:


import numpy as np
n2 = np.ones((3,5))
n2


# In[23]:


#Initilization Numpy array with Same number

import numpy as np
n1 = np.full((3,3),4)
n1


# In[24]:


#Initilization Numpy array withim the range

import numpy as np
n1 = np.arange(10,20)
n1


# In[26]:


# Initilization Numpy array within the range with Gap

import numpy as np
n1 = np.arange(10,50,5)   #(initial value,final value, gap)
n1


# In[8]:


#Initilization of Numpy array with random numbers

import numpy as np
n1 = np.random.randint(1,100,5) #(intital,final,no of random varibale)
n1


# In[13]:


# checking the shape of Numpy array

import numpy as np
n1 = np.array([[1,2,3],[4,5,6]])
n1.shape


# In[14]:


# changing the shape of numpy array

n1.shape = (3,2)
n1.shape


# In[15]:


# Joining the array
# vertically

import numpy as np
n1 = np.array([10,20,30])
n2 = np.array([40,50,60])

np.vstack((n1,n2))


# In[17]:


# joining numpy array
#horizontally

import numpy as np
n1 = np.array([10,20,30])
n2 = np.array([40,50,60])

np.hstack((n1,n2))


# In[18]:


# joining Numpy Array
# Column wise

import numpy as np
n1 = np.array([10,20,30])
n2 = np.array([40,50,60])

np.column_stack((n1,n2))


# In[19]:


# Intersection of Numpy array

import numpy as np
n1 = np.array([10,20,30,40,50])
n2 = np.array([40,50,60,70,80,90])

np.intersect1d(n1,n2)


# In[20]:


# Difference of Numpy array

import numpy as np
n1 = np.array([10,20,30,40,50])
n2 = np.array([40,50,60,70,80,90])

np.setdiff1d(n1,n2)


# In[23]:


# Addition of Numpy array

import numpy as np
n1 = np.array([10,20]) #n1 = np.array([10,20],axis=0)  for column
n2 = np.array([40,50]) #n2 = np.array([40,50],axis =1) for row

np.sum([n1,n2])


# In[ ]:




