#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import argparse


# In[ ]:


def gcf2bgc(input_file):
    bgc_list = pd.read_csv(input_file ,header=None)
    gcf_name_split = input_file.split(".")
    gcf_name = '.'.join(gcf_name_split[0:2])
    bgc_list[1] = gcf_name
    return bgc_list 


# In[ ]:


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input", required=True,
                        help="Input file.", metavar="FILE")
    parser.add_argument("-o", "--output", dest="output", required=True,
                        help="Output file.", metavar="FILE")
    options = parser.parse_args()


# In[ ]:


gcf_bgc = gcf2bgc(options.input)
gcf_bgc.to_csv(options.output,index=False,header=0)

