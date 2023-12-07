#!/usr/bin/env python
# coding: utf-8

# In[1]:


import joblib
import pandas as pd
from csm import cascade_model
import argparse


# In[4]:


def running_model(X_test):
    print('Model loading')
    loaded_model = joblib.load("CSM.joblib.dat")  
    print('Test dataset loading')
    X_test  = pd.read_csv(X_test, index_col=0)  
    print('Model running')
    y_pred = loaded_model.predict(X_test)    
    df = pd.DataFrame(data=y_pred, 
                  index =X_test.index,
                  columns=['Antibacterial_activity'])
    return df 


# In[5]:


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input", required=True,
                        help="Input file.", metavar="FILE")
    parser.add_argument("-o", "--output", dest="output", required=True,
                      help="Output file.", metavar="FILE")
    options = parser.parse_args()


# In[ ]:


df = running_model(options.input)


# In[ ]:


df.to_csv(options.output)

