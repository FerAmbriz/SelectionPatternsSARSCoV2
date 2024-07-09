#!/bin/bash


find "../../Data/alignment2" -type f -print0 | while IFS= read -r -d '' file; do
    echo Processing ... "${file}"
    mkdir "${file%.fasta}"
    nextclade run --dataset-name="sars-cov-2" --output-all="${file%.fasta}" "${file}"
done
echo '=== Done ==='
