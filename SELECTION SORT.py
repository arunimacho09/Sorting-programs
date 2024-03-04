#!/usr/bin/env python
# coding: utf-8

# In[1]:


def selection_sort(s_list):
    #Looping through all the elements of the list
    for i in range(len(s_list)):
        #Setting first element as the minimum value
        min_value = i
        #Looping through the alements next to the minimum value
        for j in range(i+1,len(s_list)):
            #Setting the minimum value after comparison and putting it in the right position
            if s_list[j] < s_list[min_value]:
                min_value = j
        s_list[i],s_list[min_value]=s_list[min_value],s_list[i]
    return s_list

s_list=[80,675,8,9,0,7,90,567,4]
s=selection_sort(s_list)
print(s)
        
    
            
    


# In[ ]:




