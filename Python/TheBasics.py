#!/usr/bin/env python
# coding: utf-8

# In[65]:


1 # Just a number 1


# In[66]:


1.0 # Floating Number


# In[67]:


1 + 1 # Basic Math functions: Addition


# In[68]:


1 * 3 # Multipacation


# In[69]:


1 / 2 # Divide - Python 3 above will give back float.


# In[70]:


2 ** 4 # To the power of 


# In[17]:


2 + 3 * 5 + 5 # Will use PEMDAS


# In[18]:


(2 + 3) * (5 + 5) # PEMDAS


# In[19]:


4 % 2 # Module, 4 / 2 is 2 remainder 0


# In[20]:


5 % 2 # remainder 1


# In[21]:


8 % 2 # remainder 0


# In[71]:


var  = 2 # Set var with 2


# In[72]:


var # Will display the contents of var


# In[73]:


x = 2 # Inits
y = 3


# In[74]:


x + y # Basic Math


# In[75]:


x = x+x # Will add 2 + 2


# In[76]:


x # X will now be 4


# In[29]:


x


# In[77]:


x = x + x # 4 + 4


# In[78]:


x # X is now 8


# In[32]:


name_of_var = 12


# In[34]:


# Strings


# In[35]:


' single quote '


# In[36]:


"this is a string"


# In[79]:


"I can't go" # Wrap around "" if you need to use single quote and vice versa


# In[80]:


x = 'hello' # Init


# In[39]:


x


# In[64]:


print(x) # will print x


# In[63]:


num = 12 # Init num with 12
name = 'Sam' # Init name with Sam


# In[62]:


print('My number is {} and my name is {}'.format(num,name)) # One way to format


# In[61]:


print('My number is {one} and my name is {two}, more {one}'.format(one=num,two=name)) # Best way to format


# In[60]:


s = 'hello' # Create a string that contains hello


# In[59]:


s[0] # Grab at index 0


# In[58]:


s[4] # Grab at index 4


# In[81]:


s = 'abcdefghijk' # Init


# In[57]:


s[0:] # Grab at index 0 and forward


# In[56]:


s[:3] # Up to but not including


# In[84]:


s[3:6] # Start at Index 3 and end (not include) at 6


# In[86]:


[1,2,3] # This is a list


# In[88]:


['a','b','c'] # Also a list


# In[89]:


my_list = ['a','b','c']


# In[90]:


my_list.append('d') # Adds to the end of the list


# In[91]:


my_list


# In[92]:


my_list[0]


# In[94]:


my_list[1:3] # Index notation can be applied to lists


# In[95]:


my_list[0] = 'NEW' # Overwrites 'a'


# In[96]:


my_list


# In[97]:


nest = [1,2,[3,4]] # List inside a list


# In[98]:


nest[2] # grab the list inside


# In[99]:


nest[2][1] # Grab within a nested list


# In[102]:


nest = [1,2,3,[4,5,['target']]] # Init


# In[103]:


nest[3] # Grabs the List inside a list


# In[105]:


nest[3][2] # Grabs the list inside a list inside of another list!


# In[106]:


nest[3][2][0] # Grabs inside the third list - notice no [ ]


# In[108]:


print(nest[3][2][0]) # Prints the content inside a list, inside a list, at index 0


# In[ ]:




