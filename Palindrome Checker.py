#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Input the word
print("Please input your word:")
word=input()
word=word.casefold()
reversed_word=word[::-1]

if word == reversed_word:
    print("It's a Palindrome!!")
    
else:
    print("Regular Word")


# In[ ]:




