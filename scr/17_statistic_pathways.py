import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pyalluvial.alluvial as alluvial
import numpy as np
from statsmodels.formula.api import ols
import statsmodels.api as sm
import scikit_posthocs as sp
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats
from sklearn.decomposition import PCA


df = pd.read_csv('../../Data/miRNA_Pathways_statistical_difference.tsv', sep = '\t')
print(df)

for i in df['Table'].unique():
    print(f'============{str(i)}=============')
    df_i = df[df['Table'] == str(i)]

    DF5 = df_i[df_i['Region']=="5'UTR"]
    DF3 = df_i[df_i['Region']=="3'UTR"]



    counts = DF5['count']
    stat, p_value = stats.shapiro(counts)
    print(f'Shapiro-Wilk: {stat}, p-valor: {p_value}')

    groups = [group['count'].values for name, group in DF5.groupby('function')]
    kruskal_result = stats.kruskal(*groups)
    print(f'Kruskal {kruskal_result}')

    dunn_result = sp.posthoc_dunn(DF5, val_col='count', group_col='function')
    print('Dunn')
    print(dunn_result)
    dunn_result.to_csv(f'dunn_5{str[i].replace({', ':'', "'": ''}.tsv')




    counts = DF3['count']
    stat, p_value = stats.shapiro(counts)
    print(f'Shapiro-Wilk: {stat}, p-valor: {p_value}')

    groups = [group['count'].values for name, group in DF3.groupby('function')]
    kruskal_result = stats.kruskal(*groups)
    print(f'Kruskal {kruskal_result}')


    dunn_result = sp.posthoc_dunn(DF3, val_col='count', group_col='function')
    print('Dunn')
    print(dunn_result)
    dunn_result.to_csv(f'dunn_3{str[i].replace({', ':'', "'": ''}.tsv')
