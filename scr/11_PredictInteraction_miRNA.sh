#!/bin/bash

miRNA=../../Data/mature_homo.fa
fastaUTR=$(ls $1/*.fasta)
output=../../Data/Estratos/miRNA_predict

for i in ${fastaUTR[@]};do
    ID=${i%.fasta}; ID=$(basename $ID)
    echo $ID
    RNAplex -q ${miRNA} -t ${i} > ${output}/${ID}_predicted_miRNA.txt 
done
figlet 'Done'
#bash 12_PredictInteraction_miRNA.sh ../Data/FastaPredict/conserved_regions_UTR_time.fasta ../Data/FastaPredict/conserved_regions_UTR_time_predicted_miRNA.txt 
#bash 12_PredictInteraction_miRNA.sh ../Data/FastaPredict/conserved_regions_UTR_time.fasta ../Data/FastaPredict/conserved_SinFold_regions_UTR_time_predicted_miRNA.txt 
