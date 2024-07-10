#!/bin/bash

#files=$(ls "identity_final2")

#for i in ${files[@]};do
#  echo "mv bin_distanciasEuclideanas2/$i" done_identity2
#done

find "identity_final2" -type f -print0 | while IFS= read -r -d '' file; do
    ID=${file##*/};
    mv bin_distanciasEuclideanas2/"$ID" done_identity2
done
