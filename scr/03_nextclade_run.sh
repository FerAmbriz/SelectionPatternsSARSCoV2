#!/bin/bash

fasta=($(ls $1/*.fasta))

for i in ${fasta[@]};
do
  echo Processing ... ${i%.fasta}
  mkdir ${i%.fasta}
  nextclade run --dataset-name="sars-cov-2" --output-all="${i%.fasta}" "$i"
done

echo '=== Done ==='
