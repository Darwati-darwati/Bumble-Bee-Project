#!/usr/bin/env python
# coding: utf-8

# # Highly divisible triangular number
# 

# ### Problem

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# Let us list the factors of the first seven triangle numbers:
# 
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28
# 
# We can see that 28 is the first triangle number to have over five divisors.
# 
# What is the value of the first triangle number to have over five hundred divisors?
# 

# ### Solution

# In[2]:


def triangleNumber(n):
    return sum ( [ i for i in range(1, n + 1) ] )
j = 0 
n = 0
numberOfDivisors = 0

while numberOfDivisors <= 500:
    numberOfDivisors = 0
    j += 1
    n = triangleNumber(j)
    i = 1
    while i <= n**0.5:
        if n % i == 0:
            numberOfDivisors += 1
        i += 1
    numberOfDivisors *= 2
print (n)
