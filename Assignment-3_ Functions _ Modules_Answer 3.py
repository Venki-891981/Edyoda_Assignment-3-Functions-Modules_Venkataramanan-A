#!/usr/bin/env python
# coding: utf-8

# # Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# 
# # Sample String : 'The quick Brow Fox'
# 
# # Expected Output :
# 
# # No. of Upper case characters : 3
# 
# # No. of Lower case Characters : 12

# In[3]:


value = input("Please enter a string: ")

def ul_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

ul_test(value)

