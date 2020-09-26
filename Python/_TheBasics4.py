#!/usr/bin/env python
# coding: utf-8

# In[2]:


def times2(var): # Funct review
    return var*2


# In[3]:


times2(5)


# In[5]:


seq=[1,2,3,4,5]


# In[6]:


map(times2, seq) # You can pass in a funct, and the seq


# In[7]:


list(map(times2,seq)) # To print this out, you have to return it as a list.


# In[8]:


lambda var: var*2 # Lambda expression of the funct above


# In[9]:


t = lambda var: var*2 # Lambda expression of the funct above


# In[10]:


t(6)


# In[12]:


list(map(lambda num: num*3,seq)) #Lambda experssion for map / instead of passing a funct


# In[13]:


filter(lambda num: num%2 == 0, seq) #creates the filter


# In[15]:


list(filter(lambda num: num%2 == 0, seq)) # Prints out the filtered seq


# In[19]:


s = 'hello my name is Sam'


# In[20]:


s.lower() # Lowers everything in a string.


# In[21]:


s.lower #Asks about the function lower, you need () to activate the function


# In[22]:


s.upper()


# In[24]:


s.split() #Splits all the white space


# In[25]:


tweet = 'Go Sports! #Sports'


# In[26]:


tweet.split()


# In[27]:


tweet.split('#') #Splits at hastag instead


# In[29]:


tweet.split('#')[1] # Just grab the hashtag only


# In[30]:


d = {'k1':1, 'k2':2}


# In[31]:


d.keys() # Returns the keys of the dict


# In[32]:


d.items() # Returns the item and key


# In[33]:


d.values() # Only gives the values


# In[38]:


lst = [1,2,3]


# In[39]:


lst.pop() # Returns last item on the list - this will update the list


# In[40]:


lst


# In[41]:


lst = [1,2,3,4,5]


# In[42]:


item = lst.pop() # Insert the last item on the list to the item


# In[45]:


lst # Show the List


# In[46]:


item # Item has the value 5


# In[47]:


first = lst.pop(0) # Pop a certain index and store it into first


# In[48]:


lst


# In[50]:


first # First now has 1


# In[51]:


lst.append('new') # As before, this will add at the end of the list


# In[52]:


lst


# In[53]:


'x' in [1,2,3] # Is x in this list?


# In[54]:


'x' in ['x','y','z']


# In[57]:


x = [(1,2),(3,4),(5,6)] # Touples in a list


# In[58]:


x


# In[59]:


x[0] # Grab the Touple at Index 0


# In[61]:


for item in x: # Touple unpacking
    print(item)


# In[62]:


for (a,b) in x:
    print(a)


# In[63]:


for (a,b) in x:
    print(b)


# In[64]:


for (a,b) in x:
    print(a)
    print(b)


# In[ ]:




