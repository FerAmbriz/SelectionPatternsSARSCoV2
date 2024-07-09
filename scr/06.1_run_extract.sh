#!/bin/bash 
d=($(ls -d $1/*/))

for i in ${d[@]};do
  echo =============$i==================
  python 06_extract_sequences_predominant.py $i
done

figlet 'Done'
