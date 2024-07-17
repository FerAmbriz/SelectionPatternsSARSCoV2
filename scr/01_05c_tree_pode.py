import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore', category=pd.errors.SettingWithCopyWarning)

path_files = '../../Data/identity_final2'
output = '../../Data/ID_poded2'

files = os.listdir(path_files)
def addhead(string):
    return '>' + string

def pode_tree(df, output_file):
    umbral = 0
    lst_mantein = []; lst_pode = []

    for i in df['Unnamed: 0']:
        df_i = df[df['Unnamed: 0'] == i]
        df_i.drop(['Unnamed: 0'], axis = 1, inplace = True)
        df_i = df_i.T

        df_i = df_i[(df_i[df_i.columns[0]] <= umbral) & (~df_i.index.isin([i]))]
        if len(df_i) > 0:
            if i not in lst_pode:
                lst_mantein.append(i)
            for j in df_i.index:
                if j not in lst_mantein:
                    lst_pode.append(j)

    lst_pode = list(set(lst_pode))
    print(f'Podando {len(lst_pode)} muestras')

    df=df[~df['Unnamed: 0'].isin(lst_pode)]

    df['Unnamed: 0'] = list(map(addhead, df['Unnamed: 0']))
    df['Unnamed: 0'].to_csv(output_file, sep='\t', index = False, header = False)


#ffile = [f'{path_files}/bin_France_(2021-05-01, 2022-01-01].tsv']

for i in files:
#for i in ffile:
    print(f'Procesando ... {i}')

    if os.path.getsize(f'{path_files}/{i}') == 0:
        print('Archivo vacio')
    else:
        df = pd.read_csv(f'{path_files}/{i}', sep = '\t')
        print(df)
        pode_tree(df, f'{output}/{i}')

    print(f'Done {i}')

print('======= All done =======')
