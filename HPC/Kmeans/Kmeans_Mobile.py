#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://www.kaggle.com/insaff/img-feature-extraction-with-pretrained-resnet
from keras.applications.mobilenet import MobileNet
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input
import numpy as np
import os
from scipy.misc import imread
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import time
import os.path
import pickle
from scipy.spatial import distance
from sklearn.cluster import KMeans
import pickle
import itertools

# In[2]:


model = MobileNet(weights='imagenet', include_top=False)


# In[3]:


def kmeans_model(pred_cats,image_path,pickle_path,query_path):
    
    model = MobileNet(weights='imagenet', include_top=False)
    
    #Reading Image Names from Predicted Categories
    image_names=[]
    
    for i in range(0,len(pred_cats)) :
        # Give the path of the semi trained dataset
        path = image_path +"/"+ pred_cats[i][1]
        for img_path in os.listdir(path):
            if('.DS_Store' not in os.path.join(path,img_path)):
                image_names.append(pred_cats[i][1]+"/"+img_path)
    
    print("image_names_len",len(image_names))            
    start = time.time()
    
    # Give the MobileNet pickle file path
    # retrieving features from pickle files of 3 predicted categories
     # Give the MobileNet pickle file path
    for i in range(3):
        pickled_db_path = pickle_path + pred_cats[i][1] + ".pck"
        with open(pickled_db_path, 'rb') as fp:
                temp = pickle.load(fp)   
        fp.close()
        if i == 0:
            mnet_loaded = temp
        else:
            mnet_loaded = np.append(mnet_loaded,temp,axis = 0)
    print("mnetloaded",mnet_loaded.shape)
    
    processed_pickle_images = []
    
    # Give the MobileNet pickle file path
    for i in range(3):
        pickled_db_path = pickle_path + pred_cats[i][1] + ".pck"
        with open(pickled_db_path, 'rb') as fp:
                temp = pickle.load(fp)
               
        fp.close()
        processed_pickle_images.append(temp)
        
    
    print("processedpickleimage", len(processed_pickle_images))
    
    processed_pickle_images_np = np.array(list(itertools.chain.from_iterable(processed_pickle_images)))
    
    print("processed_pickle_images_np",processed_pickle_images_np.shape )
#     print("type mnet", type(mnet_loaded))
    print("type processed np" , type(processed_pickle_images_np))
#####  KMEANS CLUSTERING
    
    #clustering of predicted category images
    kmeans = KMeans(n_clusters=3, random_state=0).fit(processed_pickle_images_np)
    
    print("klabels",kmeans.labels_)
    
    print("klabels",len(kmeans.labels_))
    
    #Extract features of Query Image
    imgq = image.load_img(query_path, target_size=(224, 224))
    img_dataq = image.img_to_array(imgq)
    img_dataq = np.expand_dims(img_dataq, axis=0)
    img_dataq = preprocess_input(img_dataq)
    mnet_feature_query = model.predict(img_dataq)
    mnet_feature_np_query = np.array(mnet_feature_query)
    mnet_feature_np_query = mnet_feature_np_query.flatten()
    
#     print(mnet_feature_np_query.shape) 
    
    mnet_feature_np_query = np.reshape(mnet_feature_np_query,(1,50176))
    
    #prediction of label of query using kmeans
    query_label_prediction = kmeans.predict(mnet_feature_np_query)
    
    print(mnet_feature_np_query.shape) 
    
    print(kmeans.predict(mnet_feature_np_query))
    
    #Calculate Cosine Similarity
    similarity = []
    count = 0
    position = 0
    
    for i in range(len(processed_pickle_images)):
       
        for j in processed_pickle_images[i]:
            
            if(kmeans.labels_[position] == query_label_prediction):
               
                count = count+1
                d = distance.cosine(j,mnet_feature_np_query)
                sim = (1-d)*(pred_cats[i][0])
                similarity.append((sim,image_names[position]))
            
            position = position + 1 
    print("position", position)
    print("count", count)
#    Calculate feature similarity of query image with every image from the predicted category
#     for i in range(0,len(mnet_loaded)):
   
#         if kmeans.labels_[i] == query_label_prediction:
#             count = count+1
#             d = distance.cosine(mnet_loaded[i],mnet_feature_np_query)
#             sim = 1-d
#             similarity.append((sim,image_names[count-1]))
#     print("count",count)
    # To display Image    
    def show_img(path):
        img =imread(path, mode="RGB")
        plt.imshow(img)
        plt.show()

    # Picking top 6 image similarities
    des_similarity = sorted(similarity,reverse=True)
    des_similarity = des_similarity[:6]
    print(des_similarity)
    
    # Give the Semi_images path 
    print ('Query image ==========================================')
    show_img(query_path)

    print ('Result images ========================================')
    
    # display top 6 images 
    for i in range(len(des_similarity)):
        print("similarity",des_similarity[i][0])
        result_image_path = image_path+ "/"+des_similarity[i][1]
        if(os.path.isfile(result_image_path)):
            show_img(result_image_path)

    end = time.time()
    
    total_time_main = end - start
    print("total_time_main", total_time_main)

