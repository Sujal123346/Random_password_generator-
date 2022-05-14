#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing Libraries

from tkinter import *
import random, string


# In[2]:


#initialize window

root =Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("DataFlair - PASSWORD GENERATOR")


# In[3]:


#heading
heading = Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(root, text ='DataFlair', font ='arial 15 bold').pack(side = BOTTOM)


# In[4]:


###select password length
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 6, to_ = 32 , textvariable = pass_len , width = 15).pack()


# In[5]:


#define function

pass_str = StringVar()

def Generator():
    password = ''
    for x in range(pass_len.get()):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


# In[6]:


###button

Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()


# In[7]:


# loop to run program
root.mainloop()


# In[ ]:




