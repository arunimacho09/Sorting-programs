#!/usr/bin/env python
# coding: utf-8

# In[7]:


def bubble_sort(b_list):
    for i in range(len(b_list)):
        for j in range(0,len(b_list)-i-1):
            if (b_list[j] > b_list[j+1]):
                b_list[j],b_list[j+1] = b_list[j+1],b_list[j]
    return b_list
b_list=[34,78,3,245,0,55,223,6666,8,9,23]
s=bubble_sort(b_list)
print(s)
            


# In[ ]:




