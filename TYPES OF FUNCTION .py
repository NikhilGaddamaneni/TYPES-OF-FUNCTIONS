#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#TYPES OF FUNCTION 
1.In-built Function 
2.Default Function 
3.Lambda Function 


# In[ ]:


#TYPES OF FUNCTION DECLARATION 
1.Default Argumnets 
2.Positional Arguments
3.keyword Arguments 
4.Arbitary Positionnal Arguments 
5.Arbitary Keyword Arguments


# In[2]:


#1.DEFAULT AGRUMNETS 
def one(a,b=10,c=80):
    return a+b+c 
print(one(10))


# In[3]:


#2.POSITIONAL ARGUMENTS 
def one(a,b,c): 
    return a+b+c 
print(one(10,20,30))


# In[4]:


#3.KEYWORD ARGUMNETS 
def one(name,roll): 
    return f"{name}:{roll}"
print(one("RAM",100))


# In[6]:


#4.ARBITARY POSTIONAL ARGUMNETS 
def one(*args): 
    count=0 
    for i in args:
        count+=i 
    return count 
print(one(10,20,30))


# In[7]:


#5.ARBITARY KEYWORD ARGUMNETS 
def one(**kwargs):
    for key,value in kwargs.items(): 
        print(f"{key}:{value}")
one(name='RAM',roll=100,year=2024)


# In[ ]:




