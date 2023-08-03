#!/usr/bin/env python
# coding: utf-8

# # Write a Python function to sum all the numbers in a list.
# 
# # Sample List : (8, 2, 3, 0, 7)
# 
# # Expected Output : 20
# 
# 
# # Explanation:
# 
# # Summation should like 8+2+3+0+7 = 20

# In[47]:


value = eval(input("Please enter a list of numbers:"))
numbers = list(value)
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

s=sum(numbers)
y = '+'.join(map(str, numbers))
print(y,"=", s)


# In[ ]:




