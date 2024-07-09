#!/bin/bash

d=($(ls -d $1/*/))

for i in ${d[@]};do
  echo =============$i==================
  python 04_entropy.py $i
done

figlet 'Done'
