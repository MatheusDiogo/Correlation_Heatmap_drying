!pip install --upgrade xlrd
!pip install openpyxl
##################################################################################
#                         Campo de Bibliotecas                                   #
##################################################################################
import pandas as pd
import seaborn as sn
import numpy as np
import matplotlib.pyplot as mp

data = pd.read_excel("Dados.xlsx",engine='openpyxl')

matriz=[]
matriz = data.corr()

#matriz.to_excel("mapa pearson SECAGEM.xlsx",index=False,columns=None,header=False) #convertendo para planilha excel

mp.figure(figsize=(16,9))
matrix = np.triu(matriz)
try:
    sn.heatmap(matriz, annot = True, fmt = ".2f", linewidths = .6, linecolor="k", mask=matrix)
except ValueError:  #raised if `y` is empty.
    pass
