#!/bin/bash

folder="/home/ferambriz/Projects/SARS-CoV-2/Data/"
mkdir -p "${folder}/mergeID"

x=('(2021-05-01, 2022-01-01]' '(2020-03-01, 2020-09-01]' '(2021-01-01, 2021-05-01]' '(2020-09-01, 2021-01-01]' '(2022-06-01, 2022-11-01]' '(2010-12-05, 2020-03-01]' '(2022-01-01, 2022-06-01]')

for i in "${x[@]}"; do
  echo "========== $i =========="
  for j in "${folder}/ID_poded2"/*_"${i}".tsv; do
    echo $j
    cat "$j" >> "${folder}/mergeID/merge_ID_${i}.tsv"
  done
done
