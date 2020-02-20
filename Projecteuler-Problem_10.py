#!/usr/bin/env python
# coding: utf-8

# # Summation of primes

# ### Problem

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.
# 

# ### Solution

# In[ ]:


print("Entry the number : ")
a = int(input())
def isPrime(a) :
    prime_num = 0
    for i in range(2,a) :
        if (a%i) == 0 :
            return False
        else :
            prime_num = a

result = 0
for i in range(2,a):
    if isPrime(i) != False :
        result+=i

print("The sum of prime numbers under %d is %d" % (entry,result))

