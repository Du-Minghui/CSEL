#!/bin/bash
for i in $(ls *_genomic.fna)
do
  i=${i/_genomic.fna/}
  run_antismash /home/dmh/genome_Bacillus/${i}_genomic.fna /home/dmh/antismash/Bacillus --cb-general --cb-knownclusters --cb-subclusters --genefinding-tool prodigal --allow-long-headers
done