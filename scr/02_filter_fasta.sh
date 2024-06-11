#!/bin/bash

for i in $1/*.tsv; do
  awk 'NR==FNR{a[$0];next} /^>/{f=($1 in a)} f' ${i} /home/ferambriz/Projects/SARS-CoV-2/GISAID/to_run/raw_data.fasta > ${i%*.tsv}.fasta
  awk 'BEGIN{FS=OFS="\t"} NR==FNR{gsub(/^>/,""); a[$1];next} ($1 in a)' ${i} /home/ferambriz/Projects/SARS-CoV-2/GISAID/to_run/raw_data.tsv > ${i%*.tsv}_metadata.tsv
done
