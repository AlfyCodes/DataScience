#!/usr/bin/env python
# coding: utf-8

# In[3]:


seq = [1,2,3,4,5] 


# In[4]:


for item in seq: # Loops
    print(item)


# In[5]:


for jelly in seq: # The temp variable 'item' can be named anything like 'jelly'
    print(jelly)


# In[7]:


for num in seq: # The temp variable should be names something relatable to the code such as 'num'
    print(num)


# In[12]:


for num in seq: # You can also perform an action for the amount of seq
    print('hello')


# In[16]:


i = 1
# While Loop
while (i < 5):
    print('i is: {}'.format(i))
    i = i + 1 # Increment so we are not stuck in a forever loop


# In[17]:


for x in seq:
    print(x)


# In[18]:


range(0,5) # Range function


# In[21]:


for x in range(0,5): # Range is set to start at element 0 and go up to element 5 thus we get 0-4
    print(x)
    


# In[22]:


list(range(10)) # Range has 10 elements so that means it will contain 0 - 9


# In[23]:


x = [1,2,3,4] # List Comprehension


# In[25]:


out = []

for num in x:
    out.append(num**2)


# In[26]:


print(out)


# In[30]:


out = []


# In[31]:


out = [num**2 for num in x] # Same code as above


# In[32]:


print(out)


# In[33]:


def my_func(param1): # Functions
    print(param1)


# In[34]:


my_func('hello')


# In[35]:


def my_func2(name): # Pass in a param to print out the content
    print('Hello '+name)


# In[37]:


my_func2('Alfred')


# In[38]:


def my_func3(name='Default Name'): # Set a default incase no param is passed
    print('Hello '+name)


# In[39]:


my_func3() # When no param is passed you will get the 'Default Name' you've set inside the param of the func


# In[41]:


my_func3('Alfred') # Passing a param will return your name (in this case)


# In[48]:


def square(num):
    """
    This is a docstring.
    It can go multiple lines.
    This function squares a number.
    """
    return num**2 # Returns the param to the power of 2


# In[46]:


output = square(2)


# In[47]:


output


# In[49]:


# By typing 'square' then pressing tab right after, you can get the docstring screen to pop up


# In[ ]:


range


# In[ ]:




