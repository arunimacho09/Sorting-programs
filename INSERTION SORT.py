#!/usr/bin/env python
# coding: utf-8

# In[1]:


def insertion_sort(i_list):
    #First element is considered to be sorted and start with the 2nd element
    for i in range(1,len(i_list)):
        j=i
        #The values are looped and swapped based on the condition given
        while j>0 and i_list[j]<i_list[j-1]:
            i_list[j],i_list[j-1]=i_list[j-1],i_list[j]
            #Loop will continue checking if the previous element position is correct
            j=j-1
    return i_list
i_list=[34,78,3,245,0,55,223,6666,8,9,23]
s=insertion_sort(i_list)
print(s)
            
            


# In[ ]:




