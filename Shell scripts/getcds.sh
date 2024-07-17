#!/bin/bash
while read line
do
  python3 getcds.py -i /home/dmh/bigscape/all/all_newbgcs/$line -o /home/dmh/bigscape/all/bgc_cds_len/cds_len/$line.csv
done < filename.txt