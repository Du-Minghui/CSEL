#!/bin/bash
for i in $(ls *_genomic.fna)
do
  i=${i/_genomic.fna/}
  run_antismash /home/dmh/genome_other/${i}_genomic.fna /home/dmh/antismash/other --cb-general --cb-knownclusters --cb-subclusters --genefinding-tool prodigal --allow-long-headers
done
