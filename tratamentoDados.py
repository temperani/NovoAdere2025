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
    if arquivo.lower().endswith('.csv') and '_porcentagem' in arquivo.lower():
        caminhoArquivo = os.path.join(diretorio,arquivo)
        df = pd.read_csv(caminhoArquivo, sep=';',dtype=str, encoding='utf-8')
        df=df[~df['Status'].isin(['Serviço Cancelado', 'TOTAL'])]
        df['Quantidade_num'] = pd.to_numeric(df['Quantidade'].str.replace('.', '',regex=False),errors='coerce')
        soma = df['Quantidade_num'].sum() 
        df['% do Total'] = (df['Quantidade_num']/soma*100).round(1).astype(str)+'%'
        df=df.drop(columns=['Quantidade_num'])
        df.to_csv(caminhoArquivo,sep=";",index=False,encoding='utf-8-sig')
print("Terminou")
