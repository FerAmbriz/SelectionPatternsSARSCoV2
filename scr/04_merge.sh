#/bin/bash
d=($(ls -d $1/*/))
for i in ${d[@]};do
  echo $i
  cat $i/entropy.tsv >> $1/raw_data_entropy.tsv
done
