from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
import csv
df = pd.read_csv('dados_alimentador.csv',delimiter=';')
nomeAplicativo = input("Digiete o Nome do Usuário: ")
tokenAplicativo = input("Digiete o Nome do Token do Aplicativo: ")

navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get('https://streetservice.com.br/acesso/login.php')
sleep(2.5)
loginStreetService =navegador.find_element(By.XPATH, '//*[@id="username"]')
senhaStreetService =navegador.find_element(By.XPATH, '//*[@id="token"]')
loginStreetService.send_keys(nomeAplicativo)
senhaStreetService.send_keys(tokenAplicativo)
botaoEntrar = navegador.find_element(By.XPATH,'//*[@id="login-form"]/button')
botaoEntrar.click()
sleep(5)
navegador.get('https://streetservice.com.br/acesso/status.php')
sleep(10)
equipeStreetService = navegador.find_element(By.XPATH,'//*[@id="equipe"]')
equipeStreetService.send_keys("Poda de árvores")
sleep(0.5)

for index, row in df.iterrows():
    alimentador = row['Alimentador']
    alimentadorStreetService = navegador.find_element(By.XPATH,'//*[@id="alimentador"]')
    alimentadorStreetService.send_keys(alimentador)
    sleep(0.5)
    tabelaAlimentador = navegador.find_element(By.XPATH,'//*[@id="tabelaDados"]')
    linhas = tabelaAlimentador.find_elements(By.TAG_NAME, "tr")
    dadosTabela = []
    for linha in linhas:
        celulas = linha.find_elements(By.XPATH, ".//th | .//td")
        if celulas:
           linha_dados = [celula.text.strip() for celula in celulas]
           dadosTabela.append(linha_dados)
    nome_arquivo = f"{alimentador}.csv"
    df_tabela = pd.DataFrame(dadosTabela)
    df_tabela.to_csv(nome_arquivo, index=False, header=False, encoding='utf-8', sep=';')
    sleep(0.5)
print("Extração de Dados Terminada! ")
input("Precione qualquer Tecla")