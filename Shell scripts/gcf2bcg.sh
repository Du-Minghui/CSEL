#!/bin/bash
while read line
do
  python3 gcf2bgc.py -i $line -o /home/dmh/bigscape/all/GCF_bgc/$line
done < filename.txt