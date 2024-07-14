#!/bin/bash
for i in $(ls *.gbk)
do
i=${i/.gbk/}
seqret -sequence $i.gbk -outseq $i.fasta
done