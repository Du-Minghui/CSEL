#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3, pandas as pd, numpy as np, nltk, string, matplotlib.pyplot as plt, seaborn as sns
import string, math, pickle
import sys
import math
import srd
from pycm import *
from sklearn.model_selection import KFold
from sklearn import svm, linear_model, ensemble
from mlxtend.classifier import StackingClassifier
from sklearn import model_selection
from sklearn.model_selection import cross_val_score
import warnings
warnings.filterwarnings("ignore")
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# In[2]:


rf = ensemble.RandomForestClassifier(n_estimators=172,
                                     criterion='gini',
                                     min_samples_split=2,
                                     min_samples_leaf=1,
                                     max_features='log2',
                                     class_weight='balanced',
                                     bootstrap=False,
                                     n_jobs=-1)
c_rf = CalibratedClassifierCV(rf, method='sigmoid')

ets = ensemble.ExtraTreesClassifier(n_estimators=80,
                                    criterion='entropy',
                                    min_samples_split=4,
                                    min_samples_leaf=1,
                                    max_features='log2',
                                    class_weight='balanced_subsample',
                                    bootstrap=False,
                                    n_jobs=-1)
c_ets = CalibratedClassifierCV(ets, method='sigmoid')

nusvm = svm.NuSVC(nu=0.4899941321592568,
                  kernel='rbf',
                  shrinking=True,
                  class_weight='balanced',
                  probability = True)

c_nusvm = CalibratedClassifierCV(nusvm, method='sigmoid')

ridge = linear_model.RidgeClassifier(alpha=3.714336809225957,
                                     normalize=True,
                                     copy_X=False,
                                     class_weight='balanced',
                                     solver='lsqr')
c_ridge = CalibratedClassifierCV(ridge, method='sigmoid')


# In[3]:


class stacking_layer:
    def __init__(self,index):
        self.ind_layer=index
        self.classifier0=StackingClassifier(classifiers=[c_rf,c_ets,c_nusvm], meta_classifier= c_ridge)
        self.classifier1=StackingClassifier(classifiers=[c_rf,c_ets,c_nusvm], meta_classifier= c_ridge)
        self.classifier2=StackingClassifier(classifiers=[c_rf,c_ets,c_ridge], meta_classifier= c_nusvm)
        self.classifier3=StackingClassifier(classifiers=[c_rf,c_ets,c_ridge], meta_classifier= c_nusvm)
        
    def fit(self,X,y):
        self.classifier0.fit(X,y)
        self.classifier1.fit(X,y)
        self.classifier2.fit(X,y)
        self.classifier3.fit(X,y)

    def predict(self,X):
        y_prob=self.classifier0.predict_proba(X)
        y_prob+=self.classifier1.predict_proba(X)
        y_prob+=self.classifier2.predict_proba(X)
        y_prob+=self.classifier3.predict_proba(X)
        y_pred=[]
        for prob in y_prob/4:
            y_pred.append(np.argmax(prob))
        return np.array(y_pred)

    def predict_proba(self,X):
        y_prob=self.classifier0.predict_proba(X)
        y_prob=np.column_stack((y_prob,self.classifier1.predict_proba(X)))
        y_prob=np.column_stack((y_prob,self.classifier2.predict_proba(X)))
        y_prob=np.column_stack((y_prob,self.classifier3.predict_proba(X)))
        return y_prob


# In[4]:


class cascade_layer:
    def __init__(self,num_layer):
        self.layers=[]
        self.num_layer = num_layer
              
    def fit(self,X,y):
        for num in range(self.num_layer):
            self.layers.append(stacking_layer(num))
        inputX=X
        for l in self.layers:
            l.fit(inputX,y)
            y0=l.predict_proba(inputX)
            inputX=np.column_stack((X,y0))
                      
    def predict(self,X):
        inputX=X
        for l in self.layers:
            y_pred=l.predict(inputX)
            y0=l.predict_proba(inputX)        
            inputX=np.column_stack((X,y0))
        return y_pred


# In[4]:


class cascade_model(object):
    def __init__(self, max_layer=100):
        
        self.max_layer = max_layer
        self.model = []    

    def fit(self, X, y):
        train_acc = 0.0
        layer = 1
        top_layer = 0
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
        print('================================')
        print('Model starts...')
        print('--------------------------------')

        while layer < self.max_layer:
        
            new_layer = cascade_layer(layer)
            new_layer.fit(X_train,y_train)
            pred = new_layer.predict(X_test)
            temp_acc =accuracy_score(y_test, pred)
            
            print("layer : {} | acc : {:.6f}".format(layer, temp_acc))
 
            if train_acc < temp_acc:
                train_acc = temp_acc
                top_layer = layer
            else:
                break
            
            layer = layer + 1
            self.model.append(new_layer)
        print('================================')

        for index in range(len(self.model), top_layer + 1, -1):  
            self.model.pop()

    def predict(self, X):
        for layer in self.model:
            pred = layer.predict(X)
        return pred

