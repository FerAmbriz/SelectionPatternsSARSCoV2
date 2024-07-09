import pandas as pd
import numpy as np
import math
import os
import seaborn as sns
import matplotlib.pyplot as plt
import math
import sys
import warnings
from collections import Counter
warnings.filterwarnings("ignore", category=FutureWarning)

inp = sys.argv[1]
path = inp + '/nextclade.aligned.fasta'

with open(path, 'r') as f:
    lines = f.readlines()

# Filtrar las líneas que no empiezan con '>'
lines = [line.strip() for line in lines if not line.startswith('>')]

# Convertir las líneas a listas de caracteres
lines = [list(line) for line in lines]

bases = ['A', 'G', 'C', 'T']

def contar_valores_unicos(array):
    counter = Counter(array)
    x = {key: value for key, value in counter.items() if key in bases}
    t = sum(x.values())

    lst = []
    for xj in x.values():
        pj = xj/t
        x = pj * math.log2(pj)
        lst.append(x)

    Hi = -sum(lst)
    return Hi

# Aplicar la función a cada columna
H = [contar_valores_unicos(column) for column in zip(*lines)]

df = pd.DataFrame({
    'Site': list(range(1, len(H)+1)),
    'H': H
})

print(df)
print('-------Annotating------')
bed_v2 = pd.read_csv('annotation_ncov.gff', header = None)
bed_v2.drop([0,1,2], inplace = True)
bed_v2 = bed_v2[0].str.split('\t', expand = True)
bed_v2.columns = bed_v2.loc[3]; bed_v2.drop([3], inplace = True)
bed_v2['start'] = list(map(int, bed_v2['start'])); bed_v2['end'] = list(map(int, bed_v2['end']))
bed_v2[['a', 'gene']] = bed_v2['attribute'].str.split('=', expand = True)

# Agregar UTR
utr1 = {'# seqname': '.', 'source': '.', 'feature': 'UTR', 'start': 1, 'end':265, 'score': '.',
                  'strand': '+', 'frame':'.', 'attribute': '.', 'a': '.', 'gene': "5'UTR"}
utr2 = {'# seqname': '.', 'source': '.', 'feature': 'UTR', 'start': 29675, 'end':29903, 'score': '.',
                  'strand': '+', 'frame':'.', 'attribute': '.', 'a': '.', 'gene': "3'UTR"}
orf10 = {'# seqname': '.', 'source': '.', 'feature': 'gene', 'start': 29558, 'end':29674, 'score': '.',
                  'strand': '+', 'frame':'.', 'attribute': '.', 'a': '.', 'gene': "3'UTR"}
orf10 = {'# seqname': '.', 'source': '.', 'feature': 'gene', 'start': 29558, 'end':29674, 'score': '.',
                  'strand': '+', 'frame':'.', 'attribute': '.', 'a': '.', 'gene': "ORF10"}
# termina en 21561
TRS_B1 = {'# seqname': '.', 'source': '.', 'feature': 'gene', 'start': 21556, 'end':21561, 'score': '.',
                  'strand': '+', 'frame':'.', 'attribute': '.', 'a': '.', 'gene': "TRS-B-1spike"}
TRS_B2 = {'# seqname': '.', 'source': '.', 'feature': 'gene', 'start': 25385, 'end':25390, 'score': '.',
                  'strand': '+', 'frame':'.', 'attribute': '.', 'a': '.', 'gene': "TRS-B-2orf3A"}


bed_v2 = bed_v2.append(utr1, ignore_index=True); bed_v2 = bed_v2.append(utr2, ignore_index=True);  bed_v2 = bed_v2.append(orf10, ignore_index=True)
bed_v2 = bed_v2.append(TRS_B1, ignore_index=True); bed_v2 = bed_v2.append(TRS_B2, ignore_index=True)


def annotator_v2 (site):
    genes = list(bed_v2[(bed_v2['start']<= site) & (site <= bed_v2['end'])]['gene'])
    if genes:  # Verificar si la lista no está vacía
        return genes[0]
    else:
        return 'NaN'

df['Region'] = list(map(annotator_v2, df['Site']))
df['Variant'] = [inp] * len(df)
print(df)

df.to_csv(inp + '/entropy.tsv', sep = '\t')
