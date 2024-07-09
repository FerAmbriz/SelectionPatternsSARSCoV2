import sys
import multiprocessing

path = sys.argv[1]
file = path + '/nextclade.aligned.fasta'

def contar_valores_unicos(array):
    x = {base: array.count(base) for base in ['A', 'G', 'C', 'T']}
    if not x:  # Si el diccionario está vacío
        return 'N'
    else:
        return max(x, key=x.get)

with open(file, 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if not line.startswith('>')]
# Convertir las líneas a listas de caracteres
lines = [list(line) for line in lines]

seq = [contar_valores_unicos(list(column)) for column in zip(*lines)]

#with multiprocessing.Pool() as pool:
#    seq = pool.map(contar_valores_unicos, zip(*lines))

print(seq[0:6])
seq = ''.join(seq)

with open(path + '/concensus.fasta', 'w') as f:
    f.write(seq)
