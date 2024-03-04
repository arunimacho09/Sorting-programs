#!/usr/bin/env python
# coding: utf-8

# In[2]:


def partition_value(q_list,low,high):
    #choosing the last position element as pivot
    pivot = q_list[high]
    pos = low -1
    #Looping through the elements
    for i in range(low,high):
        #Cpmaring with pivot value
        if q_list[i] <=pivot:
            #Position is swapped if condition is met
            pos+=1
            q_list[pos],q_list[i]=q_list[i],q_list[pos]
    #Swapping the pivot element with the next biggest element by position
    q_list[pos+1],q_list[high]=q_list[high],q_list[pos+1]
    #Returning the position of partion
    return pos+1
def quick_sort(q_list,low,high):
    if low < high:
        #Finding the pivot 
        par=partition_value(q_list,low,high)
        #Sorting the left and right side of the partition:
        quick_sort(q_list,low,par-1)
        quick_sort(q_list,par+1,high)
q_list=[240,6,7,100,200,41,8]
list_len=len(q_list)
quick_sort(q_list,0,list_len-1)
print(q_list)
    


# In[ ]:




