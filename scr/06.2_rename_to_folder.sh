#!/bin/bash

folder=(BloqueHuman BloquesTemporalClusters BloquesVariantes_compress)

for i in ${folder[@]};do
  echo $i
  if [[ "$i" != 'BloqueHuman' ]];then
    d=($(ls -d ${i}/*/))
    for j in ${d[@]};do
      ID=$(basename "$j"); ID=${ID%_*}
      cp -r $j/concensus.fasta $i/concensus_sequence_${ID}.fasta
    done

  fi
done
