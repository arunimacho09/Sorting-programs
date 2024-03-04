#!/usr/bin/env python
# coding: utf-8

# In[9]:


def merge_sort(m_list):
    #List should have more than one element
    if len(m_list)>1:
        #The list gets divided into halves here
        a=len(m_list)//2
        a1= m_list[a:]
        a2= m_list[:a]
        #Sorting the divided list elements
        merge_sort(a1)
        merge_sort(a2)
        #Assingning position to the the divided list and main list
        i=0
        j=0
        k=0
        #Loop will go through both the sets
        while i<len(a1) and j<len(a2):
            #If a1 element is smaller it is out in the main list,if not a2 element is
            if a1[i] < a2[j]:
                m_list[k] = a1[i]
                i+=1
            else:
                m_list[k] = a2[j]
                j+=1     
            k+=1
        # When all the elements of a1 and a2 are done we sort the other left elements
        while i<len(a1):
            m_list[k]=a1[i]
            i+=1
            k+=1
        while j < len(a2):
            m_list[k]=a2[j]
            j+=1
            k+=1
                
m_list = [10, 9, 2, 4, 6,300]
merge_sort(m_list)
print(m_list)
        

    


# In[ ]:




