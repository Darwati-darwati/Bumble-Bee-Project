#!/usr/bin/env python
# coding: utf-8

# # Power Digit Sum

# ### Problem

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^1000?
# 

# ### Solution

# In[1]:


print("Input n : ")
a = int(input())
print("Input power of n :")
b = int(input())
def power(a,b) :
    return a**b

result = 0
for i in str(power(a,b)) :
    result+=int(i)
    
print("Sum of the digits of the number %d power %d is %d" % (a,b,result))

