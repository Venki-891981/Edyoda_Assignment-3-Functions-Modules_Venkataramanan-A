#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to reverse a string.
# 
# # Sample String : "1234abcd"
# 
# # Expected Output : "dcba4321"

# In[3]:


value = input("Please enter a string: ")

def rev_string(x):
    return x[::-1]

y = rev_string(value)

print(y)


# In[ ]:




