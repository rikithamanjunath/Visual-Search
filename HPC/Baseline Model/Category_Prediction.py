
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import keras 
import tensorflow as tf

import numpy as np 
import pandas as pd
from scipy.misc import imread
import cv2
import os

from keras.models import model_from_json


# In[17]:


def cnn(json_path,model_path,image_path,query_path):
    
    # load json and create model
    json_file = open(json_path, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights(model_path)
    print("Loaded model from disk")
    
    # Extract Category Names
    id_to_label = {}
    cnt =0
    for folder in os.listdir(image_path):
        if ".DS_Store" not in folder:
            id_to_label[cnt]=folder
            cnt = cnt+1
    print("Categories",id_to_label)
    
    # Import query image
    IMG_SIZE = 64
    test_image = []
    Categories_Predicted = 3
    
    # Preprocess Query Image
    img = cv2.imread(query_path,cv2.IMREAD_COLOR)
    im = imread(query_path,mode = "RGB")
    plt.imshow(im)
    plt.show()
    img = cv2.resize(img,(IMG_SIZE,IMG_SIZE))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    test_image.append(img)
    test_image = np.array(test_image)
    #test_label = np.array(test_label)
    test_image.shape
    #test_label.shape
    X_test = test_image
    #Normalizing
    X_test = X_test/255
    #print(X_test.shape)
    #plt.imshow(X_test[0])
    
    # evaluate loaded model on test data
    loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    
    prob = loaded_model.predict(X_test)
    l = prob.tolist()
    prob_list = []
    count = 0

    for i in l:
        for j in i:
            prob_list.append((j,count))
            count = count+1

   
    # will be sorted in ascending order
    prob_list = sorted(prob_list,reverse = True)
    print("Probabilities of image belonging to each category:\n",prob_list)
    
    # picking top n categories or you can put a threshold value to pick the catgeories
    cat_pred = prob_list[:3]

    Y_pred_class = [];
    
   

    for i in range(len(cat_pred)):
        
        Y_pred_class.append((cat_pred[i][0], id_to_label[cat_pred[i][1]]))

    return Y_pred_class

