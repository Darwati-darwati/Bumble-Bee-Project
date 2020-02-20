#!/usr/bin/env python
# coding: utf-8

# # Special Pythagorean Triplet

# ### Problem

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#                     a2 + b2 = c2
# 
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# 

# ### Solution

# In[1]:


from datetime import time


# In[2]:


import time


# In[3]:


start_time=time.time()


# In[4]:



def pythagorean_triplet_m_n():
    for n in range(1,1000):
        for m in range(1,n):
            a = n**2 - m**2
            b = 2*n*m
            c = n**2 + m**2
            if a+b+c == 1000:
                return a*b*c
print (pythagorean_triplet_m_n())
end_time = time.time()

print (end_time - start_time)

