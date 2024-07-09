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
output = '../../Data/identity_final2'
done_files = '../../Data/done_identity2'
fasta = '/home/ferambriz/Projects/SARS-CoV-2/Data/BloqueHuman/ID_Human/fasta_sin_duplicados.fasta'

files = os.listdir(path_files)
seq_records = SeqIO.to_dict(SeqIO.parse(fasta, 'fasta'))

def process_file(i):
    print(f'============{i}============')
    # Leer el alineamiento resultante
    alignment = AlignIO.read(f"../../Data/alignment2/{i}/nextclade.aligned.fasta", "fasta")
    print(f'done alignment {i}')

    calculator = DistanceCalculator('identity')
    dm = calculator.get_distance(alignment)
    print(f'done get_distance {i}')

    np.savetxt(f'{output}/{i}', dm, delimiter='\t')

    df_ii = pd.read_csv(f'{output}/{i}', sep = '\t', header = None)
    df_ii.columns = dm.names
    df_ii.index = dm.names
    df_ii.to_csv(f'{output}/{i}', sep='\t')

with ProcessPoolExecutor() as executor:
    results = list(executor.map(process_file, files))

print('============= All done =============')
