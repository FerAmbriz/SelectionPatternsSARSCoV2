#!/bin/bash

miRNA=../Data/mature_homo.fa
#UTR=conserved_regions_UTR.fasta
fastaUTR=$1
output=$2

RNAplex -q ${miRNA} -t ${fastaUTR} > ${output}


#bash 12_PredictInteraction_miRNA.sh ../Data/FastaPredict/conserved_regions_UTR_time.fasta ../Data/FastaPredict/conserved_regions_UTR_time_predicted_miRNA.txt 
#bash 12_PredictInteraction_miRNA.sh ../Data/FastaPredict/conserved_regions_UTR_time.fasta ../Data/FastaPredict/conserved_SinFold_regions_UTR_time_predicted_miRNA.txt 
