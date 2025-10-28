import pandas as pd
import csv
import os

servicosFaltantes = [
    'Serviço LV/Desligar',
    'Serviço Urgente',
    'Serviço Executar',
    'Serviço Futuro'
]

diretorio = os.path.dirname(os.path.abspath(__file__)) + '\porcentagem'



for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.csv'):
        caminhoArquivo = os.path.join(diretorio,arquivo)
        df = pd.read_csv(caminhoArquivo, sep=';', encoding='utf-8')
        df['Quantidade'] = df['Quantidade'].replace('.','A')
        df=df[~df['Status'].isin(['Serviço Cancelado', 'TOTAL'])]
        filtro=df[df['Status'].isin(servicosFaltantes)]
        soma = filtro['Quantidade'].sum()

print(df)