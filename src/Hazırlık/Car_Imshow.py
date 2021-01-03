#!/usr/bin/env python
# coding: utf-8

# In[11]:


import cv2
import numpy as np


# In[12]:


path = r"C:\Users\Administrator\Desktop\car.jpg"
resim = cv2.imread(path,0)


# In[13]:


cv2.imshow("araclar",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[4]:





# In[ ]:




