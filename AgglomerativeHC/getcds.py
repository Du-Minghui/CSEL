#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio import SeqIO
import pandas as pd
import numpy as np
import argparse


# In[2]:


def getcds(record):
    cds_count = 0
    total_length = 0
    for feature in record.features:
        # 如果是CDS特征
        if feature.type == "CDS":
            # 获取位置信息
            location = feature.location
            # 计算长度并累加到总长度中
            length = len(location)
            total_length += length
            # 计算CDS数量
            cds_count += 1
    return cds_count


# In[ ]:


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input", required=True,
                        help="Input file.", metavar="FILE")
    parser.add_argument("-o", "--output", dest="output", required=True,
                        help="Output file.", metavar="FILE")
    options = parser.parse_args()


# In[26]:


gbk = options.input


# In[13]:


record = SeqIO.read(gbk, "genbank")


# In[22]:


cds_count = getcds(record)


# In[23]:


seq_length = len(record.seq)


# In[28]:


df = pd.DataFrame({ 'gbk':[gbk],
                    'cds_count':[cds_count],  
                    'seq_length':[seq_length]})


# In[31]:


df.to_csv(options.output,index=False,header=0)

