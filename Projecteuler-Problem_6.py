#!/usr/bin/env python
# coding: utf-8

# # Sum Square Difference

# ### Problem

# The sum of the squares of the first ten natural numbers is,
# 12+22+...+102=385
# 
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)2=552=3025
# 
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640
# 
# .
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# ### Solution

# In[1]:


batas = 100
b = 0
c = 0
for i in range (1,batas+1):
    k=i**2
    b+=k
    c+=i

d=c**2
e=d-b
print(b," ",d," ",e)

