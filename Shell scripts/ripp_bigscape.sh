#!/bin/bash
while read line
do
python3 /home/dmh/miniconda3/envs/bigscape/lib/python3.7/site-packages/BiG-SCAPE/bigscape.py \
        -c 10 -i /home/dmh/bigscape/ripps/gbk/$line \
        -o /home/dmh/bigscape/ripps/res/$line \
        --pfam_dir /home/dmh/data/databases/pfam/34.0 \
        --mix --no_classify 
done < filename.txt

