#!/bin/bash


#Los puntos (.) representan los nucleótidos que no están emparejados, es decir, aquellos que no forman un par de bases en la estructura secundaria.
#Los paréntesis abiertos (() y cerrados ()) representan los pares de bases. Un paréntesis abierto y un paréntesis cerrado que están al mismo nivel indican un par de bases. Por ejemplo, en la secuencia ((..)), los dos nucleótidos en las posiciones 1 y 6 forman un par de bases, al igual que los nucleótidos en las posiciones 2 y 5.
#phe_seq='GCGGAUUUAGCUCAGUUGGGAGAGCGCCAGACUGAAGAUCUGGAGGUCCUGUGUUCGAUCCACAGAAUUCGCACCA'
#echo $phe_seq | RNAfold > output.txt

#RNAplot -i output.txt -o output.ps

arr=($(ls $1/*.fasta))
threads=$2

extract_values (){
  arr2=()
  while [ $termina -ge $contador ]
  do
    arr2+=(${arr[$contador]})
    let contador=$contador+1
  done
}

test (){
  echo 'a'
  sleep 1
}

for (( i=0; i<${#arr[@]}; i=i+$threads));
do
  contador=$i && termina=$(($i + $(($threads - 1))))
  extract_values

  for j in ${arr2[@]};
  do
    echo $j
    ID=${j%*.fasta}
    #test &
    cat $j | RNAfold > ${ID}_predict_fold.txt &
  done
  wait
done
