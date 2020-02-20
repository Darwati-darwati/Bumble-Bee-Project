#!/usr/bin/env python
# coding: utf-8

# # Smallest Multiple

# ### Problem

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 
# 

# ### Solution

# In[1]:


import fractions
def habis(n): 
    ans = 1    
    for i in range(1, n + 1): 
        ans = (ans * i)/fractions.gcd(ans, i)         
    return ans
n=20
print (habis(n))

