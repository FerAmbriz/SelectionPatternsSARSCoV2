import pandas as pd
import os

from Bio import SeqIO
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import Phylo
from Bio.Align import MultipleSeqAlignment

from tqdm import tqdm
from multiprocessing import Pool
#import shutil
import numpy as np
from concurrent.futures import ProcessPoolExecutor

path_files = '../../Data/bin_distanciasEuclideanas2'
#path_files = '../../Data/Too_large_bin_distanciasEuclideanas'
output = '../../Data/identity_final2'
done_files = '../../Data/done_identity2'
fasta = '/home/ferambriz/Projects/SARS-CoV-2/Data/BloqueHuman/ID_Human/fasta_sin_duplicados.fasta'

files = os.listdir(path_files)
seq_records = SeqIO.to_dict(SeqIO.parse(fasta, 'fasta'))

def process_file(i):
    print(f'============{i}============')
    df_i = pd.read_csv(f'{path_files}/{i}', sep='\t')
    print(df_i)

    lst_i = df_i['ID']
    seq_records_filtrados = {id: seq_records[id] for id in lst_i if id in seq_records}

    seq_records_list = list(seq_records_filtrados.values())
    with open(f'../../Data/alignment2/{i}.fasta', 'w') as output_handle:
        SeqIO.write(seq_records_list, output_handle, 'fasta')

with ProcessPoolExecutor() as executor:
    results = list(executor.map(process_file, files))

    #shutil.move(f'{path_files}/{i}', {done_files})

print('============= All done =============')
