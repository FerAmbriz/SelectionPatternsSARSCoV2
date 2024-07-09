#!/bin/bash

cd $1
d=($(ls *.txt))

for i in ${d[@]};do
  echo =============$i==================
  RNAplot -i ${i} --id-prefix=${i%.txt}
done

figlet 'Done'
