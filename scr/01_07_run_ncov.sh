#!/bin/bash

ori_dir=$(pwd)
direc="/home/ferambriz/Projects/SARS-CoV-2/Data/mergeID/final"

for i in ${direc}/*.fasta;do
  ID=$(basename "$i")
  cd $ori_dir
  bash /home/ferambriz/Programs/cluster_temporal/remake_ncov.sh
  mv ncov /home/ferambriz/Programs/cluster_temporal/ 

  figlet 'DONE CLONE'

  cp "$i" /home/ferambriz/Programs/cluster_temporal/ncov/data/custom.sequences.fasta
  cp "${i%.*}"_metadata.tsv /home/ferambriz/Programs/cluster_temporal/ncov/data/custom.metadata.tsv

  cd /home/ferambriz/Programs/cluster_temporal/ncov
  nextstrain build --cpus 10 . --configfile ncov-tutorial/custom-data.yaml

  figlet 'DONE ITERATION'
  mv /home/ferambriz/Programs/cluster_temporal/ncov /home/ferambriz/Programs/cluster_temporal/ncov_"${ID%.*}"
done



