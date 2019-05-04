#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import keras 
import tensorflow as tf
import numpy as np 
import pandas as pd
from scipy.misc import imread  
import cv2
import os
from joblib import load

from keras.preprocessing import image
from keras.applications import MobileNet
from keras.applications.mobilenet import preprocess_input


# In[17]:


def mobilenet_prediction(model_path,query_path):
    

    model = MobileNet(weights='imagenet', include_top=False)

    #Extract features of Query Image
    imgq = image.load_img(query_path, target_size=(224, 224))
    img_dataq = image.img_to_array(imgq)
    img_dataq = np.expand_dims(img_dataq, axis=0)
    img_dataq = preprocess_input(img_dataq)
    mnet_feature_query = model.predict(img_dataq)
    mnet_feature_np_query = np.array(mnet_feature_query)
    mnet_feature_np_query = mnet_feature_np_query.flatten()

    listOfInput = [mnet_feature_np_query]


    loaded_model = load(model_path)


    probs = loaded_model.predict_proba(listOfInput)[:,:]
    
    print("probs", probs)
    #loaded_model.predict(listOfInput)
    
    #probs = model.predict_proba(listOfInput)
    
    category = []
    classes = loaded_model.classes_

    for index in range(len(classes)):
        category.append((probs[0][index],classes[index]))
        
    final_category = sorted(category, key=lambda x: x[0], reverse=True)
    
    return final_category[:3]


# In[ ]:




