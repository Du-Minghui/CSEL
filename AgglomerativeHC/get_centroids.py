#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import argparse


# In[ ]:


def get_centroids(input_file):
    bgc_list = pd.read_csv(input_file ,header=None)
    gcf = bgc_list[0].to_list()
    bgc_feature = pd.read_csv("bgc_feature.csv",index_col=0)
    gcf_bgc = bgc_feature.loc[gcf, : ]
    km = KMeans(
        n_clusters=1,
        init='random',
        n_init=1,
        max_iter=300,
        algorithm='full',
        random_state=1)
    km.fit(gcf_bgc)
    gcf_centroids = pd.DataFrame({"%s"%(gcf_name): km.cluster_centers_[0].astype(np.uint8)}, 
                                   index=bgc_feature.columns.values.tolist()).T
    return gcf_centroids


# In[ ]:


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input", required=True,
                        help="Input file.", metavar="FILE")
    #parser.add_argument("-o", "--output", dest="output", required=True,
                      #help="Output file.", metavar="FILE")
    options = parser.parse_args()


# In[ ]:


gcf_name_split = options.input.split(".")
gcf_name = '.'.join(gcf_name_split[0:2])


# In[ ]:


gcf_centroids = get_centroids(options.input)


# In[ ]:


gcf_centroids.to_csv("%s_centroids.csv"%(gcf_name))

