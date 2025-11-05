from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
import csv
import os

#Cria as postas para armazenar os arquivos extraidos do streetservice
diretorio = os.path.dirname(os.path.abspath(__file__))
porcentagem = "porcentagem"
qtdArvore = "qtdArvore"
caminhoPastaPorcentagem = os.path.join(diretorio, porcentagem)
caminhoPastaQtdArvore = os.path.join(diretorio, qtdArvore)
if not os.path.exists(caminhoPastaPorcentagem):
    os.makedirs(caminhoPastaPorcentagem)
if not os.path.exists(caminhoPastaQtdArvore):
    os.makedirs(caminhoPastaQtdArvore)

#leia os dados dos alimentadores que se deseja extrair
df = pd.read_csv('dados_alimentador.csv',delimiter=';')
#perguntas para acessar o streetservice
nomeAplicativo = input("Digite o Nome do Usuário: ")
tokenAplicativo = input("Digite o Nome do Token do Aplicativo: ")
#abrindo o google chrome e definindo a pagina do streetservice
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://streetservice.com.br/acesso/login.php')
sleep(2.5)
#procura o elemento username / token na pagina do streetservice e envia os dados fornecidos
loginStreetService =driver.find_element(By.XPATH, '//*[@id="username"]')
senhaStreetService =driver.find_element(By.XPATH, '//*[@id="token"]')
loginStreetService.send_keys(nomeAplicativo)
senhaStreetService.send_keys(tokenAplicativo)
botaoEntrar = driver.find_element(By.XPATH,'//*[@id="login-form"]/button')
botaoEntrar.click()
sleep(5)
#entra na pagina status para estrair dados do streetservice
driver.get('https://streetservice.com.br/acesso/status.php')
sleep(10)
equipeStreetService = driver.find_element(By.XPATH,'//*[@id="equipe"]')
equipeStreetService.send_keys("Poda de árvores")
sleep(0.5)

#For para pegar quantidade de arvores
for index, row in df.iterrows():
    alimentador = row['Alimentador']
    alimentadorStreetService = driver.find_element(By.XPATH,'//*[@id="alimentador"]')
    alimentadorStreetService.send_keys(alimentador)
    sleep(0.5)
    tabelaAlimentadorQtd = driver.find_element(By.XPATH,'//*[@id="tabelaPivot"]')
    linhas = tabelaAlimentadorQtd.find_elements(By.TAG_NAME, "tr")
    dadosTabelaQtd = []
    for linha in linhas:
        celulas = linha.find_elements(By.XPATH, ".//th | .//td")
        if celulas:
           linha_dados = [celula.text.strip() for celula in celulas]
           dadosTabelaQtd.append(linha_dados)
    nome_arquivo = caminhoPastaQtdArvore +"/"+ f"{alimentador}_quantidadeArvores.csv"
    df_tabela = pd.DataFrame(dadosTabelaQtd)
    df_tabela.to_csv(nome_arquivo, index=False, header=False, encoding='utf-8', sep=';')
    sleep(0.5)
    tabelaAlimentadorPorcentagem = driver.find_element(By.XPATH,'//*[@id="tabelaDados"]')
    linhas = tabelaAlimentadorPorcentagem.find_elements(By.TAG_NAME, "tr")
    dadosTabelaPorcentagem = []
    for linha in linhas:
        celulas = linha.find_elements(By.XPATH, ".//th | .//td")
        if celulas:
           linha_dados = [celula.text.strip() for celula in celulas]
           dadosTabelaPorcentagem.append(linha_dados)
    nome_arquivo = caminhoPastaPorcentagem +"/"+ f"{alimentador}_Porcentagem.csv"
    df_tabela = pd.DataFrame(dadosTabelaPorcentagem)
    df_tabela.to_csv(nome_arquivo, index=False, header=False, encoding='utf-8', sep=';')
    sleep(0.5)

print("Extração de Dados Terminada! ")
input("Precione qualquer Tecla")