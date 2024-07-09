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


path_files = '../../Data/bin_distanciasEuclideanas'
output = '../../Data/identity_final'
done_files = '../../Data/done_identity'
fasta = '/home/ferambriz/Projects/SARS-CoV-2/Data/BloqueHuman/ID_Human/fasta_sin_duplicados.fasta'

files = os.listdir(path_files)
seq_records = SeqIO.to_dict(SeqIO.parse(fasta, 'fasta'))

for i in files:
    print(f'============{i}============')
    df_i = pd.read_csv(f'{path_files}/{i}', sep='\t')
    print(df_i)

    lst_i = df_i['ID']
    seq_records_filtrados = {id: seq_records[id] for id in lst_i if id in seq_records}

    seq_records_list = list(seq_records_filtrados.values())
    alignment = MultipleSeqAlignment(seq_records_list)
    print('done alignment')

    calculator = DistanceCalculator('identity')
    dm = calculator.get_distance(alignment)
    print('done get_distance')

    np.savetxt(f'{output}/{i}', dm, delimiter='\t')

    df_ii = pd.read_csv(f'{output}/{i}', sep = '\t', header = None)
    df_ii.columns = dm.names
    df_ii.index = dm.names

    df_ii.to_csv(f'{output}/{i}', sep='\t')
    #shutil.move(f'{path_files}/{i}', {done_files})

print('============= All done =============')
