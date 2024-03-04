#!/usr/bin/env python
# coding: utf-8

# In[13]:


class SingletonClass:
    __instance__ = None
    
    @staticmethod
    def getInstance():
        if SingletonClass.__instance__ == None:
            SingletonClass.__instaance__ = SingletonClass()
            print("Singleton class")
        return SingletonClass.__instance__

    def __init__(self):
        print("init called")
        
    def someFunc(self):
        print("function called")
        
    
    
c=SingletonClass()
c2=c.getInstance()
c1=c.someFunc()


# In[ ]:




