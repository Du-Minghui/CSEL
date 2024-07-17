#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from bs4 import BeautifulSoup
import argparse


# In[ ]:


def html2csv(path):
    table = pd.read_html(path)
    htmlfile = open(path , 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    soup = BeautifulSoup(htmlhandle, 'lxml')
    NC_id_box = soup.find_all('div', attrs={'class': 'record-overview-header'})
    df = pd.DataFrame(columns=['Region', 'Type', 'From', 'To','Most similar known cluster','Most similar known cluster.1','Similarity'])
    for i in range(0,len(NC_id_box)):            
        NC_id  = NC_id_box[i]
        NC_id = NC_id.text.strip()
        table[i]['Region'] = NC_id  + '_' + table[i]['Region']
        df = df.append(table[i])
    df['Region'] = df['Region'].str.replace("&nbsp", "_")
    return df


# In[ ]:


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input", required=True,
                        help="Input file.", metavar="FILE")
    parser.add_argument("-o", "--output", dest="output", required=True,
                      help="Output file.", metavar="FILE")
    options = parser.parse_args()


# In[ ]:


df = html2csv(options.input)
df.to_csv(options.output,index=None)

