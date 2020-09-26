#!/usr/bin/env python
# coding: utf-8

# In[4]:


d = {'key1':'value','key2':123} # Init Dict


# In[2]:


d['key1'] # Get the content that belongs to that key


# In[5]:


d['key2']


# In[6]:


d = {'k1':[1,2,3]} # List inside a Dict


# In[7]:


d['k1']


# In[8]:


d['k1'][1] # You can grab within the list


# In[9]:


my_list = d['k1'] # Init inside contents of a dict to a variable (In this case a list)


# In[10]:


my_list # Is now a list


# In[11]:


my_list[0] 


# In[13]:


d = {'k1':{'innerkey':[1,2,3]}} # Nested Dict


# In[14]:


d['k1'] # Grab the dict inside the nested dict


# In[15]:


d['k1']['innerkey'] # Grab the contents inside the dict thats inside a dict


# In[16]:


d['k1']['innerkey'][1] # Grab a value from a list thats inside a nested dict


# In[17]:


True # Boolean Value


# In[18]:


False


# In[19]:


my_list = [1,2,3]


# In[20]:


my_list[0]


# In[21]:


t = (1,2,3) # This is a Tuple


# In[22]:


t[0]


# In[23]:


my_list[0] = 'NEW' # The main difference between a Tuple and a list


# In[24]:


my_list


# In[27]:


t[0] = 'NEW' # Tuples are immutable / Lists are not and we can change values inside (Tuple are used when you don't want the user to change the items)


# In[29]:


{1,2,3} # Init a set


# In[30]:


{1,1,1,2,2,2,3,3,3} # Set's are defiend by only unique elements


# In[35]:


set([1,1,1,1,2,2,2,5,5,5,6,6,6]) # You can call a set and pass in a list to return the unique elements in the list


# In[36]:


s = {1,2,3} # Init a set


# In[37]:


s.add(5) # Add to a set


# In[34]:


s


# In[38]:


s.add(5)


# In[40]:


s # Only one unique element in a set, so 5 will not add nor give an error


# In[41]:


1 > 2 # Is 1 greater than 2? (Comparison Operators)


# In[42]:


1 < 2 


# In[43]:


1 >= 2


# In[44]:


1 <= 2


# In[45]:


1 == 1


# In[46]:


1 = 1 # this is a variable assignment not a Comparison (Use two ==)


# In[47]:


1 != 3 # 1 is not equal to 3


# In[49]:


'hi' == 'bye'


# In[50]:


'hi' != 'bye'


# In[51]:


1 < 2 and 2 < 3 # Logical Operators


# In[52]:


1 < 2 and 2 > 3


# In[53]:


(1 < 2) and (2 > 3) # Adding () makes the code more readable


# In[54]:


(1 < 2) or (2 > 3)


# In[61]:


(1 < 2) or (2 > 3) or (1 == 1)


# In[56]:


True and True


# In[57]:


True and False


# In[58]:


True or False


# In[60]:


if (1 < 2):   # Conditionals
    print('yep!')


# In[62]:


if True:
    print('Perform code')


# In[64]:


if True:
    x = 2 + 2


# In[65]:


x


# In[70]:


if (1 == 2): # False
    print('First')
else:
    print('Last')


# In[69]:


if (1 == 2): # False
    print('First')
elif (3 == 3): # True
        print('Middle')
else:
    print('Last')


# In[ ]:




