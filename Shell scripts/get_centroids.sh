#!/bin/bash
while read line
do
  python3 get_centroids.py -i /home/dmh/bigscape/all/GCF_csv/"$line"
done < filename.txt