#!/usr/bin/env python
# coding: utf-8

# # Largest Palindrome Product

# ### Problem

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.
# 

# ### Solution

# In[1]:


print("Entry the numbers : ")
a = int(input())
b = int(input())
def largest_palindrom(a,b) :
    large_palindrom = 0
    for i in range(a,b) :
        for j in range(a,b) :
            multiple_result = i*j
            if str(multiple_result) == str(multiple_result)[::-1] :
                if multiple_result>large_palindrom :
                    large_palindrom = multiple_result
    print("The largest palindrom number between %d and %d is %d"  % (a,b,large_palindrom))

largest_palindrom(a,b)

